# Color System Generation

Algorithms for generating complete color systems from base colors.

## Color Theory Fundamentals

### HSL Color Space

Best for generating variations:
- **Hue (H)**: 0-360° on color wheel
- **Saturation (S)**: 0-100% (gray to pure color)
- **Lightness (L)**: 0-100% (black to white)

### RGB Color Space

Standard for digital display:
- **Red (R)**: 0-255
- **Green (G)**: 0-255
- **Blue (B)**: 0-255

## Palette Generation Strategies

### 1. Complementary Colors

Opposite on color wheel (180° apart):

```
Primary: H=0 (red)
Complementary: H=180 (cyan)
```

High contrast, vibrant. Use for call-to-action buttons.

### 2. Analogous Colors

Adjacent on color wheel (30° apart):

```
Primary: H=200 (blue)
Analogous 1: H=170 (teal)
Analogous 2: H=230 (purple-blue)
```

Harmonious, cohesive. Use for subtle differentiation.

### 3. Triadic Colors

Evenly spaced (120° apart):

```
Primary: H=0 (red)
Triadic 1: H=120 (green)
Triadic 2: H=240 (blue)
```

Balanced, dynamic. Use for multi-category data.

### 4. Split-Complementary

Complementary + two adjacent (150° and 210°):

```
Primary: H=0 (red)
Split 1: H=150 (teal)
Split 2: H=210 (blue)
```

Less jarring than complementary, still high contrast.

## Tint and Shade Generation

### Tints (Lighter)

Increase lightness toward 100%:

```python
def generate_tints(hex_color, steps=5):
    h, s, l = hex_to_hsl(hex_color)
    tints = []
    for i in range(1, steps + 1):
        new_l = l + (100 - l) * (i / (steps + 1))
        tints.append(hsl_to_hex(h, s, new_l))
    return tints

# Example: #FF5733 (L=60)
# Tints: L=70, L=78, L=84, L=90, L=95
```

### Shades (Darker)

Decrease lightness toward 0%:

```python
def generate_shades(hex_color, steps=5):
    h, s, l = hex_to_hsl(hex_color)
    shades = []
    for i in range(1, steps + 1):
        new_l = l * (1 - i / (steps + 1))
        shades.append(hsl_to_hex(h, s, new_l))
    return shades

# Example: #FF5733 (L=60)
# Shades: L=50, L=40, L=30, L=20, L=10
```

### Tones (Desaturated)

Decrease saturation toward 0%:

```python
def generate_tones(hex_color, steps=5):
    h, s, l = hex_to_hsl(hex_color)
    tones = []
    for i in range(1, steps + 1):
        new_s = s * (1 - i / (steps + 1))
        tones.append(hsl_to_hex(h, new_s, l))
    return tones
```

## Semantic Color Assignment

### Auto-Assign Roles

Based on color characteristics:

```python
def assign_color_roles(hex_colors):
    colors = []
    for hex in hex_colors:
        h, s, l = hex_to_hsl(hex)
        colors.append({
            'hex': hex,
            'hue': h,
            'saturation': s,
            'lightness': l
        })
    
    # Sort by saturation (most saturated = primary)
    colors.sort(key=lambda c: c['saturation'], reverse=True)
    
    roles = {}
    roles['primary'] = colors[0]['hex']
    
    # Secondary: different hue, high saturation
    for color in colors[1:]:
        if abs(color['hue'] - colors[0]['hue']) > 30:
            roles['secondary'] = color['hex']
            break
    
    # Accent: complementary or split-complementary
    primary_hue = colors[0]['hue']
    target_hue = (primary_hue + 180) % 360
    
    closest = min(colors, key=lambda c: 
        min(abs(c['hue'] - target_hue), 
            abs(c['hue'] - target_hue + 360),
            abs(c['hue'] - target_hue - 360)))
    
    roles['accent'] = closest['hex']
    
    return roles
```

### Semantic Color Defaults

When specific semantic colors aren't provided:

```python
SEMANTIC_DEFAULTS = {
    'success': {
        'hue': 140,  # Green
        'saturation': 60,
        'lightness': 45
    },
    'warning': {
        'hue': 38,   # Orange
        'saturation': 90,
        'lightness': 55
    },
    'error': {
        'hue': 4,    # Red
        'saturation': 78,
        'lightness': 58
    },
    'info': {
        'hue': 207,  # Blue
        'saturation': 73,
        'lightness': 54
    }
}
```

Adjust saturation and lightness to match brand:

```python
def adjust_semantic_to_brand(brand_primary):
    h, s, l = hex_to_hsl(brand_primary)
    
    # Match saturation and lightness levels
    semantic = {}
    for role, defaults in SEMANTIC_DEFAULTS.items():
        adjusted_s = min(s + 10, 90)  # Similar saturation
        adjusted_l = defaults['lightness']
        
        semantic[role] = hsl_to_hex(
            defaults['hue'],
            adjusted_s,
            adjusted_l
        )
    
    return semantic
```

## Text Color Generation

### WCAG Contrast Requirements

- **AA Level**: 4.5:1 for normal text, 3:1 for large text
- **AAA Level**: 7:1 for normal text, 4.5:1 for large text

### Calculate Contrast Ratio

