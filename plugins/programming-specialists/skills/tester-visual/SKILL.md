---
name: tester-visual
description: "Domain checklist for verifying visual/rendered correctness — states, viewports, platforms, layout, content edges, motion, theming, assets, stacking, accessibility, regression."
argument-hint: "<what you're testing>"
---

# tester-visual — what not to forget checking rendered UI

## States

- Render every interactive state for real — hover, focus, active, disabled, loading, empty, error.
- Trigger a state through the real interaction, not a forced flag — a style can exist and never paint.
- Check a state transition renders mid-flight, not just the before and after frame.
- Combine states that can co-occur — a disabled control that's also loading, a focused item also selected.

## Viewport and size

- Check the smallest and the largest supported size, not just the one on your own screen.
- Resize or rotate live and watch the transition, not just the two static end states.
- Check the awkward middle between breakpoints, not only exactly on one.
- Verify nothing forces a scroll direction that wasn't meant to exist.
- Check with system zoom or platform text scaling turned up, not just the default.

## Cross-platform consistency

- Render the same build on every platform and environment it actually ships to, side by side.
- Compare rendering engines, not just device shapes — two devices can share a size, render fonts differently.
- Watch for platform-level chrome — scrollbars, native controls, safe areas — fighting the design.
- Don't trust one machine's fonts, codecs, and defaults to stand in for every user's.

## Layout stability

- Watch content load in real time — nothing should shift, jump, or reflow once a neighbor arrives.
- Confirm reserved space actually holds its size before the real content fills it.
- Watch a transition play through, not just its start and end frame — check the middle too.
- Trigger the same state twice in a row and confirm layout doesn't drift between repeats.

## Content edges

- Render real long, short, empty, and overflowing content — don't judge from a comfortable sample.
- Check a field or list at its documented maximum, not a friendly one.
- Confirm overflow is handled on purpose — scroll, truncate, wrap — never silently clipped away.
- Feed in the actual longest and shortest real strings the product will show, not generic filler text.

## Motion

- Play every animation through, don't just read its spec — timing, easing, end state as rendered.
- Turn on reduced motion and confirm it's actually respected, not just shortened slightly.
- Interrupt an animation mid-play and confirm it resolves cleanly instead of glitching or stacking.
- Confirm a looping or idle animation doesn't drift, stutter, or leak over a long session.

## Theming

- Render every theme or mode the product ships — dark, light, high-contrast, any other variant.
- Switch themes live and check nothing keeps the old theme's colors, icons, or images behind.
- Check contrast and legibility separately per theme — one holding up doesn't mean the other does.
- Confirm every image, icon, and illustration exists for every theme, not borrowed from just one.

## Assets

- Confirm every image, icon, and font actually loads — no broken image, missing glyph, blank spot.
- Check the real fallback for a failed asset load actually shows, not just exists in code.
- Verify assets render at the resolution and density the surface actually needs.
- Watch the loading sequence — a missing asset can flash in before failing, not just fail outright.

## Stacking and overlap

- Open every overlay — modal, tooltip, dropdown, toast — and confirm nothing bleeds through it.
- Confirm an overlay isn't clipped by a scrolling or fixed-size container it sits inside.
- Stack two overlays that can appear together and check which one should win, and that it does.
- Confirm nothing meant to sit behind content ever visibly sits in front of it, or the reverse.

## Accessibility, by eye

- Check contrast on the real rendered build, not the source design — rendering can shift it.
- Tab through and confirm focus is visible on every control, not just present in the markup.
- Confirm touch or click targets are actually big enough to hit on the real surface.
- Check the build with real text scaling turned up, not just at the default render size.

## Regression discipline

- Compare against a known-good baseline, never a single one-off eyeball pass.
- Treat an intentional change to the baseline as its own reviewed step, not a silent overwrite.
- Diff at the resolution and platform that actually matters — passing on one can hide a break on another.
- Re-check a flaky-looking diff by rendering again before writing it off as noise.

## Typography and text

- Confirm the intended font actually loads and rendered text isn't silently using a fallback.
- Check truncation renders where expected and reveals the rest by the method the design promised.
- Render translated or localized text and confirm it doesn't break layout, truncate, or overlap.
- Check line length and wrapping against real content, not a short placeholder sentence.

## Feedback and completion

- Trigger every action and confirm something visibly happens — a click that does nothing is a bug.
- Confirm a loading indicator both appears and disappears at the right moment, not stuck either way.
- Confirm a completed action shows a visible end state, not just a return to the resting screen.
- Check error feedback actually renders where the user is looking, not off-screen or silent.

## Output surfaces

- If the surface prints or exports, render that output for real and check it, not just the screen view.
- Confirm print or export output handles the same content edges — long, empty, overflowing — as the screen.
- Check colors and contrast meant for one display still hold under another lighting or display condition.
