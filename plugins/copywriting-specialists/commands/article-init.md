---
description: "Use once to found an article — ask where it will be published, the tone and the final file, take the context the agents need, create the folders (docs, media, resources, scripts), the optional template and article.md, write it all into CLAUDE.md, and git init. Stops before the first commit so the human can look."
argument-hint: "[article name]"
---

# /article-init — found the article

Turn the folder into the **article repository** — everything about one article in one place: the text,
what the venue requires, the media, the material behind it, and the scripts the layouter writes.
One-shot. You **never commit**: the run ends with everything written and the human free to look.

## Steps

1. **Ask the setup questions first, via `AskUserQuestion`, in one batch, before writing anything.**
   - **Where will it be published?** — a journal, a conference, a platform (Habr, a blog), a thesis.
     The venue's name comes with the answer.
   - **Which tone?** — scientific (the `tone-scientific` guide), conversational (`tone-conversational`),
     or something else in the human's own words.
   - **Which final file?** — docx, md, pdf, or another. Docx means a template and a build; md means
     `article.md` is the artifact and nothing is built.
   - **The article's name** — the argument, else the folder's name, unless the human says otherwise.
2. **Give the human the floor.** In plain words, invite a few short lines about the article and
   anything the agents must know: the topic, co-authors, the deadline, what must not be said, where the
   source material is. Also ask for the paths of any files they already have — the venue's
   requirements, a template, sources. Nothing is a valid answer; never invent context. Keep what they
   say in their own words.
3. **Create the layout** — a folder or file already there is left as is:
   - **`article.md`** in the root, with the article's name as its one heading and nothing else.
   - **`docs/`** — everything the venue or publisher supplied: requirements, limits, formatting rules,
     call-for-papers letters, templates as issued.
   - **`media/`** — figures and other media, each format in its own subfolder: `media/excalidraw/` for
     sources, `media/png/` for exports. A subfolder appears with its first file, not before.
   - **`resources/`** — helper material for writing: theses, research notes, references, sources.
   - **`scripts/`** — the layouter's workshop, empty at the start. Every script that turns one thing
     into another lives here and writes where the output belongs: the Word build writes `article.docx`
     into the root, the diagram export writes into `media/png/`.
   - **`template.docx`** in the root — only when the final file is docx and the human has a template.
     A template that is not .docx stays in `docs/` as issued; say a .docx copy is needed. No template
     yet: leave it out and say so.
   - A `.gitkeep` in each empty folder, so the structure survives git.
4. **Bring in what the human already has.** Copy, never move, never edit: requirements and limits into
   `docs/`, the template to the root, material for writing into `resources/`. Say where each file went.
5. **Write the root `CLAUDE.md`** to the template below, from their answers and their words.
6. **`git init`**, unless the folder is already a repository, and a `.gitignore` with `.DS_Store`,
   `.venv/`, `__pycache__/`, `node_modules/` and `~$*`.
7. **Then stop.** No `git add`, no commit. Say what you created and what is still open — a template to
   add, requirements to drop into `docs/` — and name the team that takes it from here: the
   copywriter writes, the reviewer checks, the layouter builds.

## The root CLAUDE.md — the template

```markdown
# <article name>

## About
<what the article says, in a few lines, in the human's own words>

## Publication
- **Where:** <the venue or platform; its requirements are in docs/>
- **Tone:** <scientific | conversational | the human's words> — <the matching tone guide, if any>
- **Final file:** <docx | md | pdf | ...> — <docx: built into the root as article.docx | md: article.md is the artifact>

## For the agents
<what the human said matters: co-authors, deadline, what must not be said, where the source material
is — or "nothing given">

## Layout
- `article.md` — the article.
- `template.docx` — the Word template the build follows. <Only when the final file is docx.>
- `docs/` — what the venue supplied: requirements and limits. Read before writing or building.
- `media/<format>/` — figures, one folder per format: `excalidraw/` sources, `png/` exports.
- `resources/` — material for writing: theses, research, references.
- `scripts/` — the layouter's scripts. Outputs land where they belong: `article.docx` in the root,
  exported diagrams in `media/png/`.
```
