#!/usr/bin/env python3
"""
Brand asset extraction from various sources.
Extracts colors, typography, spacing from PPTX, images, PDFs.
"""

import json
import sys
import re
from pathlib import Path
from typing import Dict, List, Any, Optional
from collections import Counter

try:
    from pptx import Presentation
    from pptx.util import Pt
    PPTX_AVAILABLE = True
except ImportError:
    PPTX_AVAILABLE = False

try:
    from PIL import Image
    import colorsys
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False


class ColorExtractor:
    """Extract and analyze colors from various sources."""

    @staticmethod
    def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
        """Convert HEX to RGB."""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    @staticmethod
    def rgb_to_hex(rgb: tuple[int, int, int]) -> str:
        """Convert RGB to HEX."""
        return '#{:02x}{:02x}{:02x}'.format(*rgb)

    @staticmethod
    def rgb_to_hsl(rgb: tuple[int, int, int]) -> tuple[float, float, float]:
        """Convert RGB to HSL."""
        r, g, b = [x / 255.0 for x in rgb]
        h, l, s = colorsys.rgb_to_hls(r, g, b)
        return (h * 360, s * 100, l * 100)

    @staticmethod
    def calculate_luminance(rgb: tuple[int, int, int]) -> float:
        """Calculate relative luminance for WCAG contrast."""
        def adjust(c):
            c = c / 255.0
            return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

        r, g, b = [adjust(c) for c in rgb]
        return 0.2126 * r + 0.7152 * g + 0.0722 * b

    @staticmethod
    def contrast_ratio(rgb1: tuple[int, int, int], rgb2: tuple[int, int, int]) -> float:
        """Calculate WCAG contrast ratio between two colors."""
        l1 = ColorExtractor.calculate_luminance(rgb1)
        l2 = ColorExtractor.calculate_luminance(rgb2)
        lighter = max(l1, l2)
        darker = min(l1, l2)
        return (lighter + 0.05) / (darker + 0.05)

    @staticmethod
    def generate_tints_shades(hex_color: str, steps: int = 5) -> Dict[str, List[str]]:
        """Generate tint and shade variations."""
        rgb = ColorExtractor.hex_to_rgb(hex_color)
        h, s, l = ColorExtractor.rgb_to_hsl(rgb)

        tints = []
        shades = []

        for i in range(1, steps + 1):
            # Tints (lighter)
            tint_l = l + (100 - l) * (i / (steps + 1))
            tint_rgb = colorsys.hls_to_rgb(h/360, tint_l/100, s/100)
            tint_rgb = tuple(int(x * 255) for x in tint_rgb)
            tints.append(ColorExtractor.rgb_to_hex(tint_rgb))

            # Shades (darker)
            shade_l = l * (1 - i / (steps + 1))
            shade_rgb = colorsys.hls_to_rgb(h/360, shade_l/100, s/100)
            shade_rgb = tuple(int(x * 255) for x in shade_rgb)
            shades.append(ColorExtractor.rgb_to_hex(shade_rgb))

        return {"tints": tints, "shades": shades}


class PPTXExtractor:
    """Extract brand assets from PowerPoint files."""

    def __init__(self, file_path: str):
        if not PPTX_AVAILABLE:
            raise ImportError("python-pptx not installed. Run: pip install python-pptx")
        self.prs = Presentation(file_path)

    def extract_colors(self) -> List[str]:
        """Extract colors used in slides."""
        colors = []

        for slide in self.prs.slides:
            for shape in slide.shapes:
                # Fill colors
                if shape.fill.type == 1:  # SOLID
                    try:
                        rgb = shape.fill.fore_color.rgb
                        hex_color = '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])
                        colors.append(hex_color)
                    except:
                        pass

                # Text colors
                if hasattr(shape, 'text_frame'):
                    for paragraph in shape.text_frame.paragraphs:
                        for run in paragraph.runs:
                            try:
                                rgb = run.font.color.rgb
                                hex_color = '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])
                                colors.append(hex_color)
                            except:
                                pass

        # Return most common colors
        color_counts = Counter(colors)
        return [color for color, _ in color_counts.most_common(10)]

    def extract_fonts(self) -> Dict[str, Any]:
        """Extract typography information."""
        fonts = []
        font_sizes = []

        for slide in self.prs.slides:
            for shape in slide.shapes:
                if hasattr(shape, 'text_frame'):
                    for paragraph in shape.text_frame.paragraphs:
                        for run in paragraph.runs:
                            if run.font.name:
                                fonts.append(run.font.name)
                            if run.font.size:
                                font_sizes.append(run.font.size.pt)

        font_counts = Counter(fonts)
        size_counts = Counter(font_sizes)

        return {
            "primary_font": font_counts.most_common(1)[0][0] if font_counts else "Arial",
            "common_sizes": [size for size, _ in size_counts.most_common(5)],
            "all_fonts": list(set(fonts))
        }


class ImageExtractor:
    """Extract dominant colors from images."""

    def __init__(self, file_path: str):
        if not PIL_AVAILABLE:
            raise ImportError("Pillow not installed. Run: pip install Pillow")
        self.image = Image.open(file_path)

    def extract_colors(self, num_colors: int = 8) -> List[str]:
        """Extract dominant colors using color quantization."""
        # Resize for performance
        img = self.image.copy()
        img.thumbnail((150, 150))

        # Convert to RGB if necessary
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Quantize to reduce color palette
        img = img.quantize(colors=num_colors)
        palette = img.getpalette()

        # Extract RGB values
        colors = []
        for i in range(num_colors):
            rgb = tuple(palette[i*3:(i+1)*3])
            hex_color = ColorExtractor.rgb_to_hex(rgb)
            colors.append(hex_color)

        return colors


