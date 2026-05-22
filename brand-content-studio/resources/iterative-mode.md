# Iterative Mode - Slide-by-Slide Generation

Detailed implementation guide for iterative presentation generation.

## Overview

Iterative mode generates presentations one slide at a time, allowing review and refinement after each slide before moving to the next. Progress is saved incrementally to markdown and HTML files.

## File Structure

```
project/
├── {name}-outline.md           # Slide outline (generated first)
├── {name}-slides.md            # Slides appended incrementally
└── {name}-presentation.html    # HTML regenerated after each slide
```

## Phase 0: Outline Generation

### Input Analysis

When user provides source content file (e.g., `block1_design_your_survey.md`):

1. **Read entire file**
2. **Identify structure**:
   - Main sections (## headers)
   - Subsections (### headers)
   - Key concepts (bold text, lists)
   - Examples (italics, indented text)
   - Natural breaks (horizontal rules, section transitions)

3. **Count content density**:
   - Paragraphs per section
   - Complexity indicators (tables, formulas, multi-step processes)
   - Estimate slides needed (1 slide per key concept, not per paragraph)

### Outline Generation Rules

**Slide Types:**
- **Title Slide**: Opening slide with presentation title
- **Section Divider**: Full-screen colored background, section name
- **Content Slide**: Left content, right visual (60/40 split)
- **Statement Slide**: Centered bold statement, white background
- **Dark Slide**: Dark background, used for activities or key takeaways
- **Closing Slide**: Thank you / questions slide

**Slide Allocation:**
- Opening: 1 title slide
- Per major section (## header):
  - 1 section divider
  - 1 slide per distinct concept (not per paragraph)
  - 1 statement slide for core principles
- Closing: 1-2 slides (key takeaway + questions)

**Section Divider Colors:**
Rotate through brand accent colors:
- Section 1: Bright Yellow (#FFEB69)
- Section 2: Bright Blue (#A0E1E1)
- Section 3: Bright Pink (#FFD7EF)
- Section 4: Neutral (#F5F5F5)
- Repeat pattern for additional sections

**Slide Count Heuristic:**
- 80-minute workshop: 35-40 slides (2-2.5 min per slide)
- 30-minute talk: 15-20 slides
- 10-minute pitch: 6-8 slides
- Adjust based on content density and audience

### Outline Format

```markdown
# {Presentation Title} - Slide Outline

**Source:** {source-file.md}
**Total Slides:** 35
**Estimated Duration:** 80 minutes
**Generated:** 2026-05-22

## Outline

1. **Title Slide** - "{Main Title}"
2. **Section Divider** (Yellow #FFEB69) - "Learning Objectives"
3. **Content** - "What Surveys Are Good For"
4. **Content** - "What Surveys Can't Do"
5. **Statement** - "Surveys Start With Populations"
6. **Section Divider** (Blue #A0E1E1) - "Sampling"
7. **Content** - "Probabilistic Sampling Requirement"
8. **Content** - "Three Sampling Approaches"
9. **Content** - "Sample Size Power Calculation"
10. **Content** - "Statistical Power Requirements"
...
35. **Closing** - "Questions?"

## Notes

- Section dividers use Wise brand accent colors (rotate)
- Content slides follow "one key thing per slide" guideline
- Speaker notes will extract all detail from source markdown
- Slide content will be minimal (statements, not paragraphs)
```

### User Review

Present outline with:
```
Proposed Slide Outline

I've analyzed block1_design_your_survey.md and propose 35 slides:

- 1 title slide
- 6 section dividers
- 26 content slides
- 2 closing slides

Preview:
1. Title - "Design Your Survey"
2. Divider (Yellow) - "Learning Objectives"
3. Content - "What Surveys Are Good For"
...

Review this outline. You can:
• Edit slide titles
• Reorder slides
• Add or remove slides
• Change slide types
• Adjust section colors

Say "looks good" to begin slide generation, or describe changes.
```

## Phase 1: Slide Generation Loop

### Slide Generation Process

For each slide in outline:

**1. Extract Source Content**

Map outline slide to source content:
- Slide 3 "What Surveys Are Good For" → Lines 25-45 in source .md
- Find corresponding section by matching title/keywords
- Read entire section (not just first paragraph)

**2. Generate Slide Content**

Follow brand presentation guidelines:
- **One key thing per slide** (from `wise-brand-kit.json` → `presentationGuidelines.dos[0]`)
- **Minimal text** - statement or max 5 bullets
- **Bold simple statements** (from `bestPractices[0]`)
- **No busy slides** - if too much content, split across multiple slides

**Slide content should be:**
- Headlines and key statements
- Framework names (e.g., "The BRUSO Model")
- Short bullet lists (3-7 words each)
- Numbers/stats (e.g., "n=381", "80% confidence")
- Section titles

**Slide content should NOT be:**
- Paragraphs
- Long sentences
- Full explanations
- Examples (those go in notes)
- Citations (those go in notes)

**3. Generate Speaker Notes**

Load `speaker-notes-workflow.md` and follow principles:

Extract from source markdown:
- Opening context (why this slide matters)
- Main teaching content (ALL detail from source)
- Examples with full scenarios
- Citations and references (Author, Year)
- Facilitation guidance (questions, timing, transitions)

Format:
```html
<strong>Section heading</strong><br><br>

Paragraph of teaching content with specific examples and numbers...<br><br>

<ul>
<li><strong>Key point 1:</strong> Detail with evidence (Author, Year)</li>
<li><strong>Key point 2:</strong> Detail with example</li>
</ul><br>

<strong>Question to the room:</strong> "How would you calculate...?"<br><br>

<strong>Answer:</strong> Walk through calculation with specific numbers.
```

**4. Append to Markdown**

Append to `{name}-slides.md`:

```markdown
---

## Slide 3: What Surveys Are Good For

**Type:** content-slide
**Layout:** 60/40 left-content right-visual
**Background:** #F5F5F5 (Neutral)

**Slide Content:**
```html
<h2>What surveys are good for</h2>
<ul>
<li>Measuring at scale</li>
<li>Testing hypotheses</li>
<li>Quantifying relationships</li>
<li>Tracking changes over time</li>
</ul>
```

**Speaker Notes:**
<strong>Set the boundary conditions:</strong><br><br>

Surveys excel at measurement at scale. If you need to know "how many" or 
"how much" across a population, surveys are the right tool. They're designed 
for quantitative data collection, not qualitative exploration.<br><br>

<strong>Four core strengths:</strong>
<ul>
<li><strong>Scale:</strong> Reach hundreds or thousands efficiently</li>
<li><strong>Hypothesis testing:</strong> Confirm or refute specific claims</li>
<li><strong>Relationships:</strong> Measure correlations between variables</li>
<li><strong>Tracking:</strong> Compare responses over multiple waves</li>
</ul><br>

<strong>Key distinction:</strong> Surveys measure phenomena, they don't explain 
behavior. If you need to understand "why" people do something, use interviews 
or observational methods instead.
```

**5. Update HTML File**

Regenerate complete HTML:

1. **Parse markdown**: Read `{name}-slides.md`
2. **Extract all slides**: Split on `---` separator
3. **Parse each slide**:
   - Extract type, layout, background
   - Extract slide content HTML
   - Extract speaker notes HTML
4. **Generate HTML structure**:
   - Use template from `google-slides-templates.md`
   - Inject brand tokens from `{brand}.json`
   - Create `<div class="slide">` for each completed slide
   - Add navigation (arrows, keyboard)
   - Add presenter mode support
   - Add slide counter: "3 / 35 (8% complete)"
5. **Write file**: Overwrite `{name}-presentation.html`

**HTML Navigation Behavior:**
- Arrow keys work for completed slides only
- Can't navigate past last completed slide
- Slide counter shows progress: "3 / 35"

**6. Show Progress**

After each slide:

```
✓ Slide 3/35 complete: "What Surveys Are Good For"

Slide type: Content (60/40 layout)
Slide content: 4 bullet points (minimal text)
Speaker notes: 3 paragraphs with examples and teaching guidance

Files updated:
• design-your-survey-slides.md (Slide 3 appended)
• design-your-survey-presentation.html (regenerated with 3 slides)

Preview: Open design-your-survey-presentation.html in your browser

Continue? ("next" to generate Slide 4, "change X" to regenerate, "stop" to pause)
```

**7. Wait for User Input**

Accept commands:
- `"next"` / `"continue"` / `"looks good"` / `"yes"` → Generate next slide
- `"change [description]"` → Regenerate current slide with changes
- `"edit notes"` → Regenerate speaker notes only for current slide
- `"skip"` → Add placeholder, move to next slide
- `"stop"` / `"pause"` / `"save"` → Save progress, exit
- `"show outline"` → Display full outline again
- `"jump to N"` → Jump to slide N in outline
- `"regenerate HTML"` → Rebuild HTML from current .md

## Commands Reference

### During Outline Review

- `"looks good"` → Start generating slides from Slide 1
- `"change slide N to X"` → Edit specific slide in outline
- `"add slide after N: [description]"` → Insert new slide
- `"remove slide N"` → Delete slide from outline
- `"reorder: move slide N after M"` → Rearrange slides
- `"change section color N to [color]"` → Update divider color

### During Slide Generation

- `"next"` → Generate next slide
- `"change [aspect]"` → Regenerate current slide
  - Example: "change make bullets shorter"
  - Example: "change split into 2 slides"
- `"edit notes"` → Regenerate only speaker notes
- `"edit slide"` → Regenerate only slide content
- `"skip"` → Add placeholder, move forward
- `"back"` → Return to previous slide (regenerate option)
- `"jump to N"` → Skip to slide N
- `"stop"` → Save progress, exit iterative mode

### Utility Commands

- `"show outline"` → Display full slide outline
- `"show progress"` → Show completion status
- `"regenerate HTML"` → Rebuild HTML from markdown
- `"preview"` → Show last generated slide content
- `"edit outline"` → Return to outline editing phase

## Resume Support

If user stops and wants to continue later:

**Check for existing files:**
```bash
ls {name}-outline.md {name}-slides.md {name}-presentation.html
```

**If found:**
1. Read `{name}-slides.md`
2. Parse and count completed slides (count `## Slide N:` entries)
3. Read `{name}-outline.md` to get total slide count
4. Announce: "Found 12 of 35 slides complete. Resume from Slide 13?"
5. If yes: Continue loop from Slide 13
6. If no: Ask "Start over?" or "Edit existing slides?"

## Error Handling

**Missing source file:**
```
Error: Could not read source file "block1_design_your_survey.md"

Please provide the markdown file with your presentation content.
```

**Outline not confirmed:**
```
Outline must be reviewed before generating slides.

Current status: Draft outline created, awaiting review.
Say "looks good" to begin, or describe changes.
```

**Invalid slide number:**
```
Cannot jump to Slide 50 (outline has 35 slides).

Valid range: 1-35
```

## Best Practices

**For Claude:**
- Always show progress after each slide
- Keep slide content MINIMAL (follow Wise guidelines)
- Extract ALL detail from source into speaker notes
- Save markdown after each slide (don't wait)
- Regenerate HTML after each slide (user needs to preview)
- Be patient - wait for explicit user confirmation before continuing

**For Users:**
- Review outline carefully before starting (saves time)
- Open HTML in browser to preview as you go
- Edit markdown directly for quick tweaks
- Use "skip" if you want to fill in a slide later
- Use "stop" to pause - progress is saved automatically

## Example Session

```
User: /brand-content-studio slides --brand wise-brand-kit.json --mode iterative