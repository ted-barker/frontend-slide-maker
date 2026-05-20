# FigJam Templates

Generate FigJam-compatible board structures with brand styling.

## FigJam JSON Schema

FigJam files use a specific JSON structure that can be imported:

```json
{
  "name": "Board Name",
  "version": "1.0",
  "nodes": [
    {
      "id": "node-1",
      "type": "STICKY",
      "x": 100,
      "y": 100,
      "width": 200,
      "height": 200,
      "fills": [{"type": "SOLID", "color": {"r": 1, "g": 0.8, "b": 0.2}}],
      "text": "Sticky note content",
      "fontSize": 24
    }
  ],
  "connectors": [
    {
      "id": "connector-1",
      "type": "ARROW",
      "startNode": "node-1",
      "endNode": "node-2"
    }
  ]
}
```

## Node Types

### Sticky Note

```json
{
  "id": "sticky-{{ID}}",
  "type": "STICKY",
  "x": {{X_POS}},
  "y": {{Y_POS}},
  "width": 200,
  "height": 200,
  "fills": [
    {
      "type": "SOLID",
      "color": {
        "r": {{R}},
        "g": {{G}},
        "b": {{B}}
      }
    }
  ],
  "text": "{{CONTENT}}",
  "fontSize": 24,
  "fontFamily": "{{BRAND_FONT}}",
  "fontWeight": 400,
  "textAlign": "CENTER"
}
```

### Text Box (Headers/Labels)

```json
{
  "id": "text-{{ID}}",
  "type": "TEXT",
  "x": {{X_POS}},
  "y": {{Y_POS}},
  "width": 400,
  "height": "AUTO",
  "text": "{{CONTENT}}",
  "fontSize": 48,
  "fontFamily": "{{BRAND_FONT}}",
  "fontWeight": 700,
  "fills": [
    {
      "type": "SOLID",
      "color": {"r": {{R}}, "g": {{G}}, "b": {{B}}}
    }
  ]
}
```

### Shape (Rectangles, Circles)

```json
{
  "id": "shape-{{ID}}",
  "type": "RECTANGLE",
  "x": {{X_POS}},
  "y": {{Y_POS}},
  "width": {{WIDTH}},
  "height": {{HEIGHT}},
  "fills": [
    {
      "type": "SOLID",
      "color": {"r": {{R}}, "g": {{G}}, "b": {{B}}},
      "opacity": 0.1
    }
  ],
  "strokes": [
    {
      "type": "SOLID",
      "color": {"r": {{R}}, "g": {{G}}, "b": {{B}}},
      "weight": 3
    }
  ],
  "cornerRadius": {{BRAND_RADIUS}}
}
```

### Connector (Arrow)

```json
{
  "id": "connector-{{ID}}",
  "type": "ARROW",
  "startNode": "{{START_ID}}",
  "endNode": "{{END_ID}}",
  "stroke": {
    "type": "SOLID",
    "color": {"r": {{R}}, "g": {{G}}, "b": {{B}}},
    "weight": 3
  },
  "startArrowType": "NONE",
  "endArrowType": "TRIANGLE"
}
```

## Template: Brainstorm Board

```json
{
  "name": "{{BRAND_NAME}} - Brainstorm Session",
  "version": "1.0",
  "nodes": [
    {
      "id": "header",
      "type": "TEXT",
      "x": 400,
      "y": 100,
      "width": 800,
      "text": "{{TOPIC_TITLE}}",
      "fontSize": 64,
      "fontFamily": "{{BRAND_FONT_HEADING}}",
      "fontWeight": 700,
      "fills": [{"type": "SOLID", "color": "{{PRIMARY_RGB}}"}]
    },
    {
      "id": "section-1",
      "type": "TEXT",
      "x": 200,
      "y": 300,
      "text": "Ideas",
      "fontSize": 36,
      "fontWeight": 600
    },
    {
      "id": "section-2",
      "type": "TEXT",
      "x": 800,
      "y": 300,
      "text": "Questions",
      "fontSize": 36,
      "fontWeight": 600
    },
    {
      "id": "section-3",
      "type": "TEXT",
      "x": 1400,
      "y": 300,
      "text": "Actions",
      "fontSize": 36,
      "fontWeight": 600
    },
    {
      "id": "sticky-template-1",
      "type": "STICKY",
      "x": 200,
      "y": 400,
      "width": 200,
      "height": 200,
      "fills": [{"type": "SOLID", "color": "{{ACCENT_RGB}}"}],
      "text": "Add ideas here...",
      "fontSize": 20
    },
    {
      "id": "sticky-template-2",
      "type": "STICKY",
      "x": 800,
      "y": 400,
      "width": 200,
      "height": 200,
      "fills": [{"type": "SOLID", "color": "{{SECONDARY_RGB}}"}],
      "text": "Add questions...",
      "fontSize": 20
    },
    {
      "id": "sticky-template-3",
      "type": "STICKY",
      "x": 1400,
      "y": 400,
      "width": 200,
      "height": 200,
      "fills": [{"type": "SOLID", "color": "{{PRIMARY_RGB}}"}],
      "text": "Add actions...",
      "fontSize": 20
    }
  ],
  "connectors": []
}
```

