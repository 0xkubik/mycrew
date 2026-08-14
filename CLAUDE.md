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
rule files plus JSON manifests, with no build and no runtime. It ships one harness in five layers,
each driving the one beneath it: primitives and house rules, a build pipeline that carries a task from
a decision to hardened code, a worker that drives that pipeline on one repository, a product plane
holding what the product must do, and a chief on top — the human's deputy — that
shapes that plane and dispatches workers across the sub-projects. Installed into other projects, it
is the thing that does the work there rather than the thing being worked on.

## Sub-projects
<!-- The declared list every mycrew layer reads instead of scanning for .git. -->
- **Layout:** singlerepo
- `.` — the harness itself: every plugin, skill, command, agent and rule lives in this one repository.
