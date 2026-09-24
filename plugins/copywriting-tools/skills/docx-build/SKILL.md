---
name: docx-build
description: "Use when an article's Markdown must become a Word document in a specific template. Writes that repo's own converter script on top of shared modules, builds it, and hands it to docx-verify until the result is clean."
argument-hint: "<article.md> <template.docx> [requirements document]"
---

# docx-build — write the converter for one template, then prove it renders

There is no universal converter. Each article repo gets its own build script, written for its own
template out of the reusable modules in this skill's `docgen/` folder. Comes back with a script that
rebuilds the document from a clean checkout and a clean docx-verify report.

## Steps

### 1. Set up the tools

- In the article repo make a venv (`python3 -m venv .venv`, ignored by git) and install
  `requirements.txt` from this skill's folder. Copy this skill's `docgen/` folder into `scripts/`
  (the layouter's folder in a repo made by `/article-init`; create it if absent): the repo keeps
  its own copy and stays self-contained.
- Note what the machine has: Word.app (its `mathml2omml.xsl` gives native equations; without it
  formulas degrade to plain italic text) and `mmdc` (Mermaid diagrams). Say what is missing.

### 2. Read the template

- Run `inspect_template.py <template.docx>` (the repo's root `template.docx`; the venue's own files
  are in `docs/`) from this skill's folder. Ask for the detail of any
  candidate style with `--style NAME ...` and pick styles by what they do, not by their names.
- Read any formatting requirements the venue supplied. Sources rank: the venue's filled example,
  its written rules, the template's sample, a blank form; the sample wins alone on styles. Where
  the template's own sample body says which style a piece uses, trust it, and copy what it shows: the empty spacer paragraphs between
  blocks, and a first run written bold or italic (an abstract label, a references heading).
  Write the mapping down: title, authors, abstract, keywords, headings 1-3, body, list, quote,
  code, table font and width, figure and table captions, references, header and footer text
  (clear leftover template notes), page numbers.

### 3. Read how the Markdown is written

- Frontmatter keys, the title-page order (title, authors, abstract, keywords), caption prefixes,
  reference format, formulas, images, Mermaid blocks. The title-page phases of the script follow
  this article's real layout, so look at the source before writing them.
- A form the template carries, like a registration form, is an appendix: keep its data in
  `resources/` and fill it in the converter. Find out from the requirements whether it counts
  toward the page limit.

### 4. Write `scripts/build_docx.py`

- Import `docgen` for everything generic (parsing, inline runs with superscript marks, formulas,
  tables, pictures, page numbers, headers, and `typo()` for no-break spaces after labels and
  initials). Put the style names and every template-specific rule in the script itself:
  constants on top, one function per block kind, a CLI with `--input --template --output`. The
  document is written to `article.docx` in the repo root.
- `example/ispras_build.py` and `example/saec_build.py` show the shape for two different
  templates; write the new script fresh from step 2's mapping and never edit an example. A block
  kind the template has no rule for must stop the build with a clear message, never be dropped.
  Set `docgen.math_omml.FONT` / `SIZE_PT` and `docgen.inline.CODE_FONT` to the template's. When
  something generic is missing from `docgen`, add it to the repo's copy in the same style and name
  it in the report so it can be brought back to the skill.

### 5. Build, check, repeat

- Run the script, then run the docx-verify skill on the result (structure check, render, look at
  every page). Fix the script for defects in the conversion. A defect in the source text is
  reported, never edited: the words belong to the author.
- Repeat until docx-verify reports no ERROR and every page looks right. If a round changes nothing,
  stop and report what is stuck instead of looping.

### 6. Leave it reproducible

- Add `scripts/requirements.txt` and fill the root Makefile's `docx` target so `make docx` writes
  `article.docx` into the root (`/article-init` leaves the target empty; create the Makefile if it
  is absent). Make sure `.venv` and `__pycache__` are in `.gitignore`. Pictures the article needs
  (exported diagrams in `media/png/`, made by the excalidraw-export skill) must exist before the
  build; say so in the Makefile.

## Done

- **The document builds from a clean checkout** with `make docx`, and docx-verify has no ERROR.
- **The report to the caller:** the style mapping used, what is still open (template placeholders
  the human must fill, missing pictures), what was added to `docgen`, and what could not be checked.
