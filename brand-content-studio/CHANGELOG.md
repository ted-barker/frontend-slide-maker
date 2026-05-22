# Brand Content Studio - Changelog

## Version 1.1.0 - Iterative Mode (2026-05-22)

### New Feature: Iterative Slide Generation

Added slide-by-slide generation mode for presentations where you want to review and refine each slide before moving to the next.

**Key additions:**

1. **New flag: `--mode iterative`**
   - Generate slides one-by-one instead of all at once
   - Review and edit each slide before continuing
   - Progress saved incrementally

2. **Step 0: Outline Generation**
   - Analyzes source content file (markdown)
   - Proposes slide-by-slide structure
   - User reviews and edits outline before generation begins
   - Saves outline to `{name}-outline.md`

3. **Incremental File Updates**
   - Each slide appended to `{name}-slides.md` (markdown format)
   - HTML regenerated after each slide
   - User can preview in browser after each slide
   - Progress saved automatically

4. **Interactive Commands**
   - `"next"` - Generate next slide
   - `"change X"` - Regenerate current slide with modifications
   - `"edit notes"` - Regenerate speaker notes only
   - `"skip"` - Add placeholder, move forward
   - `"stop"` - Save progress, exit (can resume later)
   - `"show outline"` - Display full outline
   - `"jump to N"` - Skip to specific slide

5. **Resume Support**
   - Detects existing progress files
   - Offers to continue from last completed slide
   - No work lost if interrupted

**Files Created/Modified:**

- `SKILL.md` - Updated with iterative workflow
- `README.md` - Added iterative mode examples
- `resources/iterative-mode.md` - New detailed implementation guide
- `CHANGELOG.md` - This file

**Benefits:**

✅ Fine-grained control over each slide  
✅ Preview HTML as you go  
✅ Learning loop (each slide improves based on feedback)  
✅ Resume from any point  
✅ Markdown files are git-friendly  
✅ Can regenerate HTML from markdown anytime  

**Usage:**

```bash
# Iterative mode
/brand-content-studio slides --brand wise.json --mode iterative

# Batch mode (default, unchanged)
/brand-content-studio slides --brand wise.json
```

**Backward Compatibility:**

- Default behavior unchanged (batch mode)
- Existing workflows continue to work
- New mode is opt-in via `--mode iterative` flag

---

## Version 1.0.0 - Initial Release (2026-05-19)

Initial release of Brand Content Studio skill with:
- Brand asset extraction from HEX, PPTX, images
- Google Slides HTML generation
- FigJam board generation
- Visual preview selection
- Speaker notes workflow
- Progressive disclosure architecture
- Token-based design system
