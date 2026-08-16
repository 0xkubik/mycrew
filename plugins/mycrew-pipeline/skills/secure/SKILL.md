---
name: secure
kind: intent
description: "Use when a change must be hunted for security holes before it ships — injection, broken access control, leaked secrets, unsafe defaults, risky dependencies. Eyes that didn't write the code hunt AND rule; you close every confirmed hole in place, never hand up a list. Skips in one honest line when the change touches no trust boundary. Runs after review or standalone. Triggers: \"security review\", \"is this safe\", \"check for vulns\"."
argument-hint: "[what to secure — omit for the last change]"
---

# secure — read it like an attacker, then close the holes

You read the change the way someone trying to break it would: not *does it work* but *how do I make
it do something it shouldn't*. The hunt and the ruling belong to eyes that did not write this code —
yours knew the intent and will forgive it. The fixes are yours.

**Invariants — non-negotiable:**
- **The author never rules on his own code.** You dispatch the hunt and the verdict; you do not decide
  a hole isn't real because you remember meaning it that way.
- **Verify before you close.** A finding is a hypothesis until the attack path is shown to reach. A
  fix applied to a non-hole is a new hole.
- **Apply, don't report.** You close every confirmed hole yourself. A findings list handed up is a failure.
- **Bounded to the change** — the diff you were handed, not the whole repo's history of sins.

## Gate — is there a surface at all

Spend this pass where there is something to attack. The change touches **none** of: input from
outside the process · identity, permissions or access checks · secrets and credentials · data
crossing a boundary (network, shell, filesystem, database, serialization) · a new or bumped
dependency · a default that decides who may do what → say so in **one line** and skip. Touching any
one of them is never a skip, however small the diff.

## The hunt — fresh eyes, in lanes the change earns

Dispatch subagents on the **`sonnet` model**, scoped to the change, splitting the surface the change
actually has — never a fixed set of lanes. Cover what applies: **untrusted input** (injection through
SQL, shell, path, template, deserialization; missing or late validation) · **access** (authn and
authz gaps, object-level checks, privilege boundaries, TOCTOU) · **exposure** (secrets in code, logs
or errors; over-broad responses; SSRF and open redirect) · **the ground it runs on** (unsafe
defaults, dependency risk, permissions, crypto used wrong).

**Each hunter returns** (0–N findings):

```
findings: [ {
  title:    <short name>
  where:    <file:line / function>
  path:     <the attack: who does what → what they reach or get>
  severity: high | med | low
  trigger:  <the concrete input or condition that walks that path>
  fix:      <how it closes>
} ]
empty_reason: <if findings == [] : why this lane is genuinely clean here>
```

**Empty-lane valve:** a lane with nothing real says so. Inventing a hole to fill a slot is a bug —
noise here trains everyone to stop reading the output.

## The verdict — also not yours

Each finding goes to a **fresh judge** that never wrote the code and never sees your account of what
you intended: does the trigger actually reach, or is it guarded upstream? Confirm with a repro, a
trace, or a tight argument. Kill the false positives, dedupe across lanes, rank by damage — what an
attacker gains, not how clever the finding is.

## Close it

Fix each confirmed hole yourself, and re-run the safety net. **Never close a hole by hiding it** — a
swallowed error, a silenced log, a check moved out of reach is not a fix. Materially different ways
to close it, no clear winner → `mycrew-pipeline:how-to-do`. A hole that cannot be closed inside your
brief — it needs the design to move — is named in your report and left standing, never patched
around.
