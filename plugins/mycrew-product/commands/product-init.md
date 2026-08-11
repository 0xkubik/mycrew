---
description: "Use once to found the product — turn the folder holding the sub-project repos into the product repository: its own git repo, the root CLAUDE.md with a North Star drawn from the human, and the empty product plane (features, architecture, specs). One-shot init, run at the product root."
---

# /product-init — found the product

Turn the folder that holds the sub-project repos into the **product repository** — the home of
everything true about the whole product. One-shot; run it once, then `/setup` fills it forever after.

## What you do

1. **Gather.** Find the sub-projects and **read any `CLAUDE.md` they carry** — your raw material.
   ```bash
   find . -maxdepth 3 -name .git -not -path '*/.claude/*' | sed 's|/\.git$||'
   ```
2. **Make the root a repository, and settle how the sub-projects hang off it.** `git init` here, then
   ask the human which of the two, and record the answer in the Sub-projects section:
   - **Mounted** — each sub-project is added with `git submodule add <url> <path>`. `.gitmodules`
     becomes the manifest, one recursive clone brings the product down whole, and each repo keeps its
     own visibility, so some may be public and some private. The cost is a pointer-bump commit here
     whenever a sub-project moves.
   - **Loose** — the sub-projects merely sit here and the root ignores them. Then the `.gitignore`
     **must list every one of them before the first `git add`**: git does not recurse into a nested
     repo, but a single `git add -A` turns one into an unpopulated gitlink — clones lose its contents
     and every commit inside it dirties the root. Added after the fact, `.gitignore` no longer helps
     and it takes a `git rm --cached` to undo.

   A sub-project that is simply a folder of this repository — no repo of its own — needs neither.
3. **Ask.** Draw two things out of the human — never invent them: the product's single **North Star**
   (guiding intent), and its **current state** — is there a live production in use.
4. **Write on approval.** Compose the root `CLAUDE.md`, write it only once they approve.
5. **Seed the empty product plane.** `docs/features/features.md` and `notes.md` from the
   `mycrew-product:feature-management` templates, plus empty `docs/architecture/` and `docs/specs/`.
   `/setup` fills them; leave them empty here.

## What the root CLAUDE.md holds

- **North Star** — from the human.
- **Current state** — is there a live production, what stage the product sits at, and what that
  demands of every change (a live prod means safe, backward-compatible moves; greenfield means speed).
  Every layer below weighs it in all work.
- **Description** — a top-level synthesis of the product, assembled from the sub-projects' CLAUDE.mds
  (the whole, not the parts pasted).
- **Sub-projects** — the declared list every layer below reads instead of scanning. One entry per
  sub-project: its **path**, one crisp line on what it is and its role, and — where it isn't obvious —
  whether workers are dispatched into it at all. A repo that is a source rather than a build target (a
  charter, a spec bundle, a vendored reference) must say so, or the chief will try to build in it.
