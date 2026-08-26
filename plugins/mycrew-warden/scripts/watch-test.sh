#!/usr/bin/env bash
# Self-check for watch.sh: history stays silent, every event surfaces under its
# own name, and noise does not.
set -u
here=$(cd "$(dirname "$0")" && pwd)
T=$(mktemp -d)
mkdir -p "$T/tr" "$T/state"
A="$T/tr/aaaaaaaa-1111-2222-3333-444444444444.jsonl"
edit() { printf '{"type":"assistant","isSidechain":false,"message":{"content":[{"type":"tool_use","name":"Edit","input":{"file_path":"%s"}}]}}\n' "$1"; }

echo '{"type":"user","isMeta":false,"isSidechain":false,"message":{"content":"already said"}}' >"$A"
WARDEN_STATE="$T/state" bash "$here/watch.sh" "$T/tr" none 1 >"$T/out" 2>"$T/err" &
pid=$!; trap 'kill $pid 2>/dev/null; wait $pid 2>/dev/null; rm -rf "$T"' EXIT
sleep 2
{
  echo '{"type":"user","isMeta":false,"isSidechain":false,"message":{"content":"no, not like that"}}'
  echo '{"type":"user","isMeta":false,"isSidechain":false,"message":{"content":"<task-notification> <task-id>a123</task-id> <status>completed</status> </task-notification>"}}'
  echo '{"type":"user","isMeta":false,"isSidechain":false,"message":{"content":"<cross-session-message from=\"warden\">stop</cross-session-message>"}}'
  echo '{"type":"user","isSidechain":false,"message":{"content":[{"type":"tool_result","content":"out"}]}}'
  echo '{"type":"assistant","isSidechain":false,"message":{"content":[{"type":"tool_use","name":"Task","input":{"description":"rework auth","prompt":"rewrite the module"}}]}}'
  echo '{"type":"assistant","isSidechain":true,"message":{"content":[{"type":"tool_use","name":"Task","input":{"description":"sidechain","prompt":"must stay silent"}}]}}'
} >>"$A"
sleep 2
{ for _ in 1 2 3 4 5 6 7 8; do edit /repo/src/App.svelte; done; edit /repo/docs/product/notes.md; } >>"$A"
sleep 2
echo '{"type":"user","isMeta":false,"isSidechain":false,"message":{"content":"fresh session"}}' >"$T/tr/bbbbbbbb-1111-2222-3333-444444444444.jsonl"
sleep 2
kill $pid 2>/dev/null; wait $pid 2>/dev/null
out=$(cat "$T/out")

fail=0
want() { grep -q -- "$1" <<<"$out" || { echo "MISSING: $1"; fail=1; }; }
deny() { grep -q -- "$1" <<<"$out" && { echo "LEAKED: $1"; fail=1; }; }
want "HUMAN aaaaaaaa — no, not like that"
want "RETURN aaaaaaaa — task a123 completed"
want "DISPATCH aaaaaaaa — rework auth"
want "HANDSON aaaaaaaa"
want "CHURN aaaaaaaa — /repo/src/App.svelte ×8"
want "NEW bbbbbbbb"
want "HUMAN bbbbbbbb — fresh session"
deny "HUMAN aaaaaaaa — <task"   # a notification read as the human speaking
deny "already said"             # history from before the watch was armed
deny "cross-session"            # the warden's own flag coming back at it
deny "tool_result"              # tool output is not an event
deny "must stay silent"         # subagent traffic
deny "notes.md"                 # the plane is the chief's to edit
[ "$fail" = 0 ] && echo "watch.sh: ok" || { echo "watch.sh: FAILED"; exit 1; }
