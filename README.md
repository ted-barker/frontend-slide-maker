# Frontend Slide Maker

Generate beautiful, branded HTML presentations using AI and design system tokens. No PowerPoint, no Google Slides account needed - just open in a browser and present.

## 🎯 What It Does

Turn brand assets + content into ready-to-present HTML slides:
- **Input:** Brand colors + your content
- **Output:** Self-contained HTML presentation file
- **Workflow:** Claude Code + Brand Content Studio skill

## 🚀 Quick Start

**View the example presentation:**
1. Open `presentation.html` in any browser
2. Navigate with arrow keys or buttons
3. Press F11 (Windows) or Cmd+Ctrl+F (Mac) for fullscreen

**Create your own:**
1. Copy `wise-brand-kit.json` to `~/.claude/memory/brands/your-brand.json`
2. Edit with your brand colors, fonts, spacing
3. Use Claude Code's Brand Content Studio skill:
   ```bash
   /brand-content-studio slides --brand your-brand.json
   ```

## 📁 What's Included

```
├── presentation.html         # Example: Survey Science workshop
├── wise-brand-kit.json       # Complete design system (Wise)
├── content-outline.md        # Slide content with design notes
├── google-slides-guide.md    # Alt: Google Slides instructions
└── SETUP.md                  # GitHub setup instructions
```

## 📊 Example Content

The included presentation is a workshop on survey methodology:
- What surveys are good for (and not good for)
- Why population thinking matters in tech
- Probabilistic sampling approaches
- Sample size and statistical power
- Operational vs. analytic populations

**Target Audience:** Researchers, data scientists, product teams  
**Duration:** ~30 minutes with discussion

## 🎨 Design System Approach

Uses **token-based design** - all visual properties defined in JSON:

```json
{
  "colors": {
    "primary": "#163300",
    "secondary": "#9FE870",
    "semantic": {...},
    "variations": {...}
  },
  "typography": {
    "heading": {"family": "Inter", "sizes": {...}},
    "body": {...}
  },
  "spacing": {"unit": 8, "scale": [4, 8, 16, 24, ...]},
  "effects": {"shadows": [...], "radius": {...}}
}
```

Benefits:
- Single source of truth for all design decisions
- Easy to rebrand (swap JSON file)
- WCAG AAA accessibility compliance built-in
- Scales to new formats (PDF, PPTX) without code changes

## 🛠️ How It Works

```
Brand Assets (JSON) + Content → Claude Code → HTML Presentation
                                     ↓
                          Brand Content Studio Skill
                                     ↓
                          (Token-based rendering)
```

The skill:
1. Parses brand JSON for colors, fonts, spacing
2. Applies layout patterns (title slides, dividers, content slides)
3. Generates self-contained HTML with embedded styles
4. Validates accessibility (contrast ratios, text sizes)

Inspired by [frontend-slides](https://github.com/zarazhangrui/frontend-slides) architecture.

## 🎨 Wise Brand Example

Included `wise-brand-kit.json` extracted from [wise.design](https://wise.design):
- Forest Green (#163300) + Bright Green (#9FE870) palette
- Inter typography system
- 8px spacing grid
- Section divider layouts
- WCAG AAA compliant

**Note:** Wise brand assets included for educational/reference purposes. For production use of Wise branding, check with Wise's brand team.

## ✏️ Customization

### Update Content
Edit the HTML file directly - slides are in `<div class="slide">` blocks.

### Change Colors
Replace color hex codes in the `<style>` section, or update the brand JSON and regenerate.

### Add Slides
Copy an existing slide block, modify content, update the slide counter.

### Export Formats
- **PDF:** Print from browser (Cmd/Ctrl + P)
- **PowerPoint:** Follow `google-slides-guide.md` instructions
- **Images:** Screenshot individual slides in fullscreen

## 🔧 Requirements

**To present:**
- Any modern web browser
- Internet connection (for font loading on first open)

**To create new presentations:**
- [Claude Code](https://claude.ai/code)
- Brand Content Studio skill

**Optional (for exports):**
- wkhtmltopdf + LibreOffice (HTML → PPTX)
- Chrome headless (HTML → PDF)

## 📖 Usage Examples

### Example 1: Quick Rebrand

```bash
# Copy the example brand kit
cp wise-brand-kit.json ~/.claude/memory/brands/my-startup.json

# Edit colors/fonts in my-startup.json
# Change primary: "#163300" → "#FF6B35" (your brand color)

# Generate new presentation
/brand-content-studio slides --brand my-startup.json
```

### Example 2: Extract from Existing Slides

```bash
# Upload your PowerPoint template
/brand-content-studio

# Skill extracts colors, fonts, spacing
# Generates brand JSON automatically
# Use for new presentations
```

## 🤝 Contributing

This is a private repository for internal use. Share with colleagues who need:
- The presentation for reference
- The brand kit template for their own materials
- The workflow for creating branded presentations

## 🙏 Credits

- **[Wise](https://wise.design)** - Example brand design system
- **[Claude Code](https://claude.ai/code)** - AI coding assistant
- **Brand Content Studio** - Claude Code skill for branded content
- **[frontend-slides](https://github.com/zarazhangrui/frontend-slides)** - Architecture inspiration

## 📄 License

**Code & Templates:** MIT License - free to use, modify, distribute

**Brand Assets:** `wise-brand-kit.json` derived from Wise's design system for educational/reference use. Respect Wise's brand guidelines for commercial use.

---

**Created:** May 2026  
**Tech Stack:** HTML5, CSS3, Vanilla JS, Claude Code, Brand Content Studio skill
