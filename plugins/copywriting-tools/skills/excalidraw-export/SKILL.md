---
name: excalidraw-export
description: "Use when Excalidraw diagrams (.excalidraw) must become PNG files for a document, in the venue's font and at a legible size. Exports with Excalidraw's own renderer and warns when a diagram's text would print too small."
argument-hint: "[files] [--font ...] [--print-width-cm N]"
---

# excalidraw-export — export diagrams to PNG in the venue's font

Renders each .excalidraw file with Excalidraw's own renderer in headless Chromium, swaps the typeface
for the venue's, and writes PNGs. Comes back with the PNG paths and a warning for every diagram whose
smallest text would print under the legibility floor. Stops at the PNG: placing it in the document is
the build's job.

## Steps

### 1. Set up the tools

- In the article repo's venv install `requirements.txt` from this skill's folder, then run
  `python -m playwright install chromium`. The first run loads Excalidraw from a CDN, so it needs the
  network. Copy `excalidraw_to_png.py` into `scripts/` (the layouter's folder in a repo made by
  `/article-init`).

### 2. Read the venue's rule for figures

- Find what the requirements say about text in figures: the typeface (Times New Roman when they are
  silent), the minimum size, the printed width. Pass them as `--font` and `--print-width-cm`.

### 3. Export

- `python scripts/excalidraw_to_png.py` reads `media/excalidraw/*.excalidraw` and writes
  `media/png/<name>.png` at 3 times scale, about 300 dpi at print width. Name files to export only
  some. Make the root Makefile's `png` target call it.
- Excalidraw ships no Times New Roman, so the script exports SVG, swaps the font and rasterizes.
  Never multiply the scale by the device pixel ratio yourself: Excalidraw already does, and the
  picture comes out nine times too large.

### 4. Look at the result

- Open each PNG beside its source: nothing clipped, every label still inside its box after the font
  swap. Act on a size warning by enlarging the text in the source, or by cutting the diagram's
  content: the printed size is what the reader sees, not the size on the canvas.

## Done

- **Every diagram has a PNG in `media/png/`,** looked at, with no size warning left.
- **The report:** the files written, the font and print width used, and any diagram that had to change.
