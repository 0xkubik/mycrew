---
name: improve
description: "Use when, mid-work on some other project, something in mycrew's own agents, skills or rules turns out wrong or missing — a bad prompt, a skipped guardrail, a rule that didn't hold. Turns the observation into a committed fix in the real mycrew dev repo, never the installed plugin copy."
argument-hint: "[what to fix — or nothing, to pull it from what was just noticed]"
---

# improve — fix mycrew itself from wherever you noticed it

The project you're working in stays untouched. The fix lands in the mycrew dev repo instead.

## Steps

1. **Pin the observation.** From this conversation, state in one line what went wrong and where it
   showed up — which agent, skill or rule, what it did instead of what it should. Vague or missing →
   ask before touching anything.
2. **Find the dev repo, not the installed copy.** The plugin copy under
   `~/.claude/plugins/marketplaces/mycrew` is an auto-updating mirror — edits there are gone on the next
   pull. Check memory for the dev repo's path. Not there yet → ask once, then save it as a reference
   memory.
3. **Locate the exact file** in the dev repo — the one skill, agent file, or rule causing it or multiple files. Read
   it whole before editing; don't guess from the filename.
4. **Check all repo rules before editing files in there**
5.  **Fix precisely the behavior that was asked for.**
6. **Look around the repo** for what else this change could have affected, and what follow-up actions make sense.

## Done 

1. When the experience gained while working on a project is captured in the plugin, not in the project where the work happened.
2. All plugins stay consistent after the improvement, with no contradictions in behavior.
3. The improvement work didn't break any rule in the repo and followed everything stated in them.