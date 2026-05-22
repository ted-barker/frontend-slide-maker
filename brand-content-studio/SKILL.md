# Brand Content Studio

Generate branded content (slides, diagrams, FigJam boards) from your design system.

## Usage

```
/brand-content-studio [content-type] [--brand path/to/brand.json] [--mode batch|iterative]
```

**Examples:**
- `/brand-content-studio` — Interactive mode
- `/brand-content-studio slides --brand my-brand.json` — Generate slides (batch mode)
- `/brand-content-studio slides --brand my-brand.json --mode iterative` — Slide-by-slide generation
- `/brand-content-studio figjam` — Create FigJam-ready board

**Generation Modes:**

| Mode | Description | When to Use |
|------|-------------|-------------|
| **Batch** (default) | Generate all slides in one pass | Quick drafts, familiar content, time-constrained |
| **Iterative** | Generate slides one-by-one with preview after each | Important presentations, complex content, quality > speed |

**Mode Comparison:**
- **Batch**: Fast, efficient, complete deck at once
- **Iterative**: Slower but controlled, review each slide, incremental preview, resume support

## Workflows

### 🚀 Batch Mode (Default - Fast)

Generate complete presentation in a single pass. Best for quick drafts and straightforward content.

#### 1. Brand Setup (First Run or --brand flag)

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
- **resources/iterative-mode.md** — Slide-by-slide generation workflow (detailed implementation)

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

3. **Determine generation mode**
   - Check for `--mode iterative` flag
   - If iterative mode requested → Go to Iterative Workflow (below)
   - If batch mode (default) → Continue to step 4

4. **Content type selection** (batch mode)
   - Load `resources/layout-previews.md`
   - Generate 3 visual previews using AskUserQuestion with preview field:
     - Each preview shows ASCII mockup of layout
     - Include brief description of use case
     - User selects preferred approach

5. **Generate content** (batch mode)
   - Load appropriate template resource:
     - `resources/google-slides-templates.md` for slides
     - `resources/figjam-templates.md` for boards
   - Apply brand tokens to template
   - Generate output in requested format(s)
   - Load `resources/export-handlers.md` for multi-format export

6. **Speaker notes creation** (batch mode, for slide presentations)
   - Load `resources/speaker-notes-workflow.md`
   - Ask user preference: generate notes, provide template, or skip
   - If generating: draft contextual guidance for each slide
   - Show preview of first 2 slides with notes
   - Get feedback and adjust tone/detail
   - Embed notes in HTML (hidden by default, visible in presenter mode)

7. **Output delivery** (batch mode)
   - Primary output: working file (HTML, JSON, etc.)
   - Export options: PPTX, FigJam JSON, PDF
   - Presenter mode instructions (dual-window view, keyboard shortcuts)
   - Provide shareable link if deployed
   - Show next-step suggestions (iterate, export, share)

### Iterative Workflow (--mode iterative)

When `--mode iterative` is specified, load `resources/iterative-mode.md` for detailed implementation guidance.

**High-level flow:**

**Phase 0: Outline Generation**

1. **Check for source content file**:
   - Ask user for markdown file path (e.g., `block1_design_your_survey.md`)
   - Read entire source file
   
2. **Analyze content structure**:
   - Identify main sections (headers with `##`, `###`)
   - Extract key concepts, frameworks, examples
   - Note natural transition points
   - Count approximate slide needs per section
   
3. **Generate slide outline**:
   - Propose slide-by-slide structure with:
     - Slide number
     - Slide type (title, section-divider, content, statement, etc.)
     - Slide title/topic
     - Background color (for dividers)
     - Approximate content from source
   - Follow brand presentation guidelines (one key thing per slide)
   - Include section dividers between major topics
   - Rotate section divider colors per brand palette
   
4. **Show outline to user**:
   ```
   Proposed Slide Outline (35 slides)
   
   1. Title Slide - "Design Your Survey"
   2. Section Divider (Yellow) - "Learning Objectives"
   3. Content - "What Surveys Are Good For"
   4. Content - "What Surveys Can't Do"
   ...
   
   Review this outline. You can:
   - Edit titles or slide types
   - Reorder slides
   - Add/remove slides
   - Change section divider colors
   
   When ready, say "looks good" to begin generating slides.
   ```
   
