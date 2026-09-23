---
name: tester-functional
description: "Checklist of functional-correctness scenarios to verify — boundaries, error paths, state, concurrency, access control, compatibility. What to check is actually correct, not how to write the test."
argument-hint: "<what you're testing>"
---

# tester-functional — what not to forget checking is actually correct

## Boundaries

- Check zero, one, negative, the maximum allowed, and one past the maximum — not just a mid-range value.
- Check an empty collection, a single-item collection, and a large one — not just a comfortable few.
- Check the first and last item of a range, a loop, or a page — off-by-one hides at exactly those edges.
- Check a value sitting exactly on a rule's threshold, not just comfortably inside or outside it.

## Invalid input

- Feed malformed, oversized, wrong-type, and out-of-range input — confirm it's rejected, not just tolerated.
- Confirm rejection produces the right outcome — the right status, the right message — not just "didn't crash".
- Try input no well-behaved client would send; something upstream doesn't guarantee it always stays valid.
- Confirm an operation that should be blocked is actually blocked, not silently allowed through.

## Error paths

- Trigger every distinct error path, not just one representative one — each has its own correct outcome to prove.
- Confirm an error names what specifically failed, not just that something did.
- Confirm an operation that should fail actually fails, and fails for the stated reason, not by accident.
- Check what the system looks like right after a failure — consistent, or left half-changed.

## Workflows

- Verify a multi-step flow end to end, not just each step passing on its own.
- Walk a workflow abandoned halfway — confirm it doesn't leave a dangling, undead state behind.
- Walk a workflow resumed after being left mid-way — confirm it picks up correctly, not re-runs a step.
- Confirm a transition only happens from a valid prior state, never skipped or reached out of order.

## Data integrity

- Create, then read — confirm what comes back matches exactly what was written, not what was assumed.
- Update, then read — confirm the change actually took, and only the field meant to change did.
- Delete, then confirm gone — check it's absent everywhere it should be, not just in the one obvious place.
- Run a sequence of operations and check the end state, not just that each call individually reported success.

## Idempotency and retries

- Repeat an action that can be retried, double-submitted, or replayed — confirm it doesn't happen twice.
- Confirm a retried request that already succeeded returns the same result, not a second effect.
- Confirm a duplicate message, webhook, or event is detected and only ever processed once.
- Check two near-simultaneous duplicate submissions produce one record, not two.

## Concurrency

- Run the same operation against the same resource from two places at once — confirm the result is correct.
- Check a read-modify-write sequence for a lost update when another actor changes the value in between.
- Check what happens when two actors compete for something that can only go to one — a slot, a lock, a claim.
- Check what happens when a resource is deleted by one actor while another is still operating on it.

## Access control

- Check every permission boundary is actually enforced, not just the path that assumes full access.
- Try the operation as a user who should be denied — confirm denial, not just that an admin succeeds.
- Check one person's or tenant's data can't be reached by guessing or substituting another's ID.
- Check a permission is enforced at every entry point to an action, not only the one obvious front door.

## Integration points

- Simulate a dependency being slow, erroring, or unreachable — confirm the caller handles it, not just its success.
- Confirm a partial or malformed response from a dependency is never treated as valid data.
- Confirm behavior when a dependency's response arrives late, out of order, or arrives twice.
- Check a fallback or default engages correctly when the integration point is unavailable.

## Compatibility and recovery

- Check an old caller, an old client, or old stored data still works after a behavior change.
- Check recovery after an interrupted or partially completed operation — resumes clean, doesn't corrupt or duplicate.
- Check a deprecated path still behaves as documented until the day it's actually removed.
- Check a rollback or an undo genuinely reverts state, not just reports that it did.

## Locale and ordering

- Check timezone, locale, and unit-sensitive logic in more than one timezone, locale, and unit — never just one.
- Check a value sitting near a locale or calendar boundary — midnight, month-end, a daylight-saving shift.
- Check sort and list order stays stable and correct across repeated runs and across page boundaries.
- Check a paginated result doesn't skip or repeat an item when the underlying data changes mid-listing.

## Defaults and nulls

- Check a default value applies when nothing is given, and an explicit override actually wins over it.
- Check null, missing, and undefined are handled distinctly from empty and zero, wherever that distinction matters.
- Check an explicit "clear this field" is distinguishable from "field never sent", wherever it matters.
