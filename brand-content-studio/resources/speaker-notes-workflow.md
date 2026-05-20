# Speaker Notes Workflow

When generating HTML presentations, include a speaker notes creation process to help presenters prepare contextual guidance for each slide.

## When to Invoke

Automatically offer speaker notes creation:
- After generating slide content
- Before final output
- When user explicitly requests notes

## Workflow Stages

### Stage 1: Ask About Notes Preference

Use AskUserQuestion to determine approach:

**Question:** "Would you like to add speaker notes to help you present?"

**Options:**
1. **"Generate suggested notes"** - I'll draft contextual notes for each slide
2. **"I'll write my own"** - Export template with placeholder notes
3. **"Skip notes"** - Generate slides without notes

### Stage 2A: Generate Suggested Notes (Option 1)

For each slide, generate speaker notes that:

**Format:**
```html
<div class="speaker-notes">
    <h4>Speaker Notes</h4>
    <p>[contextual guidance for this slide]</p>
</div>
```

**Content Guidelines:**

1. **Opening slides**: Frame why this topic matters
2. **Data/visual slides**: Explain what to look for, key takeaways
3. **Process slides**: Walk through the sequence, highlight dependencies
4. **Conclusion slides**: Reinforce the forcing function or next action

**Tone:**
- Direct, conversational
- "You're telling them..." not "This slide shows..."
- Concrete, specific
- No fluff or repetition of slide content

**Length:** 1-3 sentences per slide

**Example - Data Slide:**
```
This is where most survey plans break. The overall N looks good, but the 
real question is about subgroups. Segment 5 (n=80) is below the reliable 
threshold. You can't run the analysis you planned. The solution isn't more 
data everywhere—it's strategic oversampling of the groups that matter.
```

**Example - Concept Slide:**
```
Start by setting clear expectations. Surveys are tools for measurement at 
scale, not explanation. This isn't a weakness—it's their design. Understanding 
this boundary prevents research plans that ask surveys to do work they can't do.
```

**Example - Process Slide:**
```
Population thinking comes first. The three boxes represent: theoretical 
population, reachable population, and analytically useful population. The gaps 
aren't errors—they're structural features of survey work. Ignoring them creates 
false confidence in bad data.
```

### Stage 2B: Provide Notes Template (Option 2)

Generate slides with empty speaker notes sections:

```html
<div class="speaker-notes">
    <h4>Speaker Notes</h4>
    <p>[Add your notes here - what context, examples, or stories will you share?]</p>
</div>
```

Tell user:
> "Added empty speaker notes to each slide. Edit the HTML file and replace 
> `[Add your notes here...]` with your own notes. They'll appear in presenter mode."

### Stage 3: Review & Iterate (Option 1 Only)

After generating notes, show user the first 2 slides with notes and ask:

**Question:** "Here are the speaker notes for slides 1-2. How do they feel?"

**Options:**
1. **"Perfect, generate the rest"** - Complete all remaining slides
2. **"Too detailed"** - Shorten to 1 sentence per slide
3. **"Too sparse"** - Expand to include examples/stories
4. **"Different tone"** - Adjust voice (more formal, more conversational, etc.)

Apply feedback to remaining slides.

### Stage 4: Final Output

Generate HTML presentation with:
- ✅ Speaker notes embedded in each slide
- ✅ Hidden by default during presentation
- ✅ Visible in presenter mode (Press 'P')
- ✅ Displayed in dual-window presenter view

**Tell user:**
> "✓ Added speaker notes to all 6 slides
> 
> **To view notes:**
> - Press 'P' for presenter mode (shows all slides + notes)
> - Click '🎬 Start Presenting' for dual-window mode
>   - Presenter window shows: current slide, next slide, notes, timer
>   - Main window shows: current slide only (for audience)
> 
> **To edit notes:**
> - Open the HTML file in any text editor
> - Find `<div class="speaker-notes">` sections
> - Edit the `<p>` content inside"

## Notes Writing Principles

### What Makes Good Speaker Notes

**DO:**
- ✅ Explain why this slide matters in the flow
- ✅ Highlight what to emphasize or call out
- ✅ Note common questions or objections this slide addresses
- ✅ Remind presenter of examples or stories to share
- ✅ Flag tricky transitions or non-obvious connections

**DON'T:**
- ❌ Repeat what's already on the slide
- ❌ Write full scripts to read verbatim
- ❌ Add generic filler ("This slide discusses...")
- ❌ Over-explain obvious content
- ❌ Write for the audience (notes are for the presenter)

### Contextual Note Types

**For Opening Slides:**
- Why this topic matters now
- What problem we're solving
- How this connects to audience needs

