# Google Slides Templates

HTML-based slide templates that can be converted to PPTX or viewed directly.

## Template Structure

Each template is a self-contained HTML file with:
- Responsive slide sizing (16:9 aspect ratio)
- Print-friendly CSS for PDF export
- Keyboard navigation (arrow keys)
- Brand token injection points
- Export metadata for PPTX conversion

## Base HTML Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{BRAND_NAME}} - {{PRESENTATION_TITLE}}</title>
    <style>
        :root {
            /* Brand tokens injected here */
            --color-primary: {{PRIMARY_COLOR}};
            --color-secondary: {{SECONDARY_COLOR}};
            --color-accent: {{ACCENT_COLOR}};
            --color-text-primary: {{TEXT_PRIMARY}};
            --color-text-secondary: {{TEXT_SECONDARY}};
            --color-background: {{BG_PRIMARY}};
            --font-heading: {{FONT_HEADING}};
            --font-body: {{FONT_BODY}};
            --spacing-unit: {{SPACING_UNIT}}px;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: var(--font-body);
            background: #1a1a1a;
            color: var(--color-text-primary);
            overflow: hidden;
        }

        .presentation {
            width: 100vw;
            height: 100vh;
            position: relative;
        }

        .slide {
            width: 100%;
            height: 100%;
            position: absolute;
            top: 0;
            left: 0;
            display: none;
            background: var(--color-background);
            padding: calc(var(--spacing-unit) * 6);
        }

        .slide.active {
            display: flex;
            flex-direction: column;
        }

        /* Slide layouts */
        .slide-title {
            justify-content: center;
            align-items: center;
            text-align: center;
        }

        .slide-content {
            justify-content: flex-start;
        }

        .slide-two-column {
            flex-direction: row;
            gap: calc(var(--spacing-unit) * 4);
        }

        /* Typography */
        h1 {
            font-family: var(--font-heading);
            font-size: 4rem;
            font-weight: 700;
            color: var(--color-primary);
            margin-bottom: calc(var(--spacing-unit) * 2);
        }

        h2 {
            font-family: var(--font-heading);
            font-size: 3rem;
            font-weight: 700;
            margin-bottom: calc(var(--spacing-unit) * 3);
        }

        h3 {
            font-family: var(--font-heading);
            font-size: 2rem;
            font-weight: 600;
            margin-bottom: calc(var(--spacing-unit) * 2);
        }

        p {
            font-size: 1.5rem;
            line-height: 1.6;
            color: var(--color-text-secondary);
            margin-bottom: calc(var(--spacing-unit) * 2);
        }

        ul {
            list-style: none;
            padding-left: 0;
        }

        li {
            font-size: 1.5rem;
            line-height: 1.8;
            margin-bottom: calc(var(--spacing-unit) * 2);
            padding-left: calc(var(--spacing-unit) * 4);
            position: relative;
        }

        li::before {
            content: "→";
            position: absolute;
            left: 0;
            color: var(--color-accent);
            font-weight: bold;
        }

        /* Components */
        .logo {
            font-size: 2rem;
            font-weight: 700;
            color: var(--color-primary);
        }

        .subtitle {
            font-size: 2rem;
            color: var(--color-text-secondary);
            font-weight: 400;
        }

        .highlight {
            color: var(--color-accent);
            font-weight: 600;
        }

        .card {
            background: var(--color-background);
            border: 2px solid var(--color-primary);
            border-radius: calc(var(--spacing-unit) * 2);
            padding: calc(var(--spacing-unit) * 3);
            flex: 1;
        }

        .image-container {
            width: 100%;
            height: 400px;
            background: var(--color-primary);
            border-radius: calc(var(--spacing-unit) * 2);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 1.5rem;
            margin: calc(var(--spacing-unit) * 2) 0;
        }

        /* Navigation */
        .slide-number {
            position: absolute;
            bottom: calc(var(--spacing-unit) * 2);
            right: calc(var(--spacing-unit) * 3);
            font-size: 1.2rem;
            color: var(--color-text-secondary);
        }

        /* Print styles for PDF export */
        @media print {
            body {
                background: white;
            }

            .slide {
                page-break-after: always;
                display: flex !important;
                position: relative;
            }

            .slide.active {
                display: flex !important;
            }
        }
    </style>
</head>
<body>
    <div class="presentation">
        {{SLIDES_CONTENT}}
    </div>

    <script>
        let currentSlide = 0;
        const slides = document.querySelectorAll('.slide');

        function showSlide(n) {
            slides.forEach(s => s.classList.remove('active'));
            currentSlide = (n + slides.length) % slides.length;
            slides[currentSlide].classList.add('active');
        }

        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowRight' || e.key === ' ') {
                showSlide(currentSlide + 1);
            } else if (e.key === 'ArrowLeft') {
                showSlide(currentSlide - 1);
            } else if (e.key === 'Home') {
                showSlide(0);
            } else if (e.key === 'End') {
                showSlide(slides.length - 1);
            }
        });

        showSlide(0);
    </script>
