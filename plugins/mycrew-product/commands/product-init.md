---
description: "Use once to found the product — settle repo layout (singlerepo, monorepo, polyrepo with submodules), take the North Star and production status, ask remotes, write the root CLAUDE.md, stand up the backlog, git init, and install the rules into their homes. Stops before the first commit so the human can look."
---

# /product-init — found the product

Turn the folder into the **product repository** — home of everything true about the whole product, the
plane and the board. One-shot. You **never commit**: the run ends with everything written and the human
free to look.

## Steps

1. **Ask the setup questions first, via `AskUserQuestion`, before writing anything.**
   - **Repo layout:**
     - **Singlerepo** — the product *is* one codebase. The plane lives at the root; Sub-projects holds the
       single entry, this repository itself.
     - **Monorepo** — every sub-project is a plain folder of this one repository, one history. A folder
       already carrying its own `.git` must have it removed first, or `git add` turns it into an empty
       gitlink.
     - **Polyrepo with submodules** — each sub-project keeps its own repository, mounted here with
       `git submodule add`. `.gitmodules` is the manifest; each repo keeps its own visibility. Cost: a
       pointer-bump commit here every time a sub-project moves.
   - **Which sub-projects the product contains** — path of each and one line on what it is (singlerepo
     skips this). Seed options from disk, but their list is the answer:
     `find . -maxdepth 3 -name .git -not -path '*/.claude/*' | sed 's|/\.git$||'`
   - **Remotes** — the remote for the product repo and for each sub-project, if any.
2. **Draw out the North Star and the status.** The product's single guiding intent, in their own words,
   and whether anything is **live in production**. Never invent either. Any `CLAUDE.md` the sub-projects
   carry is raw material for the description, not for these two.
3. **Create the base layout.** The root, and for polyrepo a `projects/` folder holding the sub-projects.
   Write the root `CLAUDE.md` to the template below.
4. **`git init`; set the remotes; mount the sub-projects.** Monorepo folders with their own `.git` get it
   removed first; submodules go in with `git submodule add <url> <path>`.
5. **Stand up the backlog** — the plane and the board live in it:
   - **Missing `backlog` CLI → say how to install it (`npm i -g backlog.md`) and stop.** Never improvise
     the store out of hand-written markdown; the CLI owns those files.
   - **`backlog init "<product>" --integration-mode none --defaults`**, run so it uses the repo created
     in step 4. Its own agent integration would fight the rules this command installs.
   - **Bring `backlog/config.yml` to the shape below** — every key the CLI ships is in it, active or
     commented. Keep `project_name` and `task_prefix`; set `statuses` and `labels` to what this harness
     needs — a Backlog column ahead of the CLI's three, and the four origin labels declared. Rest left at
     defaults, commented out.

6. **Install the rules.** Copy every rule file from `mycrew-tools/rules/` into its home, verbatim — a rule
   reworded on the way in is a second rule; one already there is left as is.
   - **Common** (working-with-humans, working-with-text, working-in-repo) → root `./.claude/rules/`.
   - **Code** (working-with-code) → `./projects/.claude/rules/` when polyrepo;
     otherwise into the root global `./.claude/rules/`.
   - **Product / backlog** → into `./backlog/.claude/rules/`, beside the store they govern.
7. **Then stop.** No `git add`, no commit. Say what you created — the root `CLAUDE.md`, the empty
   backlog, its columns and labels, the rules installed — and the command that shows the board:
   `backlog browser` or `backlog board`.

## The root CLAUDE.md — the template

```markdown
# <product name> - <production status>

## North Star
<the one guiding intent, in the human's own words — what this product exists for>

## Description
<what the product is as a whole — a synthesis, never the sub-projects' descriptions pasted together>

## Sub-projects layout: <singlerepo | monorepo | polyrepo with submodules>
- `<path>` — <what it is and its role, one line>
```

## Config template

```yaml
project_name: "<as init wrote it>"
default_status: "To Do"
statuses: ["To Do", "In Progress", "Done"]
labels: ["from-human", "from-chief", "from-lead", "from-specialist"]
date_format: yyyy-mm-dd
max_column_width: 20
auto_open_browser: true
default_port: 6420
remote_operations: false
auto_commit: false
filesystem_only: false
bypass_git_hooks: false
check_active_branches: true
active_branch_days: 30
task_prefix: "TASK"
hide_empty_columns: false             # hide board columns with no cards
types: [bug, feat]  # allowed --type values
default_assignee: []                  # assignees applied to new tasks created without -a
definition_of_done: []                # default Definition of Done items added to every new task - Tests pass
priorities: ["High", "Medium", "Low"] # ordered priority labels, first sorts highest
projects: []                          # allowed --project values for a monorepo backlog
include_datetime_in_dates: true       # add time-of-day to new dates
default_editor: "code --wait"         # editor opened by the 'E' key
zero_padded_ids: true                 # pad task/doc/decision IDs with leading zeros
on_status_change: "..."               # shell command run on every status change
```
