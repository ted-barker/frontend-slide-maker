# Brand Content Studio - Architecture

Technical design document explaining how this skill works.

## Design Philosophy

This skill demonstrates **advanced Claude Code skill patterns** learned from analyzing [frontend-slides](https://github.com/zarazhangrui/frontend-slides):

1. **Progressive Disclosure** - Lightweight core loads resources on-demand
2. **Visual Preview Selection** - Show options instead of asking users to describe them
3. **Token-Based Design** - Single source of truth for brand values
4. **Multi-Format Output** - Same brand data, multiple export formats
5. **Persistent Brand Assets** - Reusable design systems across sessions

## File Structure

```
brand-content-studio/
├── SKILL.md                          # Core workflow (loaded first)
├── README.md                         # User documentation
├── ARCHITECTURE.md                   # This file
├── install.sh                        # Setup script
│
├── resources/                        # Loaded on-demand
│   ├── brand-parser.py              # Extract design tokens
│   ├── color-system.md              # Color theory and generation
│   ├── layout-previews.md           # ASCII mockups for AskUserQuestion
│   ├── google-slides-templates.md   # HTML slide templates
│   └── figjam-templates.md          # FigJam JSON structures
│
└── examples/
    └── example-brand.json           # Sample brand system
```

## Execution Flow

### Phase 1: Brand Asset Initialization

```
User invokes: /brand-content-studio
    ↓
Check: ~/.claude/memory/brands/{name}.json exists?
    ↓
NO → Brand Setup Flow
    ↓
Load: resources/brand-parser.py (if extraction needed)
Load: resources/color-system.md (if HEX input)
    ↓
Generate complete design system:
- Color palette (primary/secondary/accent)
- Semantic colors (success/warning/error/info)
- Typography (heading/body/mono)
- Spacing scale
- Effects (shadows/radius/blur)
    ↓
Save: ~/.claude/memory/brands/{name}.json
```

### Phase 2: Content Type Selection

```
Load: resources/layout-previews.md
    ↓
Generate 3 visual previews for chosen format:
- Google Slides: Corporate/Creative/Data
- FigJam: Brainstorm/Process/Workshop
    ↓
Use AskUserQuestion with preview field:
{
  "question": "Which layout fits your content?",
  "options": [
    {
      "label": "Corporate Deck",
      "description": "Professional, balanced...",
      "preview": "[ASCII mockup here]"
    }
  ]
}
    ↓
User sees side-by-side layout comparison
User selects preferred option
```

### Phase 3: Content Generation

```
Load appropriate template:
- Google Slides → resources/google-slides-templates.md
- FigJam → resources/figjam-templates.md
    ↓
Inject brand tokens into template:
{{PRIMARY_COLOR}} → brand.colors.primary
{{FONT_HEADING}} → brand.typography.heading.family
{{SPACING_UNIT}} → brand.spacing.unit
    ↓
Populate with user content:
- Slide titles
- Bullet points
- Images/placeholders
- Data/stats
    ↓
Generate output file(s):
- HTML (immediate preview)
- FigJam JSON (direct import)
- Conversion scripts (PPTX, PDF)
```

## Key Design Patterns

### 1. Progressive Disclosure

**Problem**: Skills with many resources are slow to load.

**Solution**: Core workflow in SKILL.md, everything else loaded on-demand.

```markdown
# SKILL.md (always loaded, ~200 lines)

When user needs color generation:
  → Load resources/color-system.md

When user needs layout preview:
  → Load resources/layout-previews.md

When user generates slides:
  → Load resources/google-slides-templates.md
```

**Benefits**:
- Fast initial load
- Only pay context cost for what you use
- Easy to extend (add new resources without bloating core)

### 2. Visual Preview Selection

**Problem**: Users struggle to articulate design preferences verbally.

**Solution**: Generate ASCII mockups, show side-by-side with AskUserQuestion.

```python
AskUserQuestion({
  "question": "Which layout?",
  "options": [
    {
      "label": "Corporate",
      "description": "Professional style",
      "preview": """
┌─────────────────┐
│  [LOGO]         │
│                 │
│  ████ Title     │
│    Subtitle     │
│                 │
│  • Point 1      │
│  • Point 2      │
└─────────────────┘
      """
    }
  ]
})
```

**Benefits**:
- User sees actual layouts, not descriptions
- Faster decision-making
- Reduces back-and-forth iterations
- Universal (no design vocabulary needed)

### 3. Token-Based Design

**Problem**: Hard-coding values in templates is inflexible.

**Solution**: Centralized brand JSON with semantic tokens.

```json
{
  "colors": {
    "primary": "#FF5733",     // Token
    "secondary": "#3498DB"    // Token
  }
}
```

```html
<!-- Template uses tokens -->
<style>
  :root {
    --color-primary: {{PRIMARY_COLOR}};
  }
</style>
```

**Benefits**:
- Change brand once, updates everywhere
- Easy to maintain consistency
- Format-agnostic (same tokens for HTML, FigJam, etc.)
- Validates at generation time

### 4. Multi-Format Output

**Problem**: Different tools need different formats.

**Solution**: Abstract content model, render to multiple formats.

```
Content Model (abstract):
- Title: "Q2 Roadmap"
- Sections: [{title, bullets}]
- Brand: brand.json

    ↓

Renderers (format-specific):
- HTML Renderer → slides.html
- FigJam Renderer → board.figjam
- PPTX Renderer → deck.pptx
```

**Benefits**:
- Write content once, export many ways
- Each format optimized for its tool
- Easy to add new formats (just new renderer)

### 5. Persistent Brand Assets

**Problem**: Recreating brand each session is tedious.

**Solution**: Save to `~/.claude/memory/brands/`, reuse across sessions.

```bash
~/.claude/memory/brands/
├── acme-corp.json
├── startup-x.json
└── client-project.json

# Next session:
/brand-content-studio --brand acme-corp.json
# ✓ Loaded existing brand, ready to create
```

**Benefits**:
- Faster subsequent uses
- Consistent branding across projects
- Share brand files with teammates
- Version control friendly

## Technical Decisions

### Why HTML for Slides?

**Alternatives considered**: Direct PPTX generation, Google Slides API

**Chosen**: HTML + conversion tools

**Rationale**:
- ✓ Zero dependencies for basic usage
- ✓ Universal preview (any browser)
- ✓ Full design control (CSS)
- ✓ Easy to iterate locally
- ✓ Can convert to PPTX/PDF later
- ✗ Not native PowerPoint (but conversion is good enough)

### Why FigJam JSON?

**Alternatives considered**: Miro API, Figma plugin, image generation

**Chosen**: FigJam-compatible JSON structure

**Rationale**:
- ✓ Direct import (no API needed)
- ✓ Preserves interactivity (editable after import)
- ✓ No authentication required
- ✓ Can generate HTML preview for validation
- ✗ FigJam-specific (but could add Miro later)

### Why Python for Brand Parser?

**Alternatives considered**: Pure JavaScript, bash + imagemagick

**Chosen**: Python with optional libs

**Rationale**:
- ✓ `python-pptx` is mature, well-documented
- ✓ `Pillow` for robust image processing
- ✓ Rich color manipulation libraries
- ✓ Optional dependency (skill works without it)
- ✗ Requires Python (but most devs have it)

### Why Store Brands in Memory?

**Alternatives considered**: Project .claude folder, separate config

**Chosen**: `~/.claude/memory/brands/`

**Rationale**:
- ✓ Accessible from any project
- ✓ User controls it (in their home dir)
- ✓ Version control optional (user choice)
- ✓ Follows Claude Code memory patterns
- ✗ Not committed by default (but that's a feature)

## Extension Points

### Adding New Content Types

1. Create new template file in `resources/`
2. Add to layout-previews.md
3. Update SKILL.md workflow to load it
4. Implement token injection logic

**Example**: Add Miro boards

```
resources/miro-templates.md
    ↓
Update layout-previews.md with Miro mockups
    ↓
SKILL.md: load resources/miro-templates.md when selected
```

### Adding New Brand Sources

1. Extend `resources/brand-parser.py` with new extractor
2. Update SKILL.md to offer new source option
3. Test extraction produces valid brand JSON

**Example**: Extract from Figma URL

```python
class FigmaExtractor:
    def __init__(self, figma_url, api_token):
        # Fetch via Figma API
        # Extract colors, fonts, styles

    def extract_colors(self):
        # Return list of HEX colors
```

### Adding New Export Formats

1. Create converter function
2. Add to `resources/export-handlers.md` (new file)
3. Update SKILL.md to offer export option

**Example**: Add Keynote export

```python
def convert_html_to_keynote(html_file):
    # Use applescript or keynote automation
    # Convert slides to .key format
```

## Performance Considerations

### Context Window Management

- **Core workflow**: ~200 lines (minimal)
- **Resource files**: 200-500 lines each (loaded as needed)
- **Brand JSON**: ~100 lines (loaded once, reused)
- **Total for typical session**: <2000 lines

**Optimization**: Only load what's needed for current operation.

### Generation Speed

- **Brand from HEX**: Instant (pure calculation)
- **Brand from PPTX**: 1-3 seconds (file parsing)
- **Brand from image**: 2-5 seconds (color quantization)
- **Slide generation**: 1-2 seconds (template injection)
- **FigJam generation**: <1 second (JSON construction)

**Optimization**: Pre-generate common patterns, cache calculations.

### File Size

- **HTML slides**: 10-50 KB (single file, embedded CSS/JS)
- **FigJam JSON**: 5-20 KB (structure only)
- **Brand JSON**: 2-5 KB (design tokens)
- **PPTX export**: 50-500 KB (depends on images)

**Optimization**: Minify HTML/CSS, compress images, inline only essential assets.

## Testing Strategy

### Unit Tests

- Color conversion (HEX ↔ RGB ↔ HSL)
- Contrast ratio calculations
- Brand token injection
- Template rendering

### Integration Tests

- Brand extraction from PPTX
- Full workflow: HEX → brand → slides → HTML
- Multi-format export (HTML → PDF → PPTX)

### Visual Regression Tests

- Screenshot generated slides
- Compare against reference images
- Detect layout/style regressions

### Accessibility Tests

- Validate WCAG contrast ratios
- Check semantic HTML structure
- Test keyboard navigation (slides)

## Future Enhancements

### Short Term

- [ ] Animation presets (fade, slide, zoom)
- [ ] Chart generation from CSV data
- [ ] More layout templates (timeline, comparison)
- [ ] Brand theme variants (dark mode)

### Medium Term

- [ ] Real-time collaboration (WebSocket sync)
- [ ] Version history for brands
- [ ] AI-generated content suggestions
- [ ] Smart color palette recommendations

### Long Term

- [ ] Full Figma integration (read/write)
- [ ] Video storyboard generation
- [ ] Brand compliance checker (scan repos)
- [ ] Multi-language support (i18n)

## Lessons from frontend-slides

What this skill learned from [@zarazhangrui](https://github.com/zarazhangrui)'s excellent work:

1. **Progressive disclosure is essential** - Don't load everything upfront
2. **Visual previews > verbal descriptions** - Show, don't tell
3. **Single HTML file is powerful** - No dependencies = easy sharing
4. **Curated options > infinite configuration** - 3 good choices > 100 mediocre ones
5. **Focus on workflow, not just output** - The journey matters as much as the destination

## Contributing

To extend this skill:

1. Follow progressive disclosure pattern
2. Maintain token-based design consistency
3. Add visual previews for new options
4. Update documentation (README + this file)
5. Test across formats (HTML, PPTX, FigJam)

## License

MIT - Use this as a template for your own skills!
