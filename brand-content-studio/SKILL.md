# Brand Content Studio

Generate branded content (slides, diagrams, FigJam boards) from your design system.

## Usage

```
/brand-content-studio [content-type] [--brand path/to/brand.json]
```

**Examples:**
- `/brand-content-studio` — Interactive mode
- `/brand-content-studio slides --brand my-brand.json` — Generate slides with existing brand
- `/brand-content-studio figjam` — Create FigJam-ready board

## Workflow

### 1. Brand Setup (First Run or --brand flag)

If no brand assets exist, I'll help you create them:

**Option A: Upload HEX colors**
- Provide HEX codes (#FF5733, #3498DB, etc.)
- I'll generate a complete design system with:
  - Primary, secondary, accent colors
  - Semantic colors (success, warning, error, info)
  - Text colors with WCAG compliance
  - Tint/shade variations
  - Complementary palette recommendations

**Option B: Extract from existing slides**
- Upload PPTX or screenshot of Google Slides
- I'll extract:
  - Color palette
  - Typography (font families, sizes, weights)
  - Spacing/layout patterns
  - Component styles (headers, cards, buttons)

**Option C: Style guide upload**
- Upload existing brand guidelines (PDF, images)
- I'll parse and structure as reusable design tokens

Extracted brand assets save to `~/.claude/memory/brands/{brand-name}.json`

### 2. Content Type Selection

I'll show you 3 visual layout previews for your chosen format:

**Google Slides**
- Corporate deck
- Creative pitch
- Data presentation

**FigJam**
- Brainstorm board
- Process flow
- Workshop template

**Hybrid Output**
- HTML preview (immediate view)
- Export formats (PPTX, FigJam JSON, PDF)

### 3. Content Generation

You provide:
- Core message/content
- Target audience
- Desired tone

I generate:
- Fully branded output in chosen format
- Alternative layout suggestions
- Export-ready files

## Progressive Disclosure

This skill loads resources on-demand:

- **SKILL.md** (this file) — Core workflow
- **resources/brand-parser.py** — Extract design tokens from uploads
- **resources/color-system.md** — Color theory and palette generation
- **resources/google-slides-templates.md** — Slide layouts
- **resources/figjam-templates.md** — Board templates
- **resources/layout-previews.md** — Visual preview definitions
- **resources/export-handlers.md** — Format conversion utilities
- **resources/speaker-notes-workflow.md** — Speaker notes creation process

## Brand Asset Schema

```json
{
  "name": "MyBrand",
  "colors": {
    "primary": "#FF5733",
    "secondary": "#3498DB",
    "accent": "#F39C12",
    "semantic": {
      "success": "#27AE60",
      "warning": "#F39C12",
      "error": "#E74C3C",
      "info": "#3498DB"
    },
    "text": {
      "primary": "#2C3E50",
      "secondary": "#7F8C8D",
      "inverse": "#FFFFFF"
    },
    "background": {
      "primary": "#FFFFFF",
      "secondary": "#ECF0F1",
      "dark": "#2C3E50"
    }
  },
  "typography": {
    "heading": {
      "family": "Inter",
      "weight": 700,
      "sizes": {"h1": 48, "h2": 36, "h3": 28}
    },
    "body": {
      "family": "Inter",
      "weight": 400,
      "sizes": {"large": 18, "medium": 16, "small": 14}
    }
  },
  "spacing": {
    "unit": 8,
    "scale": [4, 8, 16, 24, 32, 48, 64, 96]
  },
  "effects": {
    "shadows": ["0 2px 4px rgba(0,0,0,0.1)", "0 4px 8px rgba(0,0,0,0.15)"],
    "radius": {"small": 4, "medium": 8, "large": 16}
  }
}
```

## Instructions for Claude

When this skill is invoked:

1. **Check for brand assets**
   ```bash
   BRAND_DIR="$HOME/.claude/memory/brands"
   if [ "$BRAND_FLAG" ]; then
     BRAND_FILE="$BRAND_DIR/$BRAND_FLAG"
   else
     # List available brands or prompt to create
   fi
   ```

2. **If no brand exists**, initiate brand setup:
   - Use AskUserQuestion with preview option to show:
     - Color input method (HEX upload vs extract vs upload guide)
     - Show example outputs for each method
   - Load `resources/brand-parser.py` if extraction needed
   - Load `resources/color-system.md` for palette generation
   - Save structured brand JSON to `$BRAND_DIR/{name}.json`

3. **Content type selection**
   - Load `resources/layout-previews.md`
   - Generate 3 visual previews using AskUserQuestion with preview field:
     - Each preview shows ASCII mockup of layout
     - Include brief description of use case
     - User selects preferred approach

4. **Generate content**
   - Load appropriate template resource:
     - `resources/google-slides-templates.md` for slides
     - `resources/figjam-templates.md` for boards
   - Apply brand tokens to template
   - Generate output in requested format(s)
   - Load `resources/export-handlers.md` for multi-format export

5. **Speaker notes creation** (for slide presentations)
   - Load `resources/speaker-notes-workflow.md`
   - Ask user preference: generate notes, provide template, or skip
   - If generating: draft contextual guidance for each slide
   - Show preview of first 2 slides with notes
   - Get feedback and adjust tone/detail
   - Embed notes in HTML (hidden by default, visible in presenter mode)

6. **Output delivery**
   - Primary output: working file (HTML, JSON, etc.)
   - Export options: PPTX, FigJam JSON, PDF
   - Presenter mode instructions (dual-window view, keyboard shortcuts)
   - Provide shareable link if deployed
   - Show next-step suggestions (iterate, export, share)

## Best Practices

- **Single source of truth**: Brand assets live in one JSON, referenced everywhere
- **Visual-first**: Show layout options, don't make users describe them
- **Format-agnostic core**: Separate brand logic from output format
- **Incremental enhancement**: Start with basic brand (colors only), expand later
- **Validation**: Check color contrast ratios for accessibility
- **Versioning**: Save brand assets with timestamps for rollback

## Notes

- Google Slides: Generate HTML preview, provide conversion to PPTX via LibreOffice
- FigJam: Export as FigJam-compatible JSON structure
- Brand files persist across sessions in memory directory
- Support multiple brands for users with multiple clients/projects
