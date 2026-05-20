#!/bin/bash
# Brand Content Studio - Installation Script
# Sets up directories and optional dependencies

set -e

echo "🎨 Brand Content Studio - Setup"
echo "================================"
echo ""

# Create brand storage directory
BRAND_DIR="$HOME/.claude/memory/brands"
echo "📁 Creating brand storage directory..."
mkdir -p "$BRAND_DIR"
echo "✓ Created: $BRAND_DIR"
echo ""

# Check Python
echo "🐍 Checking Python installation..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo "✓ Found: $PYTHON_VERSION"
else
    echo "⚠️  Python 3 not found (optional for brand extraction)"
fi
echo ""

# Check for optional dependencies
echo "📦 Checking optional dependencies..."
echo ""

# python-pptx
echo "Checking python-pptx (for PowerPoint extraction)..."
if python3 -c "import pptx" 2>/dev/null; then
    echo "✓ python-pptx installed"
else
    echo "✗ python-pptx not installed"
    echo "  Install with: pip3 install python-pptx"
fi
echo ""

# Pillow
echo "Checking Pillow (for image extraction)..."
if python3 -c "import PIL" 2>/dev/null; then
    echo "✓ Pillow installed"
else
    echo "✗ Pillow not installed"
    echo "  Install with: pip3 install Pillow"
fi
echo ""

# wkhtmltopdf
echo "Checking wkhtmltopdf (for PDF export)..."
if command -v wkhtmltopdf &> /dev/null; then
    echo "✓ wkhtmltopdf installed"
else
    echo "✗ wkhtmltopdf not installed"
    echo "  Install with: brew install wkhtmltopdf (macOS)"
    echo "              : apt install wkhtmltopdf (Linux)"
fi
echo ""

# LibreOffice
echo "Checking LibreOffice (for PPTX conversion)..."
if command -v libreoffice &> /dev/null; then
    echo "✓ LibreOffice installed"
else
    echo "✗ LibreOffice not installed"
    echo "  Install with: brew install libreoffice (macOS)"
    echo "              : apt install libreoffice (Linux)"
fi
echo ""

# Create example brand
EXAMPLE_BRAND="$BRAND_DIR/example-techcorp.json"
if [ ! -f "$EXAMPLE_BRAND" ]; then
    echo "📝 Creating example brand file..."
    cp examples/example-brand.json "$EXAMPLE_BRAND"
    echo "✓ Created: $EXAMPLE_BRAND"
else
    echo "✓ Example brand already exists"
fi
echo ""

# Summary
echo "================================"
echo "✨ Setup complete!"
echo ""
echo "📍 Brand files will be saved to:"
echo "   $BRAND_DIR"
echo ""
echo "🚀 Get started:"
echo "   /brand-content-studio"
echo ""
echo "📖 Documentation:"
echo "   README.md in this directory"
echo ""

# Check feature availability
echo "Feature availability:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

FEATURES=()

# Core features (always available)
FEATURES+=("✓ HEX color input")
FEATURES+=("✓ Manual brand creation")
FEATURES+=("✓ HTML slide generation")
FEATURES+=("✓ FigJam JSON export")

# Optional features
if python3 -c "import pptx" 2>/dev/null; then
    FEATURES+=("✓ PowerPoint extraction")
else
    FEATURES+=("⚠️  PowerPoint extraction (install python-pptx)")
fi

if python3 -c "import PIL" 2>/dev/null; then
    FEATURES+=("✓ Image color extraction")
else
    FEATURES+=("⚠️  Image color extraction (install Pillow)")
fi

if command -v wkhtmltopdf &> /dev/null; then
    FEATURES+=("✓ PDF export")
else
    FEATURES+=("⚠️  PDF export (install wkhtmltopdf)")
fi

if command -v libreoffice &> /dev/null; then
    FEATURES+=("✓ PPTX conversion")
else
    FEATURES+=("⚠️  PPTX conversion (install LibreOffice)")
fi

for feature in "${FEATURES[@]}"; do
    echo "  $feature"
done

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Optional: Install all dependencies
echo "💡 Install all optional dependencies?"
echo "   This will run: pip3 install python-pptx Pillow"
echo ""
read -p "Install? (y/N): " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "📦 Installing Python packages..."
    pip3 install python-pptx Pillow
    echo "✓ Python packages installed"
    echo ""

    if [[ "$OSTYPE" == "darwin"* ]]; then
        echo "📦 Installing system packages (macOS)..."
        if command -v brew &> /dev/null; then
            brew install wkhtmltopdf libreoffice
            echo "✓ System packages installed"
        else
            echo "⚠️  Homebrew not found. Install manually:"
            echo "   brew install wkhtmltopdf libreoffice"
        fi
    else
        echo "💡 Install system packages manually:"
        echo "   Linux: sudo apt install wkhtmltopdf libreoffice"
    fi
fi

echo ""
echo "🎉 Ready to create branded content!"
echo ""
