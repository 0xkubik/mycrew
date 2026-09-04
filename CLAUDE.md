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
rule files plus JSON manifests, with no build and nothing to run. It ships one harness: primitives and
house rules, the specialists — agents each carrying one concrete piece of work, the coder who carries a
task from a decision to hardened code by running the build pipeline as his own coder-* skills, the
designer who owns the product's UI kit as an independent source of design truth, each keeping its own
domain data — a product plane holding what the product must do together with a board holding what is
being done about it right now, both kept in one backlog.md store — and the leadership that steers it, a
chief who is the human's deputy over the whole product and a lead who holds one feature as a session of
its own, spawning specialists to carry the work. Installed into other projects, it is the thing that
does the work there rather than the thing being worked on.

## Sub-projects
<!-- The declared list every mycrew layer reads instead of scanning for .git. -->
- **Layout:** singlerepo
- `.` — the harness itself: every plugin, skill, command, agent and rule lives in this one repository.
