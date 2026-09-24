"""Markdown -> blocks. Knows nothing about any Word template.

parse_md(path) returns (meta, blocks). meta is the YAML frontmatter dict. Every block is a tuple:
  ('heading', level, text)      ('paragraph', text)         ('list', ordered, [item, ...])
  ('code_block', lang, code)    ('table', [row line, ...])  ('blockquote', text)
  ('math_block', latex)         ('image', alt, path)        ('hr', '')      ('empty', '')
"""

import re
import sys

import yaml

_HR = re.compile(r'^---+\s*$')
_LIST_ITEM = re.compile(r'^(?:[-*+]|\d+[.)])\s+')
_IMAGE = re.compile(r'^!\[([^\]]*)\]\(([^)]+)\)\s*$')


def parse_frontmatter(lines):
    """Split a leading ---YAML--- block off. Returns (meta_dict, remaining_lines)."""
    if not lines or lines[0].rstrip() != '---':
        return {}, lines
    end = next((i for i in range(1, len(lines)) if lines[i].rstrip() == '---'), None)
    if end is None:
        return {}, lines
    try:
        meta = yaml.safe_load(''.join(lines[1:end])) or {}
    except yaml.YAMLError as e:
        print(f"warning: YAML frontmatter parse error: {e}", file=sys.stderr)
        meta = {}
    return meta, lines[end + 1:]


def _starts_new_block(line):
    return (not line.strip() or line.startswith(('#', '```', '|', '>', '$$'))
            or bool(_HR.match(line)) or bool(_LIST_ITEM.match(line)))


def _math_block(lines, i, n):
    """A $$ block opened at lines[i]. Returns (formula, next_index)."""
    first = lines[i].rstrip('\n').strip()
    if first.endswith('$$') and len(first) > 4:                      # $$formula$$ on one line
        return first[2:-2].strip(), i + 1
    body = [first[2:].strip()] if first != '$$' else []
    i += 1
    while i < n:
        line = lines[i].rstrip('\n')
        if line.strip() == '$$':
            break
        if line.endswith('$$') and len(line) > 2:                    # closing $$ glued to the last line
            body.append(line[:-2].strip())
            break
        body.append(line)
        i += 1
    return '\n'.join(l for l in body if l).strip(), i + 1


def parse_md(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        meta, lines = parse_frontmatter(f.readlines())

    blocks, i, n = [], 0, len(lines)
    while i < n:
        line = lines[i].rstrip('\n')

        if _HR.match(line):
            blocks.append(('hr', ''))
            i += 1
            continue

        m = re.match(r'^(#{1,6})\s+(.+)$', line)
        if m:
            blocks.append(('heading', len(m.group(1)), m.group(2).strip()))
            i += 1
            continue

        if line.startswith('```'):
            lang, code = line[3:].strip(), []
            i += 1
            while i < n and not lines[i].startswith('```'):
                code.append(lines[i].rstrip('\n'))
                i += 1
            blocks.append(('code_block', lang, '\n'.join(code)))
            i += 1
            continue

        if line.startswith('|') and '|' in line[1:]:
            rows = []
            while i < n and lines[i].startswith('|'):
                rows.append(lines[i].rstrip('\n'))
                i += 1
            blocks.append(('table', rows))
            continue

        if line.startswith('>'):
            quote = []
            while i < n and lines[i].startswith('>'):
                quote.append(re.sub(r'^>\s?', '', lines[i].rstrip('\n')))
                i += 1
            blocks.append(('blockquote', '\n'.join(quote)))
            continue

        if line.startswith('$$'):
            formula, i = _math_block(lines, i, n)
            if formula:
                blocks.append(('math_block', formula))
            continue

        if not line.strip():
            blocks.append(('empty', ''))
            i += 1
            continue

        if _LIST_ITEM.match(line):
            ordered, items = bool(re.match(r'^\d', line)), []
            while i < n and _LIST_ITEM.match(lines[i].rstrip('\n')):
                item = [_LIST_ITEM.sub('', lines[i].rstrip('\n'))]
                i += 1
                while i < n and lines[i].startswith((' ', '\t')) and lines[i].strip():
                    item.append(lines[i].strip())                     # wrapped continuation
                    i += 1
                items.append(' '.join(item))
            blocks.append(('list', ordered, items))
            continue

        para = [line]
        i += 1
        while i < n and not _starts_new_block(lines[i].rstrip('\n')):
            para.append(lines[i].rstrip('\n'))
            i += 1
        text = '\n'.join(para)
        img = _IMAGE.match(text.strip())
        blocks.append(('image', img.group(1).strip(), img.group(2).strip()) if img else ('paragraph', text))

    return meta, blocks
