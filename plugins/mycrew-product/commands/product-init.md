---
description: "Use once to found the product — settle how the repository is laid out (singlerepo, monorepo, or polyrepo with submodules), take the sub-projects from the human, write the root CLAUDE.md with a North Star drawn from them, outline the empty docs/ plane, and git init. Stops before the first commit so the human can look at everything. Run at the product root."
---

# /product-init — found the product

Turn the folder that holds the sub-projects into the **product repository** — the home of everything
true about the whole product. One-shot; run it once, then `/braindump` and `/ask-me` fill it forever
after. You **never commit**: the run ends with everything written and the human free to look.

## What you do

1. **Ask the two questions first**, via `AskUserQuestion`, before writing anything.
   - **How the product repository is laid out:**
     - **Singlerepo** — the product *is* one codebase, no sub-projects at all. The plane still lives at
       the root; the Sub-projects list holds the single entry, this repository itself.
     - **Monorepo** — every sub-project is a plain folder of this one repository, one history for
       everything. A folder that already carries its own `.git` must have it removed first, or `git add`
       turns it into an empty gitlink: clones lose its contents.
     - **Polyrepo with submodules** — each sub-project keeps its own repository and is mounted here with
       `git submodule add <url> <path>`. `.gitmodules` becomes the manifest, one recursive clone brings
       the product down whole, and each repo keeps its own visibility — some public, some private. The
       cost is a pointer-bump commit here every time a sub-project moves.
   - **Which sub-projects the product contains** — the path of each and one line on what it is (a
     singlerepo skips this one). Seed the options from what's on disk, but their list is the answer:
     ```bash
     find . -maxdepth 3 -name .git -not -path '*/.claude/*' | sed 's|/\.git$||'
     ```
2. **Draw out the North Star and the status** — the product's single guiding intent in their own words,
   and whether anything is **live in production**. Never invent either. Read any `CLAUDE.md` the
   sub-projects carry: that's raw material for the description, not for these two.
3. **Write the root `CLAUDE.md`** to the template below.
4. **Outline the `docs/` plane — files in place, nothing filled in.**
   - `docs/product/features.md` — the `mycrew-product:product-rules` template, no entries. Founding
     is not filling: it stays empty unless the human affirms something about the product while
     answering — that is formalized by that skill's rules, in that turn, rather than lost to the run.
5. **`git init`, mount the sub-projects if the layout says so — then stop.** No `git add`, no commit:
   say what you created and leave it for the human to read.

## The root CLAUDE.md — the template

```markdown
# <product name>

## North Star
<the one guiding intent, in the human's own words — what this product exists for>

## Status
- **In production:** <yes | no>
<!-- yes = something is live and in use: every change must be safe and backward-compatible.
     no = greenfield: speed over caution. Every layer below weighs this in all work. -->

## Description
<what the product is as a whole — a synthesis, never the sub-projects' descriptions pasted together>

## Sub-projects
<!-- The declared list every mycrew layer reads instead of scanning for .git. -->
- **Layout:** <singlerepo | monorepo | polyrepo with submodules>
- `<path>` — <what it is and its role, one line>
- `<path>` — <…> <!-- add "not a build target" if no worker is ever dispatched into it: a charter, a
     spec bundle, a vendored reference. Without it the chief will try to build there. -->
```