## Template: Process Flow

```json
{
  "name": "{{BRAND_NAME}} - Process Flow",
  "version": "1.0",
  "nodes": [
    {
      "id": "title",
      "type": "TEXT",
      "x": 400,
      "y": 100,
      "text": "{{PROCESS_NAME}}",
      "fontSize": 56,
      "fontFamily": "{{BRAND_FONT_HEADING}}",
      "fontWeight": 700
    },
    {
      "id": "step-1",
      "type": "RECTANGLE",
      "x": 200,
      "y": 300,
      "width": 300,
      "height": 200,
      "fills": [{"type": "SOLID", "color": "{{PRIMARY_RGB}}", "opacity": 0.2}],
      "strokes": [{"type": "SOLID", "color": "{{PRIMARY_RGB}}", "weight": 3}],
      "cornerRadius": 16
    },
    {
      "id": "step-1-text",
      "type": "TEXT",
      "x": 220,
      "y": 350,
      "text": "Step 1\n{{STEP_1_DESC}}",
      "fontSize": 24,
      "fontWeight": 600,
      "width": 260
    },
    {
      "id": "step-2",
      "type": "RECTANGLE",
      "x": 600,
      "y": 300,
      "width": 300,
      "height": 200,
      "fills": [{"type": "SOLID", "color": "{{SECONDARY_RGB}}", "opacity": 0.2}],
      "strokes": [{"type": "SOLID", "color": "{{SECONDARY_RGB}}", "weight": 3}],
      "cornerRadius": 16
    },
    {
      "id": "step-2-text",
      "type": "TEXT",
      "x": 620,
      "y": 350,
      "text": "Step 2\n{{STEP_2_DESC}}",
      "fontSize": 24,
      "fontWeight": 600,
      "width": 260
    },
    {
      "id": "step-3",
      "type": "RECTANGLE",
      "x": 1000,
      "y": 300,
      "width": 300,
      "height": 200,
      "fills": [{"type": "SOLID", "color": "{{ACCENT_RGB}}", "opacity": 0.2}],
      "strokes": [{"type": "SOLID", "color": "{{ACCENT_RGB}}", "weight": 3}],
      "cornerRadius": 16
    },
    {
      "id": "step-3-text",
      "type": "TEXT",
      "x": 1020,
      "y": 350,
      "text": "Step 3\n{{STEP_3_DESC}}",
      "fontSize": 24,
      "fontWeight": 600,
      "width": 260
    }
  ],
  "connectors": [
    {
      "id": "arrow-1-2",
      "type": "ARROW",
      "startNode": "step-1",
      "endNode": "step-2",
      "stroke": {"type": "SOLID", "color": "{{PRIMARY_RGB}}", "weight": 4}
    },
    {
      "id": "arrow-2-3",
      "type": "ARROW",
      "startNode": "step-2",
      "endNode": "step-3",
      "stroke": {"type": "SOLID", "color": "{{SECONDARY_RGB}}", "weight": 4}
    }
  ]
}
```

## Template: Workshop Board

