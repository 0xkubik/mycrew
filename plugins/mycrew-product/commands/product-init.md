---
description: "Found the product: turn the folder holding your sub-project repos into the product repository — its own git repo, the root CLAUDE.md with a North Star drawn from the human, and the empty product plane (features, architecture, specs). One-shot init, run at the product root."
argument-hint: "(no args — run at the product root)"
---

# /product-init — found the product

Turn the folder that holds the sub-project repos into the **product repository** — the home of
everything true about the whole product. One-shot; run it once, then `/setup` fills it forever after.

## What you do

1. **Gather.** List the git-repo subfolders and **read each one's `CLAUDE.md`** — your raw material.
   ```bash
   for d in */; do [ -e "$d/.git" ] && echo "$d"; done
   ```
2. **Make the root a repository.** `git init` here, and write a `.gitignore` listing every
   sub-project folder. This is **load-bearing, not tidiness**: git does not recurse into a nested
   repo, but a single `git add -A` at the root turns one into an unpopulated gitlink — clones lose
   its contents and every commit inside it dirties the root. Ignored first, that can't happen; added
   after the fact, `.gitignore` no longer helps and it takes a `git rm --cached` to undo. The folders
   stay visible in the editor and keep working as their own repos.
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
- **Sub-projects** — each with one crisp line: what it is and its role.
