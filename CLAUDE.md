# mycrew

## North Star
Make this setup trustworthy enough that human can hand it work and not check the result — and autonomous
enough to run 24/7 without attention.

## Status
- **In production:** no
<!-- yes = something is live and in use: every change must be safe and backward-compatible.
     no = greenfield: speed over caution. Every layer below weighs this in all work. -->

## Description
A Claude Code plugin marketplace, built almost entirely out of prompts — skills, commands, agents and
rule files plus JSON manifests, with no build and, but for one shell watcher, nothing to run. It ships
one harness in five layers, each driving the one beneath it: primitives and house rules, a build
pipeline that carries a task from a decision to hardened code, a product plane holding what the
product must do, a board holding what is being done about it right now, and the crew that builds it —
a chief who is the human's deputy over the whole product, a lead who holds one feature as a session of
its own, a worker who carries one assignment. Beside the layers stand the specialists, a plugin each
and only where the trade is substantial enough to earn one: the warden is the first, watching the
working sessions, judging whether what they do still serves what was asked, and stopping what
wandered. Installed into other projects, it is the thing that does the work there rather than the
thing being worked on.

## Sub-projects
<!-- The declared list every mycrew layer reads instead of scanning for .git. -->
- **Layout:** singlerepo
- `.` — the harness itself: every plugin, skill, command, agent and rule lives in this one repository.