class BrandSystemGenerator:
    """Generate complete brand system from base colors."""

    def __init__(self, colors: List[str], name: str = "MyBrand"):
        self.colors = colors
        self.name = name

    def assign_roles(self) -> Dict[str, str]:
        """Assign semantic roles to colors based on characteristics."""
        color_data = []

        for hex_color in self.colors:
            rgb = ColorExtractor.hex_to_rgb(hex_color)
            h, s, l = ColorExtractor.rgb_to_hsl(rgb)
            color_data.append({
                "hex": hex_color,
                "h": h,
                "s": s,
                "l": l,
                "rgb": rgb
            })

        # Sort by saturation and lightness
        color_data.sort(key=lambda x: (x['s'], -x['l']), reverse=True)

        roles = {}

        # Primary: most saturated
        if len(color_data) >= 1:
            roles["primary"] = color_data[0]["hex"]

        # Secondary: second most saturated with different hue
        if len(color_data) >= 2:
            primary_hue = color_data[0]["h"]
            for color in color_data[1:]:
                if abs(color["h"] - primary_hue) > 30:
                    roles["secondary"] = color["hex"]
                    break
            else:
                roles["secondary"] = color_data[1]["hex"]

        # Accent: high saturation, different hue
        if len(color_data) >= 3:
            for color in color_data:
                if color["hex"] not in roles.values() and color["s"] > 50:
                    roles["accent"] = color["hex"]
                    break

        return roles

    def generate_semantic_colors(self) -> Dict[str, str]:
        """Generate semantic colors (success, warning, error, info)."""
        return {
            "success": "#27AE60",  # Green
            "warning": "#F39C12",  # Orange
            "error": "#E74C3C",    # Red
            "info": "#3498DB"      # Blue
        }

    def generate_text_colors(self, primary_color: str) -> Dict[str, str]:
        """Generate text colors with WCAG compliance."""
        # Check if primary is light or dark
        rgb = ColorExtractor.hex_to_rgb(primary_color)
        luminance = ColorExtractor.calculate_luminance(rgb)

        if luminance > 0.5:
            # Light background
            return {
                "primary": "#2C3E50",
                "secondary": "#7F8C8D",
                "inverse": "#FFFFFF"
            }
        else:
            # Dark background
            return {
                "primary": "#FFFFFF",
                "secondary": "#ECF0F1",
                "inverse": "#2C3E50"
            }

    def generate_system(self) -> Dict[str, Any]:
        """Generate complete design system."""
        roles = self.assign_roles()
        primary = roles.get("primary", self.colors[0])

        # Generate variations for primary
        variations = ColorExtractor.generate_tints_shades(primary)

        system = {
            "name": self.name,
            "colors": {
                **roles,
                "semantic": self.generate_semantic_colors(),
                "text": self.generate_text_colors(primary),
                "background": {
                    "primary": "#FFFFFF",
                    "secondary": "#F8F9FA",
                    "dark": "#2C3E50"
                },
                "variations": variations
            },
            "typography": {
                "heading": {
                    "family": "Inter, system-ui, sans-serif",
                    "weight": 700,
                    "sizes": {"h1": 48, "h2": 36, "h3": 28, "h4": 24, "h5": 20, "h6": 18}
                },
                "body": {
                    "family": "Inter, system-ui, sans-serif",
                    "weight": 400,
                    "sizes": {"large": 18, "medium": 16, "small": 14, "xs": 12}
                },
                "mono": {
                    "family": "Menlo, Monaco, 'Courier New', monospace",
                    "weight": 400
                }
            },
            "spacing": {
                "unit": 8,
                "scale": [4, 8, 12, 16, 24, 32, 48, 64, 96, 128]
            },
            "effects": {
                "shadows": [
                    "0 1px 2px rgba(0,0,0,0.05)",
                    "0 2px 4px rgba(0,0,0,0.1)",
                    "0 4px 8px rgba(0,0,0,0.15)",
                    "0 8px 16px rgba(0,0,0,0.2)"
                ],
                "radius": {"xs": 2, "small": 4, "medium": 8, "large": 16, "xl": 24, "full": 9999}
            }
        }

        return system


def main():
    """CLI interface."""
    if len(sys.argv) < 2:
        print("Usage: brand-parser.py <command> [args]")
        print("\nCommands:")
        print("  colors <hex1> <hex2> ...     Generate system from HEX colors")
        print("  pptx <file> [name]           Extract from PowerPoint")
        print("  image <file> [name]          Extract from image")
        sys.exit(1)

    command = sys.argv[1]

    if command == "colors":
        colors = sys.argv[2:]
        name = "MyBrand"
        generator = BrandSystemGenerator(colors, name)
        system = generator.generate_system()
        print(json.dumps(system, indent=2))

    elif command == "pptx":
        file_path = sys.argv[2]
        name = sys.argv[3] if len(sys.argv) > 3 else Path(file_path).stem
        extractor = PPTXExtractor(file_path)
        colors = extractor.extract_colors()
        fonts = extractor.extract_fonts()

        generator = BrandSystemGenerator(colors, name)
        system = generator.generate_system()
        system["typography"]["heading"]["family"] = fonts["primary_font"]
        system["typography"]["body"]["family"] = fonts["primary_font"]

        print(json.dumps(system, indent=2))

    elif command == "image":
        file_path = sys.argv[2]
        name = sys.argv[3] if len(sys.argv) > 3 else Path(file_path).stem
        extractor = ImageExtractor(file_path)
        colors = extractor.extract_colors()

        generator = BrandSystemGenerator(colors, name)
        system = generator.generate_system()
        print(json.dumps(system, indent=2))

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