**For Data/Evidence Slides:**
- What to look for in the visual
- The one number/insight that matters most
- Common misinterpretations to avoid

**For Process/Framework Slides:**
- Walk through the sequence
- Highlight dependencies or non-obvious steps
- Note where people typically get stuck

**For Comparison Slides:**
- What's being compared and why
- Which option is recommended (if any)
- Key tradeoffs to acknowledge

**For Closing/Action Slides:**
- The forcing function or key question
- Next concrete step
- What success looks like

## Examples by Slide Type

### Example 1: Concept Introduction
**Slide:** "Surveys measure scale. They don't explain behaviour."

**Good notes:**
```
Start by setting clear expectations. Surveys are tools for measurement at 
scale, not explanation. This isn't a weakness—it's their design. Understanding 
this boundary prevents research plans that ask surveys to do work they can't do.
```

### Example 2: Data Visualization
**Slide:** Bar chart showing segment sizes (80, 120, 200, 250, 350)

**Good notes:**
```
This is where most survey plans break. The overall N looks good, but the real 
question is about subgroups. Segment 5 (n=80) is below the reliable threshold. 
You can't run the analysis you planned. The solution isn't more data everywhere—
it's strategic oversampling of the groups that matter.
```

### Example 3: Framework/Process
**Slide:** Three-box funnel (Who exists → Who we reach → Who we analyze)

**Good notes:**
```
Population thinking comes first. The three boxes represent: theoretical population, 
reachable population, and analytically useful population. The gaps aren't errors—
they're structural features of survey work. Ignoring them creates false confidence 
in bad data.
```

### Example 4: Comparison
**Slide:** Proportional sample vs. Oversampled version (side-by-side)

**Good notes:**
```
Same population, different sample design. Proportional sampling makes the rare 
group invisible. Oversampling gives you enough n to analyze separately, then you 
weight back during analysis. This isn't a workaround—it's standard practice for 
hard-to-reach populations.
```

### Example 5: Checklist/Action
**Slide:** "Have you planned your subgroup Ns?"

**Good notes:**
```
End with the planning checklist. These three steps happen before fielding. If 
you skip them, you're hoping the data will be usable. Hope is not a research 
strategy. The question at the end is the forcing function: "Have you planned 
your subgroup Ns?" If the answer is no, you're not ready to field.
```

## Integration with Presentation Template

Speaker notes are embedded in each slide's HTML structure:

```html
<div class="slide">
    <div class="slide-content">
        <h1>Slide Title</h1>
        <p class="core-content">Slide content...</p>
        
        <!-- Visual elements -->
        <div class="chart-container">...</div>
        
        <!-- Speaker notes (hidden by default) -->
        <div class="speaker-notes">
            <h4>Speaker Notes</h4>
            <p>Contextual guidance for presenter...</p>
        </div>
    </div>
</div>
```

**CSS ensures:**
- Notes hidden during presentation (`display: none`)
- Notes visible in presenter mode
- Notes visible in dual-window presenter view
- Notes excluded from PDF export (unless explicitly included)

## User Instructions to Include

When delivering final presentation, tell user:

```
📝 SPEAKER NOTES INCLUDED

Your presentation includes speaker notes on [X] of [Y] slides.

TO VIEW NOTES:
1. Press 'P' → Presenter mode (all slides + notes visible)
2. Click '🎬 Start Presenting' → Dual-window presenter view
   - Shows current slide, next slide, notes, and timer
   - Drag presenter window to laptop, main window to projector

TO EDIT NOTES:
1. Open HTML file in text editor
2. Find <div class="speaker-notes">
3. Edit the <p> content inside
4. Save and reload in browser

TO PRINT WITH NOTES:
1. Press 'P' for presenter mode
2. Cmd/Ctrl+P to print
3. Notes will appear below each slide

TO REMOVE NOTES:
Delete the <div class="speaker-notes">...</div> sections
```

## Default Behavior

**If user doesn't explicitly request notes:**
- Don't add them automatically
- Don't ask about notes mid-flow
- Mention at end: "Want to add speaker notes? I can generate contextual guidance for each slide."

**If user says "add speaker notes" after initial generation:**
- Read existing slides
- Generate notes following the principles above
- Insert into HTML
- Provide updated file

## Quality Checklist

Before delivering speaker notes, verify:
- ✅ Each note adds context not on the slide
- ✅ Notes explain *why* or *how*, not *what*
- ✅ Tone is conversational and direct
- ✅ Length is 1-3 sentences per slide
- ✅ Notes help presenter, not audience
- ✅ No generic filler or obvious content
- ✅ Notes are properly embedded in HTML structure
