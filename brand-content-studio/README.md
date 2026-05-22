# Brand Content Studio

**A Claude Code skill for generating branded presentations, diagrams, and collaboration boards.**

## 🎯 What It Does

Turn your brand assets into beautiful, on-brand content:

- **Upload HEX colors** → Full design system with complementary palettes
- **Parse existing slides** → Extract colors, fonts, spacing from PPTX/screenshots
- **Generate content** → Google Slides, FigJam boards, HTML presentations
- **Visual-first workflow** → See layout previews before generating

## ⚡ Quick Start

```bash
# Interactive mode (recommended first time)
/brand-content-studio

# Generate all slides at once (batch mode)
/brand-content-studio slides --brand my-company.json

# Generate slides one-by-one with preview (iterative mode)
/brand-content-studio slides --brand my-company.json --mode iterative

# Create FigJam board
/brand-content-studio figjam --brand startup-x.json
```

## 📋 Features

### Generation Modes

**Batch Mode (Default):**
- Generate all slides at once
- Fast, efficient for straightforward content
- Get complete presentation in one pass

**Iterative Mode (New!):**
- Generate slides one-by-one
- Review and refine each slide before moving to next
- Preview HTML after each slide
- Progress saved incrementally to markdown
- Resume from any point
- Perfect for important presentations where quality > speed

### Brand Asset Management

**From HEX Colors:**
```
/brand-content-studio
> Enter HEX colors: #FF5733 #3498DB #2ECC71
```

Generates complete design system:
- Primary/secondary/accent colors
- Semantic colors (success, warning, error)
- WCAG-compliant text colors
- Tint/shade variations
- Spacing scale
- Typography styles

**From Existing Slides:**
```
Upload PPTX or screenshot → Extract:
- Color palette
- Font families and sizes
- Layout patterns
- Component styles
```

**From Style Guides:**
```
Upload brand PDF/images → Parse and structure:
- Logo usage
- Color specifications
- Typography system
- Spacing rules
```

### Content Types

**Google Slides Presentations:**
- Corporate Deck (professional, balanced)
- Creative Pitch (bold, dynamic)
- Data Presentation (metrics-focused)

**FigJam Boards:**
- Brainstorm Board (ideas, questions, actions)
- Process Flow (step-by-step workflows)
- Workshop Template (timed activities, voting)

**Output Formats:**
- HTML (immediate preview)
- PPTX (PowerPoint export)
- FigJam JSON (direct import)
- PDF (print-ready)

## 🎨 Visual Preview Selection

Instead of describing what you want, **see it first**:

```
Which layout fits your content?

[ ] Corporate Deck          [ ] Creative Pitch         [ ] Data Presentation
┌─────────────────┐        ┌─────────────────┐        ┌─────────────────┐
│  [LOGO]         │        │ [LOGO]          │        │  Key Metrics    │
│                 │        │                 │        │  ══════════     │
│  ████ Title     │        │  ╔═══════════╗  │        │  ┌───────────┐  │
│    Subtitle     │        │  ║ BOLD      ║  │        │  │  ▄▄▄      │  │
│                 │        │  ║ STATEMENT ║  │        │  │ █   █     │  │
│  ┌────┐ ┌────┐  │        │  ╚═══════════╝  │        │  └───────────┘  │
│  │ IMG│ │ IMG│  │        │                 │        │  45%    $2.3M   │
│  └────┘ └────┘  │        │  Supporting...  │        │  ┌──────────┐   │
│                 │        │                 │        │  • Insights   │  │
└─────────────────┘        └─────────────────┘        └─────────────────┘
Professional               Story-driven               Chart-focused
```

## 🏗️ Architecture

