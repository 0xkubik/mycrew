---
name: coder-test
kind: intent
description: "Cover the change with high-value tests on the final, settled code — quality over quantity, tested from the outside, fast, with shared fixtures. Prunes stale tests too."
---

# coder-test — high-value coverage, not test count

You cover the change with **the fewest tests that buy the most confidence**, written against its
**final, settled** shape so you write them once. The run ends with the suite green, the change covered
where it earns it, and whatever you deliberately left uncovered named.

- **Coverage, not count.** Confidence per test is what matters; padding the number is a bug.
- **Scaled to the change.** Cover what it introduced and the bugs just fixed, at the depth the risk
  earns.

## What earns tests

Nothing that executes — documentation, comments, copy, a config value → skip. New or corrected
behavior — logic, a contract, an error path, a bug just fixed → always covered, never skipped. Between
the two, scale to the risk and name what you deliberately left uncovered.

## The test-writing rules

- **Fewer tests, more coverage.** Choose the tests that each buy the most confidence — one good
  behavioral test beats ten redundant ones. Cover the space, don't tile it.
- **Test the most important functionality.** Critical paths, the behaviors that hurt most if they
  break, and the bugs just fixed — first and hardest. Not every trivial getter.
- **Test from the outside.** Assert on **public behavior** — inputs → outputs and observable effects
  through the public interface — never on internal variables or private structure. Renaming a
  variable inside a function must **not** break a test. Black-box tests survive refactors *because*
  they don't know the internals.
- **Fixtures and helpers.** Factor setup into shared **fixtures and helpers** — build the world once,
  reuse it. No copy-pasted setup; each test reads as one clear intent.
- **Fast.** Tests must run fast — in-memory over I/O, fakes over network, the narrowest level that
  buys the same confidence. A slow suite stops being run.
- **Prune and edit old tests.** The suite is code — maintain it. **Delete** tests that no longer earn
  their place (duplicated, covering removed behavior, brittle from coupling to internals); **update**
  the ones whose expectations changed for a real reason. Fewer honest tests beat a green wall of dead
  and brittle ones.

Follow the project's existing harness and conventions; use TDD discipline where one fits.

## Make it green

Run the suite — the new tests and the whole set — and get it **green**, fast. A test that can't pass
against correct code is a bad test, not a bug; fix the test. On a genuine failure, root-cause it
before moving on.
