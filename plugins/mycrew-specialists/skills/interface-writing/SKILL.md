---
name: interface-writing
kind: rule
description: "Use whenever words go into an interface — a label, a button, an error, an empty state, a toast. What the words must do, whose vocabulary they use, and how a flow keeps one name for one action. Rules only: never the visual direction they sit in."
user-invocable: false
---

# interface-writing — words are design material, not decoration

Words are in an interface for one reason: to make it easier to understand, and so easier to use. Copy
written as an afterthought makes a design feel as templated as a stock palette does — and it is the
part a person actually reads.

## Whose words they are

- **Write from the person's side of the screen.** Name things by what they control and recognise, never
  by how the system is built: someone manages notifications, not webhook config.
- **Say what a thing does, never sell it.** Plain description beats a pitch every time, and specific
  always beats clever.
- **Ask what the surface needs to say before writing what it says.** The answer is usually shorter than
  the first draft and never the same as the field names underneath.
- **Keep the register conversational and tuned.** Plain verbs, sentence case, no filler, tone matched to
  the brand and who it is for.

## How a flow stays learnable

- **A control names what happens when it is used.** "Save changes", never "Submit".
- **One action keeps one name for its whole life.** The button that says Publish produces a toast that
  says Published; a renamed action is a new action as far as the person is concerned.
- **Each element does exactly one job.** A label labels, an example demonstrates, a hint hints — nothing
  quietly does double duty.

## The two surfaces everyone writes last

- **An error says what happened and how to fix it, in the interface's voice.** Errors do not apologise
  and are never vague about what went wrong. "Something went wrong" is the absence of a message.
- **An empty state is an invitation to act, not a mood.** It names the one thing to do next; emptiness
  described and left there is a dead end with nice typography.
