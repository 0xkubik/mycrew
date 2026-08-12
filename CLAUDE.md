# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A Claude Code **plugin marketplace** named `mycrew` — a five-layer harness made almost entirely of
prompts. Everything here is markdown (skills, commands, agents, rules) plus JSON manifests; the only
executable is one bash script. There is no build, no test suite, no dependencies, no language runtime.
Editing this repo means editing instructions that *other* Claude instances load and obey.

## Layout

| Path | What loads it |
| --- | --- |
| `.claude-plugin/marketplace.json` | the marketplace itself — lists all five plugins and their `source` paths |
| `plugins/<name>/.claude-plugin/plugin.json` | per-plugin manifest; its `version` is what ships changes |
| `plugins/<name>/commands/*.md` | slash commands — `/chief`, `/worker`, `/setup`, `/product-init` |
| `plugins/<name>/skills/<skill>/SKILL.md` | skills, invoked as `<plugin>:<skill>` (e.g. `mycrew-pipeline:do`) |
| `plugins/mycrew-worker/agents/worker.md` | the `worker` subagent type the chief spawns |
| `plugins/mycrew-tools/rules/*.md` | rule files shipped for copying into a consumer project's `.claude/rules/` |

## The five layers

Each layer builds on the one below; a layer only ever drives the layer beneath it.

1. **mycrew-tools** — project-agnostic primitives (`/slap`, `/likec4`, `/reminder`, `/retract`) plus the
   shipped rule files. Also holds `skillsmaker` and `rulesmaker`, the house standards for writing here.
2. **mycrew-pipeline** — five stage skills carrying one task from decision to hardened code:
   `how-to-do` → `do` → `refactor` → `review` → `test`. Skills only, no commands.
3. **mycrew-worker** — the second pilot on ONE repo. Same rules inline (`/worker`) or as a subagent;
   `worker-rules` is the single source of truth for both, and both must stay in sync with it.
4. **mycrew-chief** — the brain between the product plane and the repos. Owns architecture and specs,
   decomposes an approved feature into per-repo assignments, spawns workers. Never writes code.
5. **mycrew-product** — the only layer that talks to the human about direction. `/product-init` founds
   the product repo once; `/setup` runs an endless extractive interview that files what it draws out.
   `propose-idea` is the one place mycrew contributes an idea of its own — pitched, and filed only on
   the human's approval.

## The product plane — the vocabulary every layer shares

These paths sit at the **product root** (the nearest ancestor folder holding `docs/features/`), one level
above the sub-project repos. Most skills here refer to them, so changing one path means changing several files.

- `docs/features/features.md` — the approved feature list, flat `- [ ] F000 - …` checkboxes with a
  permanent id per line; accumulates, never deleted.
- `docs/features/notes.md` — scratch.
- `docs/features/ideas/` — every idea `propose-idea` pitched: `ideas.md` one line each with the human's
  verdict, `history/<slug>.md` the full case per idea. Approved and rejected alike; append-only.
- `docs/architecture/model.c4` — ONE LikeC4 tree for the whole product, plus `likec4.config.json` beside it.
- `docs/specs/<sub-project>/spec.md` — one spec file per sub-project, a `##` section per feature keyed by
  its id; where a feature's one line isn't enough.
- root `CLAUDE.md` — North Star, current state, and the **Sub-projects list**: the declared paths every layer
  reads. Sub-projects are never discovered by scanning for `.git`.

Ownership is the invariant most edits must respect: the product layer decides *what*, the chief owns the
design and hands out assignments, the worker builds to the plane and never writes it (a design gap comes back
as a report, not a repair). Keep any new prompt on the right side of that line.

## Writing conventions

- Before writing or rewriting a `SKILL.md`, read `mycrew-tools:skillsmaker`; before a rule file, read
  `mycrew-tools:rulesmaker`. Both are the house standard and both obey themselves — match the sibling files.
- All prose, identifiers, and titles in English.
- Prettier ignores `**/SKILL.md` and `**/commands/*.md` — hand-tuned markdown, don't reformat it.
- `.claude/rules/{fit-the-project,manage-git-history,speak-plainly,stay-in-scope}.md` are byte-identical
  copies of `plugins/mycrew-tools/rules/` — the repo dogfoods its own rules. Change one, change both.
  (`bump-plugin-version.md` is repo-only.)
- The flags `--auto`, `--plan`, `--res9ty`, `--worktree`, `--ultracode` are defined in `worker-rules` and
  restated in `commands/worker.md` and `commands/chief.md`. Change one wording, change all of them.
- A plugin's `description` is the same sentence in its `plugin.json` and in `.claude-plugin/marketplace.json`
  — the manifest's opens `Layer N/5 of the mycrew harness`, the marketplace's just `Layer N/5`. Change one,
  change both.

## Checking a change

No build, no tests. What there is:

```bash
bash -n plugins/mycrew-product/bin/mycrewctl                 # the only script; syntax check
python3 -m json.tool <manifest> >/dev/null                   # manifests must stay valid JSON
```

Try changes for real by installing this checkout: `/plugin marketplace add .` then
`/plugin install mycrew-tools@mycrew`. An installed copy only picks up changes when the plugin's `version`
moves — see `.claude/rules/bump-plugin-version.md`.

`plugins/mycrew-product/bin/mycrewctl` is a standalone terminal helper for `features.md` / `notes.md`
(`mycrewctl features next`, `notes add …`). No skill or command invokes it.
