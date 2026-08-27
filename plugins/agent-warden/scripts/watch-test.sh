#!/usr/bin/env bash
# Self-check for watch.sh. Builds a throwaway board, runs the watcher against it,
# and asserts what it says and what it stays quiet about.
set -u
here=$(cd "$(dirname "$0")" && pwd)
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
mkdir -p "$T/tasks" "$T/state"
fail=0
pid=""

card() { cat > "$T/tasks/$1.md"; }
run() { # run <seconds> [command-to-run-midway]
  : >"$T/out"
  WARDEN_STATE="$T/state" bash "$here/watch.sh" "$T/tasks" 1 >"$T/out" 2>&1 & pid=$!
  sleep 1.5; [ $# -gt 1 ] && eval "$2"
  sleep "$1"; kill $pid 2>/dev/null; wait $pid 2>/dev/null; pid=""
}
want() { grep -q -- "$1" "$T/out" || { echo "MISSING: $1"; fail=1; }; }
deny() { grep -q -- "$1" "$T/out" && { echo "UNEXPECTED: $1"; fail=1; }; return 0; }

card clean <<'EOF'
---
id: CLEAN-1
status: In Progress
labels:
  - from-chief
milestone: F001 A feature
---
## Acceptance Criteria
- [x] #1 checked
EOF
card ungated <<'EOF'
---
id: UNG-1
status: In Progress
labels:
  - from-lead
milestone: F001 A feature
---
- [ ] #1 open
EOF
card gated <<'EOF'
---
id: GATE-1
status: In Progress
labels:
  - from-worker
  - gated
milestone: F001 A feature
---
- [ ] #1 open
EOF
card early <<'EOF'
---
id: EARLY-1
status: Done
labels:
  - from-human
milestone: F001 A feature
---
- [ ] #1 never checked
- [ ] #2 nor this
EOF
card noplan <<'EOF'
---
id: PLAN-1
status: To Do
labels:
  - from-human
---
- [ ] #1 open
EOF

# 1. Standing violations are reported the moment the watch comes up.
run 1
want "UNGATED UNG-1"
want "EARLYDONE EARLY-1 — done with 2 criteria unchecked"
want "NOPLAN PLAN-1"
deny "CLEAN-1"          # nothing wrong with it
deny "UNGATED GATE-1"   # agent-born but gated

# 2. A card that changes is announced; an untouched clean card stays silent.
run 2 "sed -i'' -e 's/^status: To Do/status: In Progress/' '$T/tasks/noplan.md'"
want "CARD PLAN-1 — In Progress"
want "NOPLAN PLAN-1"    # still serving no feature
deny "UNGATED PLAN-1"   # from-human is never gated, in progress or not
deny "CARD CLEAN-1"

# 3. A clean board says nothing at all.
rm "$T/tasks"/*.md; rm -f "$T/state"/*
card only <<'EOF'
---
id: OK-1
status: To Do
labels:
  - from-chief
milestone: F001 A feature
---
- [ ] #1 open
EOF
run 1
[ -s "$T/out" ] && { echo "UNEXPECTED: quiet board produced output:"; cat "$T/out"; fail=1; }

[ "$fail" = 0 ] && echo "watch.sh: ok" || { echo "watch.sh: FAILED"; exit 1; }
