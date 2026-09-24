"""Inline Markdown -> Word runs: bold, italic, bold-italic, code, math ($..$, $$..$$), links,
Unicode superscript digits.

Links keep their visible label only (no hyperlink object). Set CODE_FONT from the build script to
give `code` spans a monospace face; None leaves them in the paragraph's own font.
"""

import re

from .math_omml import insert_formula

CODE_FONT = None

PATTERNS = [
    ('bold_italic', re.compile(r'\*\*\*(.+?)\*\*\*')),
    ('bold',        re.compile(r'\*\*(.+?)\*\*')),
    ('italic',      re.compile(r'(?<!\*)\*([^*]+?)\*(?!\*)')),
    # _text_ only when not glued to word characters, so snake_case and subscripts survive
    ('italic',      re.compile(r'(?<!\w)_([^_\n]+?)_(?!\w)', re.UNICODE)),
    ('code',        re.compile(r'`([^`]+?)`')),
    ('math_display', re.compile(r'\$\$(.+?)\$\$')),
    # $..$ is math unless it opens on a digit: $200 and $0.39 are money
    ('math_inline', re.compile(r'(?<!\$)\$(?!\d)((?:[^$\\]|\\.)+?)\$(?!\$)')),
    ('link_angle',  re.compile(r'<((?:https?://|mailto:)[^>]+)>')),
    ('link_md',     re.compile(r'\[([^\]]+)\]\(([^)]+)\)')),
    # author and affiliation marks written as Unicode digits become real superscript runs
    ('superscript', re.compile(r'([⁰¹²³⁴⁵⁶⁷⁸⁹]+)')),
]
_SUP_DIGITS = str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹', '0123456789')


def _run(para, text, bold, italic, force_not_bold):
    run = para.add_run(text)
    if force_not_bold:
        run.bold = False
    elif bold:
        run.bold = True
    if italic:
        run.italic = True
    return run


def add_inline_runs(para, text, bold=False, italic=False,
                    force_not_bold=False, suppress_bold=False, suppress_italic=False):
    """Append text to para, turning Markdown emphasis, code, math and links into runs.

    suppress_bold / suppress_italic drop that emphasis (for styles that are already bold or
    italic); force_not_bold writes runs with bold explicitly off (for a bold lead-in prefix).
    """
    if not text:
        return

    best = kind = None
    start = len(text)
    for k, pattern in PATTERNS:
        m = pattern.search(text)
        if m and m.start() < start:
            best, kind, start = m, k, m.start()

    if best is None:
        _run(para, text, bold, italic, force_not_bold)
        return

    kw = dict(force_not_bold=force_not_bold, suppress_bold=suppress_bold,
              suppress_italic=suppress_italic)
    if start > 0:
        add_inline_runs(para, text[:start], bold=bold, italic=italic, **kw)

    inner = best.group(1)
    if kind == 'bold_italic':
        add_inline_runs(para, inner, bold=not suppress_bold, italic=not suppress_italic, **kw)
    elif kind == 'bold':
        add_inline_runs(para, inner, bold=not suppress_bold, italic=italic, **kw)
    elif kind == 'italic':
        add_inline_runs(para, inner, bold=bold, italic=not suppress_italic, **kw)
    elif kind == 'code':
        run = para.add_run(inner)
        if CODE_FONT:
            run.font.name = CODE_FONT
    elif kind in ('math_display', 'math_inline'):
        insert_formula(para, inner, display=(kind == 'math_display'))
    elif kind == 'superscript':
        _run(para, inner.translate(_SUP_DIGITS), bold, italic, force_not_bold).font.superscript = True
    else:                                                    # link_angle, link_md
        _run(para, inner, bold, italic, force_not_bold)

    rest = text[best.end():]
    if rest:
        add_inline_runs(para, rest, bold=bold, italic=italic, **kw)
