# Iterative Mode - Quick Start Guide

Generate presentations one slide at a time with review after each.

## When to Use

✅ **Use Iterative Mode when:**
- Important presentations (keynotes, investor pitches)
- Complex content that needs careful refinement
- Learning new content as you build
- Working with stakeholder review cycles
- Want to preview each slide in browser before moving on

✅ **Use Batch Mode when:**
- Quick drafts or internal presentations
- Familiar content that's straightforward
- Time-constrained situations
- Content is already well-structured

## Quick Start

### 1. Invoke with Iterative Flag

```bash
/brand-content-studio slides --brand wise-brand-kit.json --mode iterative
```

### 2. Provide Source Content

```
Claude: What's your source content file?

You: block1_design_your_survey.md
```

### 3. Review Proposed Outline

Claude analyzes your content and proposes a slide outline:

```
Proposed Slide Outline (35 slides)

1. Title Slide - "Design Your Survey"
2. Section Divider (Yellow) - "Learning Objectives"
3. Content - "What Surveys Are Good For"
4. Content - "What Surveys Can't Do"
...
35. Closing - "Questions?"

Review this outline. You can:
• Edit slide titles
• Reorder slides
• Add or remove slides
• Change slide types

Say "looks good" to begin generating slides.
```

### 4. Edit Outline (Optional)

Make changes:
```
You: change slide 3 to "Why Surveys Matter in Tech"
You: add slide after 5: "Population Thinking Framework"
You: looks good
```

### 5. Generate Slides One-by-One

Claude generates each slide and waits for your approval:

```
✓ Slide 1/35 complete: "Design Your Survey"

Slide content: Title + subtitle (minimal text)
Speaker notes: 3 paragraphs with session overview

Files updated:
• design-your-survey-slides.md (created)
• design-your-survey-presentation.html (created)

Preview: Open design-your-survey-presentation.html in browser

Options:
• "next" - Generate Slide 2
• "change X" - Regenerate this slide
• "stop" - Save and exit
```

### 6. Continue or Edit

```
You: next
```

Or make changes:
```
You: change make subtitle shorter
You: edit notes add example about HVC users
```

### 7. Preview in Browser

Open the HTML file after any slide to see how it looks:

```bash
open design-your-survey-presentation.html
```

- Navigate with arrow keys
- Press 'P' for presenter mode
- See speaker notes in presenter window

## Common Commands

### During Outline Review
- `"looks good"` - Start generating slides
- `"change slide N to X"` - Edit specific slide
- `"add slide after N: [description]"` - Insert slide
- `"remove slide N"` - Delete slide

### During Slide Generation
- `"next"` / `"continue"` - Generate next slide
- `"change [description]"` - Regenerate current slide
- `"edit notes"` - Regenerate speaker notes only
- `"skip"` - Add placeholder, move forward
- `"stop"` - Save progress, exit

### Utility Commands
- `"show outline"` - Display full outline
- `"show progress"` - Show completion status
- `"jump to N"` - Skip to slide N

## File Structure

Iterative mode creates these files:

```
design-your-survey-outline.md          # Slide outline (Step 0)
design-your-survey-slides.md           # Slides appended incrementally
design-your-survey-presentation.html   # HTML regenerated after each slide
```

**Markdown format:**
```markdown
## Slide 3: What Surveys Are Good For

**Type:** content-slide
**Layout:** 60/40 left-content right-visual

**Slide Content:**
```html
<h2>What surveys are good for</h2>
<ul>
<li>Measuring at scale</li>
<li>Testing hypotheses</li>
<li>Quantifying relationships</li>
</ul>
```

**Speaker Notes:**
Full teaching script with examples, citations, and facilitation guidance...
```

## Resume Later

If you stop mid-generation:

```bash
/brand-content-studio slides --brand wise.json --mode iterative
```

Claude detects existing progress:

```
Found design-your-survey-slides.md with 12 completed slides.

Resume from Slide 13? (yes/no)
```

## Tips

**1. Review the outline carefully**
- Saves time to get structure right upfront
- Easier to reorder slides in outline than after generation

**2. Open HTML in browser early**
- Preview after Slide 2-3 to check style/flow
- Make adjustments before generating 30 more slides

**3. Use "skip" for uncertain slides**
- Add placeholder, come back later
- Don't get stuck on one difficult slide

**4. Edit markdown directly for quick tweaks**
- Faster than regenerating via commands
- Just edit `design-your-survey-slides.md`
- Run "regenerate HTML" after

**5. Save often**
- Progress auto-saves after each slide
- Use "stop" anytime without losing work

**6. Use feedback to improve subsequent slides**
- "change make bullets shorter" on Slide 3
- Claude applies that feedback to Slides 4-35

## Comparison: Batch vs Iterative

| Feature | Batch Mode | Iterative Mode |
|---------|-----------|----------------|
| Speed | Fast | Slower (interactive) |
| Control | Low | High |
| Preview | At end only | After each slide |
| Edit | Regenerate all | Edit one slide |
| Resume | No | Yes |
| Best for | Quick drafts | Important decks |

## Troubleshooting

**"Outline too long" (50+ slides)**
→ Ask Claude to condense sections or split into multiple presentations

**"Slide content still too busy"**
→ Use "change split into 2 slides" to break up dense content

**"Speaker notes too brief"**
→ Use "edit notes add more examples and citations from source"

**"Can't open HTML file"**
→ Check file path, make sure it's in your current directory

**"Lost my place"**
→ Run "show progress" to see current status

## Example Session

```
You: /brand-content-studio slides --brand wise.json --mode iterative

Claude: What's your source content file?

You: block1_design_your_survey.md

Claude: [Analyzes and proposes 35-slide outline]

You: looks good

Claude: [Generates Slide 1, shows progress]

You: next

Claude: [Generates Slide 2]

You: change make it a statement slide instead of divider

Claude: [Regenerates Slide 2 as statement slide]

You: next

[Continue through all slides...]

Claude: ✓ All 35 slides complete!

Files created:
• design-your-survey-outline.md
• design-your-survey-slides.md
• design-your-survey-presentation.html

Open design-your-survey-presentation.html to present!
```

## Next Steps

After generating all slides:

1. **Review full presentation** in browser
2. **Test presenter mode** - Click "🎬 Start Presenting"
3. **Make final edits** - Edit markdown directly
4. **Regenerate HTML** - From markdown if needed
5. **Export** - PDF via print, or PPTX via conversion tools

---

**Ready to try it?**

```bash
/brand-content-studio slides --brand your-brand.json --mode iterative
```
