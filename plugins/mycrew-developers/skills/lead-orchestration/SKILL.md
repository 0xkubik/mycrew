---
name: lead-orchestration
kind: rule
description: "Use when a feature is being handed to a lead or a lead has brought one home — the one rule set for running leads across a product: what a complete feature brief carries, what is never handed down with it, how dependent features are spread, what a finished feature is judged against, and the one verdict it earns, ACCEPTED or BACK. Reference, loaded by the chief."
user-invocable: false
---

# lead-orchestration — how the leads are run

A **lead** is a whole feature's owner and a session of its own, not a call that returns. You write the
brief it holds and you rule on what it brings back — both ends of the same job, because half of "it
built the wrong feature" is a brief that described the wrong feature. Between those two moments it is
not yours to steer.

## The brief

- **Spawn one lead per feature, named for the feature it holds.** The name is how you and every other
  lead reach it; an unnamed session is one nobody can send a dependency to.
- **A brief carries the feature, its detail file, the sub-projects it reaches, and the features it
  depends on with the leads that hold them.** Everything it cannot see from inside its own repo is
  yours to put in the brief.
- **A brief the lead would have to invent its way out of is unfinished.** Finish it here — a guess made
  downstream comes back as a feature you delegate twice.
- **Never hand the plane down with the feature.** The detail file is a brief to build to; adding a
  feature, checking one off or editing that file stays with you, however small the correction.
- **Never spawn two leads onto one feature.** Two owners is no owner, and neither can be asked what
  state it is in.

## How features are spread

- **Everything the plane has approved and nothing blocks goes out at once.** Delegating one feature and
  waiting makes the whole product move at one lead's pace.
- **A dependent feature is spawned with its provider named, not held back.** The lead settles the
  waiting itself; holding it here just moves the queue into your context.
- **Spawn only as many leads as you can take home.** Every one of them will finish and need a verdict,
  and features finished but never accepted are the same as features never built.
- **Never reach past a lead into its workers.** How the feature gets built is the lead's, and a second
  hand in its dispatches leaves nobody accountable for the result.

## The verdict

- **Take a finished feature the moment it lands, never in a batch.** An accepted feature unblocks the
  leads waiting on it; a batched review throws away the parallelism you just bought.
- **Judge against three things only: the feature as the plane states it, its detail file, and the brief
  you actually sent.** How it was built, which route it took, what you would have done is not this gate.
- **Read the brief you sent, not your memory of it.** A thin or mistaken brief is yours — repair it and
  re-brief, never charge it to the lead.
- **Steer by what the lead reports, never by reading the code.** You are a brain, not a reviewer; the
  pipeline already hunted the bugs, the holes and the mess.
- **A fork the lead settled inside the feature was the lead's to settle.** Overrule only where the
  choice reaches past the feature — it contradicts the plane, or changes what another feature builds
  against.
- **A plane gap the lead names is yours, not a failure of theirs.** Move the plane by the product
  layer's rules, then re-brief. Never send a lead to fix the plane.
- **ACCEPTED or BACK, nothing else.** ACCEPTED — the feature exists as the plane states it. BACK —
  exactly what is missing and what the re-brief must say **differently**, so the same gap cannot return.
- **Only accepted work moves the plane.** Mark the feature and advance the frontier after acceptance and
  never before.
