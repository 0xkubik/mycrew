---
description: "Use once to found the product — settle how the repository is laid out (singlerepo, monorepo, or polyrepo with submodules), take the sub-projects from the human, write the root CLAUDE.md with a North Star drawn from them, stand up the backlog that holds the plane and the board, and git init. Stops before the first commit so the human can look at everything. Run at the product root."
---

# /product-init — found the product

Turn the folder that holds the sub-projects into the **product repository** — the home of everything
true about the whole product, the plane and the board alike. One-shot; run it once, then `/braindump`
and `/ask-me` fill it forever after. You **never commit**: the run ends with everything written and the
human free to look.

## What you do

1. **Ask the two questions first**, via `AskUserQuestion`, before writing anything.
   - **How the product repository is laid out:**
     - **Singlerepo** — the product *is* one codebase, no sub-projects at all. The plane still lives at
       the root; the Sub-projects list holds the single entry, this repository itself.
     - **Monorepo** — every sub-project is a plain folder of this one repository, one history for
       everything. A folder that already carries its own `.git` must have it removed first, or `git add`
       turns it into an empty gitlink: clones lose its contents.
     - **Polyrepo with submodules** — each sub-project keeps its own repository and is mounted here with
       `git submodule add <url> <path>`. `.gitmodules` becomes the manifest, one recursive clone brings
       the product down whole, and each repo keeps its own visibility — some public, some private. The
       cost is a pointer-bump commit here every time a sub-project moves.
   - **Which sub-projects the product contains** — the path of each and one line on what it is (a
     singlerepo skips this one). Seed the options from what's on disk, but their list is the answer:
     ```bash
     find . -maxdepth 3 -name .git -not -path '*/.claude/*' | sed 's|/\.git$||'
     ```
2. **Draw out the North Star and the status** — the product's single guiding intent in their own words,
   and whether anything is **live in production**. Never invent either. Read any `CLAUDE.md` the
   sub-projects carry: that's raw material for the description, not for these two.
3. **Write the root `CLAUDE.md`** to the template below.
4. **`git init`, and mount the sub-projects if the layout says so.** Monorepo folders that carry their
   own `.git` get it removed first; submodules go in with `git submodule add`.
5. **Stand up the backlog — the plane and the board both live in it.**
   - **The `backlog` CLI missing → say how to install it (`npm i -g backlog.md`, or `brew install
     backlog-md`) and stop.** Never improvise the store out of hand-written markdown; the CLI owns
     those files.
   - **`backlog init "<product>" --integration-mode none --defaults`**, run now so it uses the repo
     step 4 created. Its own agent integration would install a directive over every request in this
     product; the rules this command installs are what govern the store here, and two rule sets pulling
     in different directions is worse than either alone.
   - **Bring `backlog/config.yml` to the shape below — every key the CLI ships is in it, active or
     commented, so nothing about the store is a key someone has to go find in the CLI's own docs.**
     Keep the `project_name` and `task_prefix` init already wrote; `statuses` and `labels` are the two
     keys the CLI won't take as a flag or a `config set`, set here to what this harness needs — a
     `Backlog` column ahead of the CLI's own three, and the four origin labels declared so nothing
     depends on whoever types them first spelling them the same way. Every other key is left at the
     CLI's own default and commented out, there to uncomment rather than rediscover.
   - **Open no milestones.** The index starts empty; `/ask-me`, `/braindump` and `/propose-idea` fill
     it as the human affirms things.
   - **Install the rules this plugin ships.** Copy every file under the plugin's `rules/backlog/`
     (`find ~/.claude/plugins -path '*mycrew-product/rules/backlog/*.md'`) into the product's
     `.claude/rules/backlog/`, verbatim. A rule reworded on the way in is a second rule; a rule already
     sitting there is left exactly as it is, because the human may have edited it.
6. **Then stop.** No `git add`, no commit: say what you created — the root `CLAUDE.md`, the empty
   backlog, its columns and labels, the rules installed — and name the one command that shows it:
   `backlog browser` for the board in a browser, `backlog board` for it in the terminal.

## The root CLAUDE.md — the template

```markdown
# <product name>

## North Star
<the one guiding intent, in the human's own words — what this product exists for>

## Status
- **In production:** <yes | no>
<!-- yes = something is live and in use: every change must be safe and backward-compatible.
     no = greenfield: speed over caution. Every layer below weighs this in all work. -->

## Description
<what the product is as a whole — a synthesis, never the sub-projects' descriptions pasted together>

## Sub-projects
<!-- The declared list every mycrew layer reads instead of scanning for .git. -->
- **Layout:** <singlerepo | monorepo | polyrepo with submodules>
- `<path>` — <what it is and its role, one line>
- `<path>` — <…> <!-- add "not a build target" if no worker is ever dispatched into it: a charter, a
     spec bundle, a vendored reference. Without it the chief will try to build there. -->
```

## Config template

```yaml
project_name: "<as init wrote it>"
default_status: "To Do"
statuses: ["Backlog", "To Do", "In Progress", "Done"]
labels: ["from-human", "from-chief", "from-lead", "from-worker"]
date_format: yyyy-mm-dd
max_column_width: 20
auto_open_browser: true
default_port: 6420
remote_operations: true
auto_commit: false
filesystem_only: false
bypass_git_hooks: false
check_active_branches: true
active_branch_days: 30
task_prefix: "<as init wrote it>"
# hide_empty_columns: false             # hide board columns with no cards
# types: [bug, feature, enhancement, task, chore, docs, spike]  # allowed --type values
# default_assignee: []                  # assignees applied to new tasks created without -a
# definition_of_done:                   # default Definition of Done items added to every new task
#   - Tests pass
# priorities: ["High", "Medium", "Low"] # ordered priority labels, first sorts highest
# projects: ["web", "api"]              # allowed --project values for a monorepo backlog
# include_datetime_in_dates: true       # add time-of-day to new dates
# default_editor: "code --wait"         # editor opened by the 'E' key
# zero_padded_ids: true                 # pad task/doc/decision IDs with leading zeros
# on_status_change: "..."               # shell command run on every status change
```
