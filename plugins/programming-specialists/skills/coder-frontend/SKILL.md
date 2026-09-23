---
name: coder-frontend
description: "Domain checklist for writing frontend code — components, layout, accessibility, input, state, performance, forms, i18n, resilience, security."
argument-hint: "<what you're building>"
---

# coder-frontend — what not to forget building UI code

## Components

- Reuse an existing component or token before writing new markup or styles from scratch.
- Build every state a component needs — hover, focus, disabled, loading, empty, error — not just rest.
- A repeated pattern becomes a variant prop on one component, never a second copy of it.
- Handle long, short, empty, and overflowing content — don't design for one sample string.
- Separate presentation from business logic so a component can be tested without its real data source.
- Give a component one obvious way to override its default look, not five competing ones.

## Layout and responsiveness

- Reserve space before content arrives — nothing should shove a neighbour when it loads or expands.
- Lay out for a range of screen sizes and orientations, not one fixed canvas.
- Let content reflow and wrap; don't clip or truncate without a way to reach the rest.
- Check both the smallest and largest sizes you support, not just the one on your own screen.
- Respect the platform's safe areas and system chrome instead of assuming the full surface is yours.

## Motion

- Animate only in response to something the user did; motion as decoration is noise.
- Respect a reduced-motion preference — shorten or drop animations, don't force them.
- Keep transitions short enough that they never feel like they're blocking the next action.
- If new state arrives mid-transition, resolve it cleanly — don't queue and stack animations.

## Accessibility

- Every interactive element needs a visible focus state and a name assistive tech can read.
- Text holds contrast and survives zoom or larger system font sizes — colour alone can't carry meaning.
- Group and label related controls so their relationship is announced, not just each one alone.
- Announce async state changes — loaded, failed, updated — to assistive tech, not only sighted users.
- Follow the platform's own accessibility conventions instead of reinventing a custom one.

## Keyboard and input

- Every action reachable by pointer or touch must also be reachable without one.
- Keep tab and focus order matching visual order; don't let it jump around the layout.
- Let the platform's "back out" action close the topmost overlay before it does anything else.
- Support the navigation pattern users expect for a given control — stepping through a list, etc.
- Size touch targets for a finger, not a cursor, even on a device that also takes precise input.
- Debounce or throttle handlers on expensive or high-frequency input; don't run full work per event.

## State and data

- Wire every request's full set of states: loading, empty, error, success — never just the happy path.
- Keep state at the lowest level that needs it; lift it only once two places truly share it.
- Fetch once per need — a network call inside a render path is a bug, not a pattern.
- Cancel or ignore a stale request once a newer one supersedes it — don't let responses race.
- Treat an optimistic update as provisional; reconcile or roll it back once the real answer arrives.
- Derive computed values from source state instead of duplicating them somewhere they can drift.

## Async and lifecycle

- Cancel in-flight work, timers, and subscriptions when the thing that started them goes away.
- Guard against updating a view that has already closed, unmounted, or navigated away.
- Keep expensive or blocking work off the main thread so input and rendering stay responsive.
- Break up large synchronous work so it can't freeze the whole interface for one operation.

## Performance

- Size and format images and assets for where they're shown, not the source resolution.
- Load what's off-screen or not-yet-needed lazily instead of paying for it up front.
- Measure before optimizing — don't hand-tune a path that isn't actually slow.
- Avoid re-deriving the same expensive value on every update; cache or memoize it.

## Forms and input handling

- Validate on the client for fast feedback, but never treat it as the only validation.
- Preserve what a user entered across an error, a retry, or a navigation away and back.
- Show a validation error next to the field it belongs to, not only in a summary far away.
- Set the right input type and constraints so the platform's own input aids can kick in.
- Validate progressively; don't block submission on a field the user hasn't reached yet.

## Internationalization

- Never concatenate strings assuming a fixed word order — a sentence built from parts breaks.
- Leave room for text to grow; a translated string can run much longer than the source.
- Externalize every user-facing string instead of hardcoding it inline.
- Format dates, numbers, and currency for the user's locale, not the one you wrote the code in.
- Support a mirrored, right-to-left layout if the product supports a right-to-left language.

## Resilience and errors

- Wrap sections that can fail in a boundary that degrades gracefully, not one that blanks everything.
- Distinguish "no data yet" from "data failed to load" from "data is empty" — each needs its own message.
- Retry transient failures with backoff; surface permanent ones with a clear, actionable message.
- Handle the offline and slow-network case explicitly — don't assume a request always returns fast.
- Never let one unhandled error take down the whole interface; contain the blast radius.

## Security

- Escape untrusted content by default; sanitize anything you deliberately render as markup.
- Never put a secret or credential in client-visible code, storage, or logs.
- Validate and constrain anything read from a link or external input before acting on it.
- Treat any client-side check — validation, permission flag, business rule — as convenience, not a boundary.

## Testability

- Structure components so behaviour can be tested without spinning up the whole interface.
- Give interactive elements stable identifiers a test can target, independent of text or styling.
- Keep side effects — timers, network calls — behind something a test can substitute.
