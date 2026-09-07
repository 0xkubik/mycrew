---
name: designer-review
description: "Use when the human explicitly asks the designer to look at a build the coder has already shipped and judge it eye-first — never on the designer's, lead's, or coder's own initiative. Checks the rendered UI/UX against the kit and hands back a concrete list of fixes; never edits the coder's files and never touches the kit itself (that's designer-design)."
argument-hint: "<the built screen or flow to review>"
---

# designer-review — judge the shipped build against the kit

Runs standalone, only when the human asks for it by name — not part of coder → reviewer → tester,
and not something the designer starts on its own. The coder has already built the screen out of the
kit's components; this pass looks at the real, rendered result and says where it falls short.

## What to do

- **Open the real build**, not the code — browser or screenshot via computer-use or claude-in-chrome.
  Judge what a user would see, not `kit.html` and not the markup.
- **Compare against `design/kit.html`.** Drift from the kit's tokens, components, or states is a bug,
  not an opinion — name it as one.
- **Walk the actual flow like a user would**, at real breakpoints: layout, spacing, hierarchy,
  readability, hover/focus/empty/error states, motion, pacing.
- **Judge UX, not just look.** Is the flow clear, does an interaction do what a user expects, does
  anything fight the kit's own logic.

## Never

- Edit the coder's files — this is a review pass, not a fix pass; the coder integrates the fixes.
- Touch the kit — a gap in the kit itself (missing state, wrong token) is a finding to run
  `mycrew-specialists:designer-design` on separately, never patched inline here.

## Report

Back to the human directly, plain list: what's off, whether it's a kit-drift or a UX problem, and the
concrete fix. Nothing gets edited by this pass — the coder applies what's accepted.
