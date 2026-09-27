---
name: look-around
description: "Use at the start of a session, before touching anything, to get oriented fast in an unfamiliar or long-untouched project."
---

# look-around — quick orientation at session start

Get the lay of the land in one fast pass, not an audit. Read the root CLAUDE.md (and any nested ones
near the working directory), list what's under .claude/rules (project and installed plugin rules),
skim your memory index (MEMORY.md) and open any entry that looks live or contradicts what you just
read, and check `git log -n 10 --oneline` plus `git status`. That's the whole sweep — no reading every
file in full, no walking the memory folder entry by entry, no diffing old commits. Stop as soon as you
can state in a few lines: what this project is, what state it's in, which rules or memories constrain
the work ahead, and what changed recently. Say that, then stop — don't start work unless asked.