```python
def calculate_luminance(rgb):
    def adjust(c):
        c = c / 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    
    r, g, b = [adjust(c) for c in rgb]
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def contrast_ratio(rgb1, rgb2):
    l1 = calculate_luminance(rgb1)
    l2 = calculate_luminance(rgb2)
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)

# Example
bg = hex_to_rgb('#FFFFFF')
text = hex_to_rgb('#2C3E50')
ratio = contrast_ratio(bg, text)  # 12.6:1 (AAA)
```

### Auto-Generate Text Colors

```python
def generate_text_colors(background_hex):
    bg_rgb = hex_to_rgb(background_hex)
    bg_luminance = calculate_luminance(bg_rgb)
    
    if bg_luminance > 0.5:  # Light background
        return {
            'primary': '#2C3E50',    # Dark text (12.6:1)
            'secondary': '#7F8C8D',  # Medium gray (4.8:1)
            'tertiary': '#BDC3C7',   # Light gray (2.3:1)
            'inverse': '#FFFFFF'
        }
    else:  # Dark background
        return {
            'primary': '#FFFFFF',    # White text
            'secondary': '#ECF0F1',  # Off-white
            'tertiary': '#95A5A6',   # Medium gray
            'inverse': '#2C3E50'
        }
```

## Color Harmony Validation

### Check Color Distance

Ensure colors are distinguishable:

```python
def color_distance(hex1, hex2):
    """Euclidean distance in RGB space"""
    rgb1 = hex_to_rgb(hex1)
    rgb2 = hex_to_rgb(hex2)
    
    return ((rgb1[0] - rgb2[0])**2 + 
            (rgb1[1] - rgb2[1])**2 + 
            (rgb1[2] - rgb2[2])**2) ** 0.5

# Minimum distance: 50 (0-441 scale)
if color_distance('#FF5733', '#FF6644') < 50:
    print("Colors too similar!")
```

### Validate Palette

```python
def validate_palette(colors):
    issues = []
    
    # Check for sufficient contrast between roles
    if contrast_ratio(
        hex_to_rgb(colors['primary']),
        hex_to_rgb(colors['background'])
    ) < 3.0:
        issues.append("Primary color has poor contrast with background")
    
    # Check for color blindness
    # (deuteranopia simulation)
    
    # Check for sufficient variety
    hues = [hex_to_hsl(c)[0] for c in colors.values()]
    if max(hues) - min(hues) < 30:
        issues.append("Color palette lacks hue variety")
    
    return issues
```

## Advanced Techniques

### Perceptual Lightness Steps

Human perception is non-linear. Use perceptual lightness (L*) from LAB color space:

```python
def perceptual_lightness_scale(hex_color, steps=9):
    """Generate perceptually uniform lightness steps"""
    # Convert to LAB color space
    lab = rgb_to_lab(hex_to_rgb(hex_color))
    
    # Generate steps from L*=10 to L*=90
    scale = []
    for i in range(steps):
        new_l = 10 + (80 * i / (steps - 1))
        new_lab = (new_l, lab[1], lab[2])
        scale.append(lab_to_hex(new_lab))
    
    return scale
```

### Color Temperature

Adjust warmth/coolness:

```python
def adjust_temperature(hex_color, delta):
    """
    delta > 0: warmer (more red/orange)
    delta < 0: cooler (more blue)
    """
    h, s, l = hex_to_hsl(hex_color)
    
    if delta > 0:
        # Shift toward red (0°) or orange (30°)
        if h > 180:
            new_h = h - abs(delta)
        else:
            new_h = h + abs(delta)
    else:
        # Shift toward blue (210-240°)
        target = 220
        new_h = h + (target - h) * abs(delta) / 100
    
    return hsl_to_hex(new_h % 360, s, l)
```

## Color Naming

Generate semantic names for palette colors:

```python
HUE_NAMES = {
    (0, 15): "red",
    (15, 45): "orange",
    (45, 65): "yellow",
    (65, 150): "green",
    (150, 190): "cyan",
    (190, 260): "blue",
    (260, 290): "purple",
    (290, 330): "magenta",
    (330, 360): "red"
}

def name_color(hex_color):
    h, s, l = hex_to_hsl(hex_color)
    
    # Get hue name
    hue_name = next(name for (start, end), name in HUE_NAMES.items() 
                    if start <= h < end)
    
    # Add lightness modifier
    if l < 20:
        modifier = "very-dark"
    elif l < 40:
        modifier = "dark"
    elif l < 60:
        modifier = ""
    elif l < 80:
        modifier = "light"
    else:
        modifier = "very-light"
    
    # Add saturation modifier
    if s < 20:
        sat_mod = "gray"
    elif s < 40:
        sat_mod = "muted"
    else:
        sat_mod = ""
    
    parts = [p for p in [modifier, sat_mod, hue_name] if p]
    return "-".join(parts)

# Examples:
# #FF5733 → "red"
# #FFB3A6 → "light-red"
# #8C5C4F → "muted-red"
```

## Usage in Skill

When user provides HEX colors:

1. **Analyze** input colors (hue, saturation, lightness)
2. **Assign roles** (primary, secondary, accent)
3. **Generate variations** (tints, shades for each role)
4. **Create semantic colors** (success, warning, error, info)
5. **Generate text colors** with WCAG validation
6. **Add complementary colors** if palette is monochromatic
7. **Validate** entire system for contrast and harmony
8. **Save** as structured brand JSON

This ensures even minimal input (1-2 colors) produces a complete, accessible design system.
