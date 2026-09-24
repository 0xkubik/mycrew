---
name: docx-verify
description: "Use when a built .docx must be proven correct — its structure against the Markdown source and its pages by eye. Reports every defect with its page; fixes nothing."
argument-hint: "<out.docx> [source article.md]"
---

# docx-verify — prove a Word document is right, by structure and by eye

Runs the structural check, renders the pages to images, looks at every page, and reports what is
wrong and where. Works on any .docx. Comes back with a defect list; the fixing is the caller's.

## Steps

### 1. Run the structural check

- `python check.py out.docx --md article.md` from this skill's folder; add `--placeholders TEXT ...`
  for template leftovers you know of (a sample author's name). Needs python-docx.
- Read every line. ERRORs (a picture or diagram missing, no native equations when the source has
  formulas, a picture wider than the text) must be fixed. Judge each WARN: leaked Markdown, text
  left in the default style, empty runs, a dropped-content word count. A journal's volume number
  left as "XX" is a real defect only if the human already has the number.

### 2. Render the pages

- `python render.py out.docx renders/` from this skill's folder. It tries LibreOffice first, then
  a macOS Quick Look thumbnail. Quick Look shows the first page only: say so in the report, and
  ask the human either to install LibreOffice or to allow `--backend word`.
- `--backend word` renders through Word for Mac and gives the true layout, but it opens Word on the
  person's screen and may ask for file access. Never run it without their go-ahead.

### 3. Look at every page image

- Read each PNG. For each page note: text clipped or overflowing; fonts and sizes off from the
  template; a heading stranded at the page bottom; a table cut or wider than the text; a figure
  too big, too small or missing; a caption detached from its figure; a formula shown as plain
  italic text; header, footer and page number wrong for odd and even pages; a blank page.
- Text inside a figure printing under about 8 pt at its printed width: measure it on the page, not
  on the PNG.
- After a full rebuild look at every page; after a point fix, at the changed pages and their
  neighbours. The report says which.
- Compare the title page with the venue's filled example first, then with the template's own sample
  rendered the same way. Written requirements outrank the sample; the sample wins on styles.

### 4. Report

- One line per defect: page, what is wrong, and whether the fix belongs in the build script or in
  the source text. Group repeats. Say plainly which pages were not looked at and why.
- Count the pages against the limit. Over it: say by how many lines and where a cut actually
  helps; a cut before a figure that then moves to the next page does not.

## Done

- **Every page was looked at, or the report says exactly which were not** and what would allow it.
- **The caller gets a defect list with pages,** and no file has been changed.