5. **Save outline**:
   - Write to: `{presentation-name}-outline.md`
   - Include metadata: total slides, estimated duration, source file
   
**Phase 1: Slide-by-Slide Generation**

6. **For each slide in outline**:
   
   a. **Generate slide content**:
      - Extract relevant content from source .md file
      - Create MINIMAL slide text (follow "no busy slides" rule)
      - One statement or max 5 short bullets per slide
      - Use brand colors from JSON
      - Apply appropriate slide layout (title, content, divider, etc.)
   
   b. **Generate speaker notes**:
      - Load `resources/speaker-notes-workflow.md`
      - Extract ALL detail from corresponding source section
      - Write comprehensive teaching script (3-6 paragraphs)
      - Include examples, citations, facilitation guidance
      - Follow speaker notes principles (context, teaching content, transitions)
   
   c. **Append to markdown file**:
      - Append slide to `{presentation-name}-slides.md`
      - Format: Slide number, type, content HTML, speaker notes
      - Use `---` separator between slides
   
   d. **Update HTML file**:
      - Read all slides from markdown file
      - Parse and generate HTML structure
      - Include navigation, presenter mode, slide counter
      - Write/overwrite `{presentation-name}-presentation.html`
   
   e. **Show progress**:
      ```
      ✓ Slide 3/35 complete: "What Surveys Can't Do"
      
      Slide content: Statement slide with 3 key limitations
      Speaker notes: 4 paragraphs with examples from source
      
      Files updated:
      - design-your-survey-slides.md (appended)
      - design-your-survey-presentation.html (regenerated)
      
      Open HTML in browser to preview.
      
      Options: "next" | "change X" | "edit notes" | "skip" | "stop"
      ```
   
   f. **Wait for user input**:
      - `"next"` / `"continue"` / `"looks good"` → Generate next slide
      - `"change [description]"` → Regenerate current slide with changes
      - `"edit notes"` → Regenerate only speaker notes
      - `"skip"` → Add placeholder slide, continue
      - `"stop"` / `"pause"` → Save progress, exit
      - `"show outline"` → Display full outline
      - `"jump to N"` → Jump to slide N
   
7. **Resume support**:
   - If markdown file exists: "Found 12 completed slides. Resume from Slide 13?"
   - Parse markdown to find last completed slide
   - Continue from that position
   
8. **Completion**:
   - When all slides complete, show summary
   - Provide final HTML file with all slides
   - Offer export options (PDF, PPTX)
   - Show presenter mode instructions

### 🎯 Iterative Mode (Controlled - Quality)

For presentations where you want to review and refine each slide before moving to the next. Best for important decks and complex content.

### Step 0: Generate Outline

1. **Read source content** (markdown file with narrative)
2. **Analyze structure**: Identify main sections, key concepts, natural breaks
3. **Propose slide outline**: List of slides with types and titles
4. **Show outline** to user with slide count, types, section dividers
5. **User reviews**: Edit titles, reorder, add/remove slides
6. **Save outline** to `{presentation-name}-outline.md`

**Example outline:**
```markdown
# Design Your Survey - Slide Outline

Total: 35 slides | Duration: ~80 minutes

1. Title Slide - "Design Your Survey"
2. Section Divider (Yellow) - "Learning Objectives"
3. Content - "What Surveys Are Good For"
4. Content - "What Surveys Can't Do"
5. Section Divider (Blue) - "Sampling"
6. Statement - "Probabilistic Sampling Is Required"
7. Content - "Three Sampling Approaches"
8. Content - "Sample Size Power Calculation"
9. Content - "Statistical Power Requirements"
...
```

### Step 1-N: Generate Each Slide

For each slide in the outline:

