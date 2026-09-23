---
name: work-with-specialists
description: "Use before dispatching any specialist (coder, designer, devops, reviewer, tester) — what each one knows and does, and the two ways to hand it work: a board task, or a self-contained prompt with nothing else assumed."
---

# work-with-specialists — what each one knows, and how to hand it work

Every specialist agent is fully self-contained — it carries its own identity, values, and craft
knowledge, and knows nothing about milestones, boards, or the management layer above it. Read this
before every dispatch: what each one actually does, and the two shapes work can arrive in.

## The two ways to dispatch

- **A board task.** The task is the brief — metadata, acceptance criteria, origin label. The specialist
  reads it, does the work, reports back. Default for anything the board already tracks.
- **A standalone prompt.** No task needed. The prompt itself carries everything the specialist would
  otherwise get from a task: what to build or check, the boundary of the ask, anything it needs to do
  it well. Use this for whatever isn't worth opening a task for — a quick fix, a one-off check, a
  question only a specialist can answer.
- Either way, a specialist never infers scope from context it wasn't given — an unstated boundary is
  one the dispatcher forgot to state, never one it will guess at.

## Prompt in goals, not steps

- State the goal, the context that shapes it, and what "done" must satisfy — never a step-by-step of
  how to build it. The specialist owns the how; that's what its own craft and rules are for.
- Useful context beats instructions: what this connects to, what already exists, what constraints are
  real — hand over what it needs to know, not a script to follow.
- Name what matters to check before the work is handed back — the bar it's judged against, not a
  checklist of actions to perform to get there.
- A prompt written as steps is a sign the dispatcher is doing the specialist's thinking for it —
  rewrite it as the goal those steps were trying to reach.

## What every specialist needs from you, either way

- **The actual boundary of the ask** — specialists no longer read a shared "where your freedom ends"
  doc; state it in the dispatch, every time.
- **Where it happens** — the repo, the sub-project, the branch or worktree — never assumed.
- **How to report back** — a specialist's report comes back in its reply; read it there, not from a file.

## The specialists

- **coder** — writes one task end to end, refactor-first, without testing and reviewing.
- **designer** — holds design best practice, judged by rendering it and looking.
- **devops** — works real infrastructure directly, security-first — deploys, cluster, CI/CD. 
- **reviewer** — reads someone else's committed code and reasons out what's actually wrong with it.
- **tester** — proves committed code works, unit through e2e, owns the whole suite's health.

## Keep it current

This roster drifts the moment a specialist's tools or scope change. Whoever edits an agent file updates
its entry here in the same change.