</body>
</html>
```

## Slide Type Components

### Title Slide

```html
<div class="slide slide-title">
    <div class="logo">{{BRAND_NAME}}</div>
    <h1>{{TITLE}}</h1>
    <p class="subtitle">{{SUBTITLE}}</p>
</div>
```

### Content Slide

```html
<div class="slide slide-content">
    <h2>{{SLIDE_TITLE}}</h2>
    <ul>
        {{#each BULLET_POINTS}}
        <li>{{this}}</li>
        {{/each}}
    </ul>
    <div class="slide-number">{{SLIDE_NUMBER}} / {{TOTAL_SLIDES}}</div>
</div>
```

### Two Column Slide

```html
<div class="slide slide-two-column">
    <div style="flex: 1;">
        <h2>{{LEFT_TITLE}}</h2>
        <p>{{LEFT_CONTENT}}</p>
    </div>
    <div style="flex: 1;">
        <div class="image-container">
            {{IMAGE_PLACEHOLDER}}
        </div>
    </div>
    <div class="slide-number">{{SLIDE_NUMBER}} / {{TOTAL_SLIDES}}</div>
</div>
```

### Image + Caption Slide

```html
<div class="slide slide-content">
    <h2>{{SLIDE_TITLE}}</h2>
    <div class="image-container">
        {{IMAGE_PLACEHOLDER}}
    </div>
    <p style="text-align: center; font-style: italic;">{{CAPTION}}</p>
    <div class="slide-number">{{SLIDE_NUMBER}} / {{TOTAL_SLIDES}}</div>
</div>
```

### Quote Slide

```html
<div class="slide slide-title">
    <h1 style="font-size: 3rem; font-style: italic; max-width: 80%;">
        "{{QUOTE_TEXT}}"
    </h1>
    <p class="subtitle">— {{ATTRIBUTION}}</p>
    <div class="slide-number">{{SLIDE_NUMBER}} / {{TOTAL_SLIDES}}</div>
</div>
```

### Data/Stats Slide

```html
<div class="slide slide-content">
    <h2>{{SLIDE_TITLE}}</h2>
    <div style="display: flex; gap: calc(var(--spacing-unit) * 4); margin-top: calc(var(--spacing-unit) * 4);">
        {{#each STATS}}
        <div class="card">
            <h1 class="highlight">{{value}}</h1>
            <p>{{label}}</p>
        </div>
        {{/each}}
    </div>
    <div class="slide-number">{{SLIDE_NUMBER}} / {{TOTAL_SLIDES}}</div>
</div>
```

## Corporate Deck Template

Pre-assembled slide sequence:

1. Title slide (brand + presentation title)
2. Agenda slide (bullet points)
3. Content slides (2-3 with key points)
4. Two-column slide (text + visual)
5. Data slide (stats cards)
6. Closing slide (CTA or thank you)

## Creative Pitch Template

Pre-assembled sequence:

1. Bold title slide (large statement)
2. Problem slide (challenge definition)
3. Solution slide (your approach)
4. Visual demonstration (2-column)
5. Impact slide (stats)
6. Next steps slide

## Data Presentation Template

Pre-assembled sequence:

1. Executive summary title
2. Key metrics slide (stat cards)
3. Trend analysis (placeholder for chart)
4. Insights slide (bullet points)
5. Recommendations slide
6. Appendix title slide

## Export Instructions

### To Google Slides

1. Open Google Slides
2. File → Import slides → Upload HTML (not directly supported)
3. **Alternative**: Use print-to-PDF, then import PDF to Google Slides
4. Google Slides will convert each page to a slide

### To PPTX (via LibreOffice)

```bash
# Convert HTML to PDF
wkhtmltopdf --enable-local-file-access slides.html slides.pdf

# Convert PDF to PPTX (requires LibreOffice)
libreoffice --headless --convert-to pptx slides.pdf
```

### Direct PPTX Generation (Python)

Use `python-pptx` to generate native PPTX:

```python
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN

def create_pptx(brand, content):
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(5.625)  # 16:9
    
    # Apply brand colors to master
    # Add slides based on content
    # ...
    
    prs.save('output.pptx')
```

## Token Injection

Before rendering, replace placeholders with brand tokens:

- `{{PRIMARY_COLOR}}` → brand.colors.primary
- `{{SECONDARY_COLOR}}` → brand.colors.secondary
- `{{FONT_HEADING}}` → brand.typography.heading.family
- `{{SPACING_UNIT}}` → brand.spacing.unit

## Usage in Skill

1. User selects layout type (Corporate/Creative/Data)
2. Load corresponding template
3. Inject brand tokens from brand JSON
4. Populate content slides from user input
5. Generate HTML file
6. Offer export options (view in browser, convert to PPTX, print to PDF)