1. **Generate slide content** (minimal text, following Wise presentation guidelines)
2. **Generate speaker notes** (comprehensive, extracted from source .md)
3. **Append to markdown** file: `{presentation-name}-slides.md`
4. **Update HTML file**: `{presentation-name}-presentation.html`
5. **Show progress**: "Slide 3/35 complete. Open HTML to preview."
6. **Wait for user feedback**:
   - "looks good" / "next" / "continue" → Move to next slide
   - "change X" → Regenerate current slide with changes
   - "skip" → Add placeholder, move to next
   - "stop" → Save progress, can resume later

### Markdown Format (Appended Incrementally)

```markdown
# Presentation Title - Slides

## Slide 1: Title Slide

**Type:** title-slide
**Background:** #163300 (Forest Green)
**Layout:** 60/40 split

**Slide Content:**
```html
<h1>Design Your Survey</h1>
<p class="subtitle">Survey Science Workshop - Block 1</p>
```

**Speaker Notes:**
Welcome to Block 1 of the Survey Science workshop. This 80-minute session 
focuses on foundational decisions: sampling, question construction, and 
cognitive fatigue management. The goal is to help you avoid the most common 
failure modes in survey design...

---

## Slide 2: Section Divider

**Type:** section-divider
**Background:** #FFEB69 (Bright Yellow)

**Slide Content:**
```html
<h2>LEARNING OBJECTIVES</h2>
```

**Speaker Notes:**
Transition to objectives (2 minutes). By the end of this session, participants 
will understand probabilistic sampling requirements, the BRUSO model for 
question construction...

---

[Continue for each slide...]
```

### HTML Incremental Update

After each slide is appended to the .md file:

1. **Parse markdown** to extract all completed slides
2. **Generate HTML** with:
   - All completed slides (fully rendered)
   - Navigation working for completed slides only
   - Presenter mode with notes
   - Slide counter shows: "3 of 35 (8% complete)"
3. **Write/overwrite** `{presentation-name}-presentation.html`
4. **User can open HTML** in browser to preview current state

### Resume from Progress

If the user stops and wants to continue later:

1. **Read markdown file**: `{presentation-name}-slides.md`
2. **Count completed slides**: Parse markdown to find last `## Slide N:`
3. **Read outline**: `{presentation-name}-outline.md`
4. **Ask user**: "Found 12 completed slides. Resume from Slide 13?"
5. **Continue from last position**

### Commands During Iteration

- `"next"` / `"continue"` / `"looks good"` → Generate next slide
- `"change [description]"` → Regenerate current slide with changes
- `"edit notes"` → Regenerate only speaker notes for current slide
- `"skip"` → Add placeholder, move to next slide
- `"jump to slide N"` → Jump to specific slide number
- `"show outline"` → Display full outline again
- `"regenerate HTML"` → Rebuild HTML from current .md file
- `"stop"` / `"pause"` → Save progress, exit iterative mode

### Benefits of Iterative Mode

✅ **Incremental progress** - Save work as you go  
✅ **Preview anytime** - Open HTML after each slide  
✅ **Easy editing** - Edit .md file directly if needed  
✅ **Version control** - Markdown is git-friendly  
✅ **Resume later** - Continue from any slide  
✅ **Regenerate** - HTML can be rebuilt from .md anytime  
✅ **Learning loop** - Each slide improves based on feedback  
✅ **Fine-grained control** - Review every slide before finalizing

## Best Practices

- **Single source of truth**: Brand assets live in one JSON, referenced everywhere
- **Visual-first**: Show layout options, don't make users describe them
- **Format-agnostic core**: Separate brand logic from output format
- **Incremental enhancement**: Start with basic brand (colors only), expand later
- **Validation**: Check color contrast ratios for accessibility
- **Versioning**: Save brand assets with timestamps for rollback
- **Iterative mode**: Use for important presentations where quality > speed

## Notes

- Google Slides: Generate HTML preview, provide conversion to PPTX via LibreOffice
- FigJam: Export as FigJam-compatible JSON structure
- Brand files persist across sessions in memory directory
- Support multiple brands for users with multiple clients/projects