Progressive disclosure pattern (inspired by [frontend-slides](https://github.com/zarazhangrui/frontend-slides)):

```
SKILL.md (core workflow)
├── resources/
│   ├── brand-parser.py          # Extract design tokens
│   ├── color-system.md          # Palette generation
│   ├── layout-previews.md       # Visual preview templates
│   ├── google-slides-templates.md
│   └── figjam-templates.md
```

Resources load on-demand, keeping the skill lightweight and fast.

## 📦 Brand Asset Storage

Brand files save to `~/.claude/memory/brands/` for reuse across sessions:

```json
{
  "name": "MyCompany",
  "colors": {
    "primary": "#FF5733",
    "secondary": "#3498DB",
    "accent": "#F39C12",
    "semantic": {...},
    "text": {...},
    "variations": {
      "tints": ["#FF7A59", "#FF9D7F", ...],
      "shades": ["#CC4629", "#99341F", ...]
    }
  },
  "typography": {
    "heading": {"family": "Inter", "weight": 700, "sizes": {...}},
    "body": {"family": "Inter", "weight": 400, "sizes": {...}}
  },
  "spacing": {"unit": 8, "scale": [4, 8, 16, 24, ...]},
  "effects": {"shadows": [...], "radius": {...}}
}
```

## 🔧 Setup

### Python Dependencies (Optional)

For brand extraction features:

```bash
# Extract from PowerPoint
pip install python-pptx

# Extract from images
pip install Pillow

# Convert to PPTX
brew install wkhtmltopdf libreoffice  # macOS
```

Not required for basic usage (HEX input + HTML output).

## 📖 Usage Examples

### Example 1: First-Time User

```bash
/brand-content-studio

> No brand assets found. Let's create your brand system.
> How do you want to provide brand colors?

[ ] Enter HEX codes
[ ] Upload existing slides (PPTX)
[ ] Upload style guide (PDF/images)

> Selected: Enter HEX codes
> Enter your primary colors (space-separated): #FF5733 #3498DB

✓ Generated complete design system
✓ Saved to ~/.claude/memory/brands/mycompany.json

> What type of content do you want to create?

[ ] Google Slides presentation
[ ] FigJam board

> Selected: Google Slides presentation
> [Shows 3 layout previews]

> Selected: Corporate Deck
> What's the presentation about? Product roadmap Q2 2026

[Generates branded slides with your content]

✓ Created: mycompany-roadmap.html
✓ View in browser: open mycompany-roadmap.html
✓ Export to PPTX: wkhtmltopdf + libreoffice (instructions provided)
```

### Example 2: Returning User

```bash
/brand-content-studio figjam --brand acme-corp.json

✓ Loaded brand: ACME Corp
> What's the board for? Sprint planning workshop

[Shows FigJam layout previews]

> Selected: Workshop Template

✓ Created: acme-sprint-planning.figjam
✓ HTML preview: acme-sprint-planning.html
✓ Import to FigJam: File → Import → Select .figjam file
```

### Example 3: Extract from Existing Slides

```bash
/brand-content-studio

> Drag and drop your PowerPoint file...
> Uploaded: company-template.pptx

✓ Extracted colors: #1E3A8A, #3B82F6, #10B981
✓ Extracted fonts: Roboto, Open Sans
✓ Generated design system
✓ Saved to ~/.claude/memory/brands/company-template.json

> Create new content or refine brand system?
```

### Example 4: Iterative Slide Generation

```bash
/brand-content-studio slides --brand wise.json --mode iterative

> Source content file? block1_design_your_survey.md

✓ Read source file (45,892 bytes)
✓ Analyzed structure: 6 main sections

Proposed Slide Outline (35 slides):
1. Title - "Design Your Survey"
2. Divider (Yellow) - "Learning Objectives"
3. Content - "What Surveys Are Good For"
...
35. Closing - "Questions?"

> Review outline. Say "looks good" to begin.

User: looks good

✓ Outline saved to: design-your-survey-outline.md

Generating Slide 1/35...

✓ Slide 1 complete: "Design Your Survey" (Title)
  Slide content: Title + subtitle
  Speaker notes: 3 paragraphs (welcome, session overview, objectives)

Files updated:
• design-your-survey-slides.md (created)
• design-your-survey-presentation.html (created)

Preview: Open design-your-survey-presentation.html in browser

Continue? ("next" to generate Slide 2)

User: next

Generating Slide 2/35...

✓ Slide 2 complete: "Learning Objectives" (Section Divider)
  ...

[Process continues through all 35 slides]
```

## 🎓 Best Practices

### Brand Management

- **Start simple**: Begin with 2-3 HEX colors, expand later
- **One brand per client**: Create separate brand files for each project
- **Version control**: Brand files are timestamped for rollback
- **Validate contrast**: Tool automatically checks WCAG compliance

### Content Creation

- **Preview first**: Always review layout options before generating
- **Iterate locally**: HTML output allows quick browser preview
- **Export last**: Generate HTML first, export to PPTX/FigJam when finalized
- **Test early**: View slides at actual presentation size (full screen)

### Collaboration

- **Share brand files**: Send `.json` files to teammates
- **Export for review**: HTML works everywhere, no special software needed
- **Convert on demand**: Keep source as HTML, convert to PPTX for stakeholders

## 🔍 Advanced Usage

### Custom Color Roles

Manually edit brand JSON to assign specific roles:

```json
{
  "colors": {
    "primary": "#FF5733",    // Main brand color
    "secondary": "#3498DB",  // Supporting color
    "accent": "#F39C12",     // Call-to-action
    "custom": {
      "feature": "#9B59B6",  // Feature highlights
      "premium": "#F1C40F"   // Premium tier
    }
  }
}
```

### Typography Customization

```json
{
  "typography": {
    "heading": {
      "family": "Playfair Display, serif",
      "weight": 700
    },
    "body": {
      "family": "Source Sans Pro, sans-serif",
      "weight": 400
    },
    "code": {
      "family": "Fira Code, monospace",
      "weight": 400
    }
  }
}
```

### Layout Overrides

Pass custom layout parameters:

```bash
/brand-content-studio slides --brand myco.json --layout two-column --density minimal
```

## 🤝 Integration with Other Tools

### Figma

1. Generate FigJam board
2. Import to Figma via FigJam integration
3. Convert FigJam nodes to Figma frames

### Google Slides

1. Export HTML to PDF
2. Import PDF to Google Slides
3. Each page becomes a slide

### Notion

1. Generate HTML presentation
2. Embed HTML in Notion page
3. Or export PDF and upload to Notion

## 📐 Design System Philosophy

This skill follows **token-based design**:

- **Single source of truth**: Brand JSON defines all values
- **Semantic naming**: Colors named by purpose, not appearance
- **Scalable**: Add new formats without redefining tokens
- **Accessible**: WCAG contrast validation built-in

## 🚀 Roadmap

Planned features:

- [ ] Animation presets for slide transitions
- [ ] Chart generation from CSV data
- [ ] Miro board export
- [ ] Canva template generation
- [ ] Brand compliance checker
- [ ] Multi-language support
- [ ] Real-time collaboration (multi-user editing)

## 📝 License

MIT

## 🙏 Credits

Inspired by [frontend-slides](https://github.com/zarazhangrui/frontend-slides) by [@zarazhangrui](https://github.com/zarazhangrui) — the progressive disclosure architecture and visual preview pattern are brilliant.

## 💬 Feedback

Issues and feature requests: [Create an issue](https://github.com/your-repo/brand-content-studio/issues)
