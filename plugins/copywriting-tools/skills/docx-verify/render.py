#!/usr/bin/env python3
"""Render a .docx to page images so its layout can be looked at.

    python render.py file.docx outdir [--dpi 90] [--backend auto|soffice|word|quicklook]

Backends, in the order auto tries them:
  soffice    LibreOffice headless -> PDF -> pdftoppm PNGs. Every page. Needs LibreOffice and poppler.
  quicklook  macOS Quick Look thumbnail. FIRST PAGE ONLY, but needs nothing installed.
  word       Word for Mac through AppleScript -> PDF -> PNGs. Every page, true Word layout. Never picked
             by auto: it opens Word on the person's screen and may ask for file access. Name it explicitly.
Prints one PNG path per page. The first line says which backend produced them and whether it is partial.
"""

import argparse
import glob
import os
import shutil
import subprocess
import sys


def soffice_path():
    for c in (shutil.which('soffice'), shutil.which('libreoffice'),
              '/Applications/LibreOffice.app/Contents/MacOS/soffice'):
        if c and os.path.exists(c):
            return c
    return None


def pdf_to_pngs(pdf, outdir, dpi):
    if not shutil.which('pdftoppm'):
        sys.exit('pdftoppm not found (install poppler: brew install poppler); the PDF is at ' + pdf)
    prefix = os.path.join(outdir, 'page')
    subprocess.run(['pdftoppm', '-r', str(dpi), '-png', pdf, prefix], check=True)
    return sorted(glob.glob(prefix + '-*.png'))


def via_soffice(docx, outdir, dpi):
    exe = soffice_path()
    if not exe:
        return None
    subprocess.run([exe, '--headless', '--convert-to', 'pdf', '--outdir', outdir, docx],
                   check=True, capture_output=True, timeout=180)
    pdf = os.path.join(outdir, os.path.splitext(os.path.basename(docx))[0] + '.pdf')
    return pdf_to_pngs(pdf, outdir, dpi) if os.path.exists(pdf) else None


def via_word(docx, outdir, dpi):
    pdf = os.path.join(outdir, os.path.splitext(os.path.basename(docx))[0] + '.pdf')
    script = f'''
tell application "Microsoft Word"
    open POSIX file "{os.path.abspath(docx)}"
    set d to active document
    save as d file name "{os.path.abspath(pdf)}" file format format PDF
    close d saving no
end tell'''
    subprocess.run(['osascript', '-e', script], check=True, timeout=180)
    return pdf_to_pngs(pdf, outdir, dpi) if os.path.exists(pdf) else None


def via_quicklook(docx, outdir, dpi):
    if not shutil.which('qlmanage'):
        return None
    subprocess.run(['qlmanage', '-t', '-s', str(int(dpi * 11)), '-o', outdir, docx],
                   check=True, capture_output=True, timeout=120)
    return sorted(glob.glob(os.path.join(outdir, os.path.basename(docx) + '.png')))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('docx')
    ap.add_argument('outdir')
    ap.add_argument('--dpi', type=int, default=90)
    ap.add_argument('--backend', default='auto', choices=['auto', 'soffice', 'word', 'quicklook'])
    args = ap.parse_args()
    os.makedirs(args.outdir, exist_ok=True)

    order = {'auto': ['soffice', 'quicklook']}.get(args.backend, [args.backend])
    tools = {'soffice': via_soffice, 'word': via_word, 'quicklook': via_quicklook}
    for name in order:
        try:
            pages = tools[name](args.docx, args.outdir, args.dpi)
        except (subprocess.SubprocessError, OSError) as e:
            print(f'{name} failed: {e}', file=sys.stderr)
            continue
        if pages:
            note = ' (FIRST PAGE ONLY - the rest of the layout is unchecked)' if name == 'quicklook' else ''
            print(f'backend: {name}, {len(pages)} page image(s){note}')
            print('\n'.join(pages))
            return
    sys.exit('no rendering backend worked: install LibreOffice (brew install --cask libreoffice), '
             'or name --backend word to render through Word')


if __name__ == '__main__':
    main()
