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
3. **Locate the exact file** in the dev repo — the one `SKILL.md`, agent file, or rule causing it. Read
   it whole before editing; don't guess from the filename.
4. **Fix it there**, in the dev repo's own voice, following its own rules: bump the plugin's version in
   its `plugin.json`, update its `CLAUDE.md` if the change affects how the repo is set up or worked on.
5. **Commit in the dev repo** with an honest message. Don't push — a push there goes live in every
   project via auto-update, so surface that a push is the remaining step, and wait to be asked.

## Done

- **A new commit sits in the mycrew dev repo**, unpushed unless pushing was explicitly asked for.
- **Reported back in the current project**, in plain language: what changed in mycrew, and that a push
  is what makes it live everywhere else.
