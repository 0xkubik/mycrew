---
name: rename
description: "Use when the human asks to rename or replace something across the repo — a variable, function, file, term — that shows up in more than a couple of places. Runs one regex search-and-replace over the whole scope instead of editing every file by hand."
argument-hint: "<old pattern> -> <new pattern> [scope: path or glob]"
---

# rename — rewrite a pattern across the repo with one command

Replaces every occurrence of a pattern with its replacement in a single regex pass over the given
scope, so a rename never turns into file-by-file manual edits. Ends with the old pattern gone and
the command that did it reported.

## Steps

### 1. Pin the pattern, the replacement, and the scope

Exact regex (or literal string), what it becomes, and where — whole repo or a path/glob. Ambiguous
case (identifier only, or also comments, strings, docs? does it need
camelCase/PascalCase/snake_case/kebab-case variants too?) → ask before running anything.

### 2. Preview before touching a file

`rg -n '<pattern>' <scope>` — show the human the match count and a few sample lines. A pattern that
also catches something unintended gets tightened here, before any file changes.

### 3. Run one command

Prefer an already-installed rename tool if the repo has one (`sd`, `fastmod`); otherwise `rg -l
'<pattern>' <scope> | xargs sed -i '' -E 's/<pattern>/<replacement>/g'` (drop the `''` on Linux).
One command over the whole scope — never a loop of per-file Edit calls.

### 4. Verify

Re-run the same search — it should come back empty, or only match the deliberate exclusions. Run the
project's build or tests if either exists, since a regex rename can silently catch a partial match.

## Done

- **The old pattern is gone from scope**, confirmed by re-running the search, not by memory of which
  files were touched.
- **One command did the rewrite** — report the command used, files touched, and match count, not a
  file-by-file diff walk.
