---
name: design-rules
description: "Use whenever the product's interface is being decided — what a surface is, how a flow runs, what something looks like and how it behaves. The house stance: the built UI is the only design there is, so a direction is settled by building it and never by writing it down or mocking it up. Rules only: what must hold when the interface is chosen, never who chooses it or how a proposal is worked out."
user-invocable: false
---

# design-rules — how the product's interface is decided

The design **is the built UI** — what a person actually sees and touches when the product runs.
Nothing standing beside it describes it. So deciding a direction ends in exactly one place: work that
changes that interface.

## Rules & concepts — non-negotiable

- **Never write the design down.** No design document, no spec, no mockup kept as the reference, no
  section in the plane. A description of the interface is a second truth that stops matching the
  product the first time a screen changes, and then it misleads whoever builds against it.
- **Look at what is built before you change it.** Run the product and see the surfaces as they are.
  Deciding from a description of the UI, or from what it was the last time you looked, is how a
  direction lands on a screen that no longer exists. Nothing built yet → the features are the ground.
- **The human's vision is the input, in whatever form it arrives.** Words, a reference product, a
  rough sketch, "like this but calmer" — take it, understand what they are after, and let it shape
  what you build. Never transcribe it back at them and never file it anywhere.
- **A decision lives only as work.** Settled means being built — the same run, handed to whoever
  builds it. A direction agreed and not carried into work did not happen; there is no file to come
  back to and nobody will remember it.
- **Decide at the surface, not per feature.** Surfaces — screens, flows, the shell around them — are
  what the design is made of. A new feature lands on the surfaces that already exist unless it truly
  has nowhere to go; giving every feature a place of its own is how a product turns into a list of
  unrelated pages.
- **Consistency beats novelty.** What the product already does is the strongest argument for what it
  should do next — same patterns, same spacing, same words for the same things. A direction is only
  worth breaking that for when the existing pattern genuinely fails the job.
- **Nothing decided that cannot be pointed at.** Every choice has to be visible on a running screen —
  this element, here, behaving this way. A direction that can only be described in adjectives has not
  been decided, it has been gestured at.
- **The human owns the look.** You work a direction out and put it to them with the case; they decide.
  One they have not approved is never built, and their reason for turning one down binds what you
  propose next.

## What the interface must be

- **Experience before looks.** A direction is judged first on how it feels to use — the person always
  knows where they are, what just happened, and what to do next. One that looks right and reads wrong
  has failed, however good the screenshot is.
- **Every state, not the good one.** A direction is not decided until it is decided empty, loading,
  broken and overflowing — nothing there yet, something on its way, the thing failed, ten thousand rows,
  a name that runs off the edge. The surface with perfect content is the one case that designs itself.
- **Motion carries every change.** Things move, arrive and leave; nothing snaps into place. Animation is
  quick, smooth, and says what happened — motion that only decorates, or that makes the person wait, is
  cut.
- **Nothing invented.** Elements sit where a person expects them and behave the way they look like they
  behave. A novel interaction is a thing to be learned, and nobody came here to learn an interface: the
  ordinary control on the ordinary gesture wins every time.
- **One visual system.** One palette, one readable typeface, one spacing rhythm, across every surface —
  and a current one, not a decade old. Surfaces that do not match each other read as unfinished.
- **Dense, never cramped.** Elements sit close together and the screen stays compact. Space is spent
  where it separates things that are genuinely separate, never by default.
- **Show it, don't caption it.** Images, icons and media carry the meaning — mocked placeholders early
  on are expected, not a shortcut. Blocks of explanatory text on a surface are a failure of the design;
  text that is genuinely needed lives in an element that appears on demand and is gone otherwise.
- **Fit the product and its audience.** The register comes from who this is for — what is right for a
  trading terminal is wrong for a children's app. The North Star and the audience settle it, never taste
  in the abstract.
