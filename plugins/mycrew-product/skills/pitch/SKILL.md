---
name: pitch
description: "Use when the human wants their product told back to them — how it actually works, out of what the plane already says. Reads the North Star, every feature and its detail, the decisions and the shape, and tells one plain story: what it is, how a person moves through it, what holds it together, what it will never do — then names what the plane couldn't answer. Strictly what is written: it never invents, never flatters, and never writes anything back. Triggers: \"pitch it\", \"tell me how the product works\", \"explain my product back to me\"."
argument-hint: "[a part to go deep on — or nothing for the whole product]"
---

# pitch — tell the product back, out of what is written

The plane is written one line at a time and nobody ever reads it end to end. You do — then you tell
the human how their product works, in plain human language: the story a list of features never
tells. Hearing it back from outside their own head is how they find what is missing.

## Rules & concepts — non-negotiable

- **Only what is written.** Every sentence traces to something on the plane. Never fill a gap with a
  plausible guess, never smooth a rough edge, never make it sound better than it is. This is a
  mirror, not a brochure — a telling they can't trust is worse than none.
- **Ground in all of it.** The North Star and the status in the product `CLAUDE.md`, `features.md`
  and **every** detail file behind it, the product decisions, and the shape in `docs/design/`. Where
  the Sub-projects list names a sub-project that is documentation rather than code, that is written
  product too — read it.
- **Tell a story, not the files.** Why it exists → what it is → how a person actually moves through
  it, one real path from arriving to getting what they came for → the rules that bind every part →
  what it refuses to do → how it is built, one short paragraph at the end. Never a walk down the
  feature list in id order.
- **Say what it refuses.** A telling that only lists capabilities is a brochure. What the product
  will never do, never charge for, never show — that is half of what it is, and it lives in the
  decisions.
- **Ids in brackets, never in the prose.** Plain sentences carry the story and `(F006)`, `(P001)` sit
  at the end of them so the human can jump to the source. A sentence built out of ids is a file being
  read aloud.
- **Never claim built what isn't.** `[ ]` and `[x]` are the truth of what exists; say plainly which
  parts of this story are still only written down.
- **The whole product fits a page; a named part goes as deep as it has.** No argument → the shape of
  the whole thing, not an inventory. A part named → everything the plane holds about it.
- **Close with what the plane couldn't answer.** The contradictions you hit, the feature with a line
  and nothing behind it, the question any reader would ask that nothing here answers. This is the
  most useful thing you produce — name it plainly and route them to `/ask-me`.
- **Read-only, always.** You file nothing, fix nothing, add nothing — not a feature, not a note, not
  a correction to a contradiction you just found. Writing to the plane is `/braindump`, `/ask-me` and
  `propose-idea`; you only tell.
- **Speak the human's language.** The plane is written in English; the telling is spoken in whatever
  language they speak to you.
