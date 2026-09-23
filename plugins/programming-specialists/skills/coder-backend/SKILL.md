---
name: coder-backend
description: "Domain checklist for writing backend code — contracts, data, errors, concurrency, resilience, observability, config, lifecycle. What not to forget while building server-side code."
argument-hint: "<what you're building>"
---

# coder-backend — what not to forget building server-side code

## Contracts

- Settle the interface — shape, status codes, required vs optional — before writing the implementation.
- Version a contract already in use; a breaking change ships with a migration path, never a silent swap.
- Prefer additive changes to a live contract — add a field, don't repurpose or remove one in place.
- Never expose an internal ID, internal enum, or internal error code through a public contract as-is.
- Deprecate a contract path with notice and a timeline before removing it, not without warning.
- Define what an input's absence means — missing, null, and empty are three different things to a caller.

## Data

- Write migrations that run forward and back, and hold up against real data, not an empty database.
- Ship a schema change in the same commit as the code that needs it.
- Watch for N+1 queries; load what a request needs in the calls its scale actually allows.
- Page any result set that can grow unbounded; a query without a limit is a future outage.
- Treat cache invalidation as part of the write path, not an afterthought bolted on after the fact.
- Decide what "not found" returns before writing the read path — empty result, null, or an error.

## Errors and boundaries

- Validate everything crossing a process boundary — a request, a queue message, a file — before it's trusted.
- Check authorization server-side, next to the action it guards. Never trust what the client claims.
- Never let internals leak into a response. Full detail goes to the log, never onto the wire.
- Fail loud on a programmer error, fail soft on an expected one — don't handle a bug like it's routine.
- Give an error enough to act on — what failed, with what input — not just "an error occurred".

## Concurrency

- Make an operation idempotent wherever a retry, a duplicate webhook, or a re-run job can hit it twice.
- Lock, transact, or queue only where shared mutable state is genuinely at risk — not by default.
- Assume more than one instance of this code runs at once; single-instance timing is never safe to assume.
- Bound every queue, worker pool, and in-flight request count — unbounded concurrency is a crash waiting.
- Guard a read-modify-write sequence; another process can change the value between the read and the write.

## Resilience

- Put a timeout on every network call, lock wait, and external resource — nothing waits forever.
- Retry a transient failure with backoff; an immediate retry just hits the same overload harder.
- Stop calling a dependency that's clearly down instead of piling retries onto its failure.
- Decide a fallback per dependency ahead of time — degrade the feature, don't take the whole request down.
- Never retry a request that already changed state unless the operation is confirmed idempotent.
- Respect a downstream service's rate limit; back off before it forces the issue with an error.

## Observability

- Log what someone debugging this at 3am needs — inputs, identifiers, outcome — not what was easy to print.
- Structure log output so it can be searched and filtered; a wall of free text isn't a debugging tool.
- Never log a secret, credential, or full payload carrying personal data.
- Log one line per meaningful event, not one per line of code — a trace isn't a narration.
- Carry a correlation ID through every log line a single request or job produces.
- Strip debug prints left over from development before the code ships.

## Configuration

- Read configuration from the environment or a config source; never hard-code a value that changes per deploy.
- Keep a secret out of source control, out of a log line, and out of an error message — always.
- Fail fast at startup on missing or malformed configuration; don't discover it mid-request.
- Default a setting where a sane default exists; fail loudly and early where it doesn't.

## Lifecycle

- On shutdown: stop taking new work, finish what's in flight, then exit — don't just die mid-request.
- Release every connection, file handle, and lock you opened, on every exit path, including failing ones.
- Expose a way to check the process can actually do its job, not just that it's running.
- Warm up and verify what needs it before the process starts taking real traffic.

## Structure

- Keep business logic free of the transport and framework code around it; it should run without either.
- Push I/O to the edges; keep core logic in functions that take input and return output, nothing else.
- Wire a dependency in rather than reaching for a global; a hard-coded global can't be swapped in a test.
- Resist an abstraction until a second real case needs it — one implementation doesn't need an interface.

## Dependencies

- Pin a dependency's version; an unpinned one can change the build under you with no code change of your own.
- Weigh what a new dependency costs — size, maintenance burden, the trust it demands — before adding it.
- Check a license before adding a dependency; not every license is compatible with shipping the product.