```json
{
  "name": "{{BRAND_NAME}} - Workshop",
  "version": "1.0",
  "nodes": [
    {
      "id": "header",
      "type": "TEXT",
      "x": 100,
      "y": 50,
      "text": "🎯 {{WORKSHOP_GOAL}}",
      "fontSize": 48,
      "fontWeight": 700
    },
    {
      "id": "timer-section",
      "type": "RECTANGLE",
      "x": 1400,
      "y": 50,
      "width": 250,
      "height": 100,
      "fills": [{"type": "SOLID", "color": "{{ACCENT_RGB}}", "opacity": 0.3}],
      "cornerRadius": 12
    },
    {
      "id": "timer-text",
      "type": "TEXT",
      "x": 1420,
      "y": 70,
      "text": "⏱️ Time: {{DURATION}} min",
      "fontSize": 28,
      "fontWeight": 600
    },
    {
      "id": "section-1-bg",
      "type": "RECTANGLE",
      "x": 100,
      "y": 200,
      "width": 500,
      "height": 600,
      "fills": [{"type": "SOLID", "color": {"r": 0.95, "g": 0.95, "b": 0.95}}],
      "cornerRadius": 16
    },
    {
      "id": "section-1-title",
      "type": "TEXT",
      "x": 120,
      "y": 220,
      "text": "Section 1: Ideate",
      "fontSize": 32,
      "fontWeight": 700,
      "fills": [{"type": "SOLID", "color": "{{PRIMARY_RGB}}"}]
    },
    {
      "id": "section-2-bg",
      "type": "RECTANGLE",
      "x": 650,
      "y": 200,
      "width": 500,
      "height": 600,
      "fills": [{"type": "SOLID", "color": {"r": 0.95, "g": 0.95, "b": 0.95}}],
      "cornerRadius": 16
    },
    {
      "id": "section-2-title",
      "type": "TEXT",
      "x": 670,
      "y": 220,
      "text": "Section 2: Prioritize",
      "fontSize": 32,
      "fontWeight": 700,
      "fills": [{"type": "SOLID", "color": "{{SECONDARY_RGB}}"}]
    },
    {
      "id": "section-3-bg",
      "type": "RECTANGLE",
      "x": 1200,
      "y": 200,
      "width": 500,
      "height": 600,
      "fills": [{"type": "SOLID", "color": {"r": 0.95, "g": 0.95, "b": 0.95}}],
      "cornerRadius": 16
    },
    {
      "id": "section-3-title",
      "type": "TEXT",
      "x": 1220,
      "y": 220,
      "text": "Section 3: Action Plan",
      "fontSize": 32,
      "fontWeight": 700,
      "fills": [{"type": "SOLID", "color": "{{ACCENT_RGB}}"}]
    }
  ]
}
```

## Color Conversion Helper

FigJam uses RGB 0-1 scale. Convert HEX to FigJam RGB:

```python
def hex_to_figjam_rgb(hex_color):
    """Convert #FF5733 to {"r": 1.0, "g": 0.34, "b": 0.2}"""
    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16) / 255
    g = int(hex_color[2:4], 16) / 255
    b = int(hex_color[4:6], 16) / 255
    return {"r": round(r, 2), "g": round(g, 2), "b": round(b, 2)}
```

## Layout Positioning System

Use grid-based positioning for consistency:

```python
GRID_SIZE = 50
STICKY_SIZE = 200
CARD_WIDTH = 300
CARD_HEIGHT = 200

def grid_position(col, row):
    """Convert grid coordinates to pixel position"""
    return {
        "x": col * (STICKY_SIZE + GRID_SIZE),
        "y": row * (STICKY_SIZE + GRID_SIZE)
    }

# Example: place sticky in column 2, row 3
pos = grid_position(2, 3)  # {"x": 500, "y": 750}
```

## Export Instructions

### To FigJam

1. Generate JSON file with .figjam extension
2. In FigJam: File → Import → Select .figjam file
3. Board will be created with all nodes and styling

### Alternative: Manual Recreation

If direct import is not supported:

1. Generate HTML visualization of the board layout
2. Provide structured markdown with:
   - Board structure
   - Element positions
   - Content for each element
   - Connection instructions
3. User recreates in FigJam using instructions

## HTML Preview Generation

For immediate viewing before FigJam import:

```html
<!DOCTYPE html>
<html>
<head>
    <title>FigJam Board Preview</title>
    <style>
        body { background: #f0f0f0; margin: 0; padding: 20px; }
        .board { 
            background: white; 
            min-width: 1920px; 
            min-height: 1080px; 
            position: relative;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        .sticky {
            position: absolute;
            width: 200px;
            height: 200px;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.15);
            font-size: 16px;
        }
        .arrow {
            position: absolute;
            border: 2px solid;
            pointer-events: none;
        }
    </style>
</head>
<body>
    <div class="board">
        <!-- Rendered nodes here -->
    </div>
</body>
</html>
```

## Usage in Skill

1. User selects FigJam board type
2. Load corresponding template
3. Inject brand colors (convert HEX → RGB 0-1)
4. Position elements on grid
5. Add connectors between related elements
6. Generate .figjam JSON file
7. Generate HTML preview
8. Provide both files to user with import instructions
