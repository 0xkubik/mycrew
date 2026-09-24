#!/usr/bin/env python3
"""Export .excalidraw files to PNG with Excalidraw's own renderer, text set in the venue's font.

    python scripts/excalidraw_to_png.py [files...] [--src media/excalidraw] [--out media/png]
                                        [--font "'Times New Roman', Times, serif"] [--scale 3]
                                        [--print-width-cm 12] [--min-pt 8]

Runs headless Chromium (Playwright) and Excalidraw's exportToSvg, loaded from esm.sh, so it needs the
network on first load. Excalidraw ships no Times New Roman, so the SVG's text is switched to --font
and that is rasterized. Paths are relative to the current folder. Warns when the smallest text in a
diagram would print under --min-pt at --print-width-cm wide.
"""

import argparse
import json
import pathlib
import sys

from playwright.sync_api import sync_playwright

PT_PER_CM = 28.35

# ponytail: library pinned via CDN; vendor it locally if builds must run offline.
PAGE = """<!doctype html><meta charset="utf-8">
<style>body{margin:0;background:#fff} svg{display:block}</style>
<div id="out"></div>
<script type="module">
import { exportToSvg } from 'https://esm.sh/@excalidraw/excalidraw@0.18.0?bundle&deps=react@18.3.1,react-dom@18.3.1';
window.render = async (scene, font, scale) => {
  const svg = await exportToSvg({
    elements: scene.elements.filter(e => !e.isDeleted),
    appState: { ...(scene.appState || {}), exportBackground: true, viewBackgroundColor: '#ffffff' },
    files: scene.files || {},
    skipInliningFonts: true,
  });
  svg.querySelectorAll('text').forEach(t => t.setAttribute('font-family', font));
  // Scale through the SVG's own size at devicePixelRatio 1: Excalidraw multiplies by the ratio itself.
  for (const k of ['width', 'height']) svg.setAttribute(k, svg.getAttribute(k) * scale);
  document.getElementById('out').replaceChildren(svg);
  await document.fonts.ready;
};
window.ready = true;
</script>"""


def smallest_text_pt(scene, print_cm):
    """Printed size in points of the smallest text, if the diagram is printed print_cm wide."""
    els = [e for e in scene['elements'] if not e.get('isDeleted')]
    sizes = [e['fontSize'] for e in els if e.get('type') == 'text' and e.get('fontSize')]
    if not sizes:
        return None
    width = max(e['x'] + e.get('width', 0) for e in els) - min(e['x'] for e in els)
    return min(sizes) * print_cm / max(width, 1) * PT_PER_CM


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('files', nargs='*', type=pathlib.Path)
    ap.add_argument('--src', type=pathlib.Path, default=pathlib.Path('media/excalidraw'))
    ap.add_argument('--out', type=pathlib.Path, default=pathlib.Path('media/png'))
    ap.add_argument('--font', default="'Times New Roman', Times, serif")
    ap.add_argument('--scale', type=float, default=3, help='pixel multiplier (3 is about 300 dpi at print width)')
    ap.add_argument('--print-width-cm', type=float, default=12)
    ap.add_argument('--min-pt', type=float, default=8)
    args = ap.parse_args()

    files = args.files or sorted(args.src.glob('*.excalidraw'))
    if not files:
        sys.exit(f'no .excalidraw files in {args.src}')
    args.out.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page()
        page.on('pageerror', lambda e: print(f'page error: {e}', file=sys.stderr))
        page.set_content(PAGE)
        page.wait_for_function('window.ready === true', timeout=120_000)
        for f in files:
            scene = json.loads(f.read_text(encoding='utf-8'))
            page.evaluate('([s, f, k]) => render(s, f, k)', [scene, args.font, args.scale])
            png = page.locator('#out svg').screenshot()
            out = args.out / (f.stem + '.png')
            out.write_bytes(png)
            print(f'{f} -> {out} ({len(png) // 1024} KB)')
            pt = smallest_text_pt(scene, args.print_width_cm)
            if pt is not None and pt < args.min_pt:
                print(f'WARN {f.name}: smallest text prints at about {pt:.1f} pt at {args.print_width_cm} cm wide, '
                      f'under {args.min_pt} pt: enlarge the text in the source', file=sys.stderr)
        browser.close()


if __name__ == '__main__':
    main()
