#!/usr/bin/env bash
# Self-check for watch.sh: history stays silent, every event surfaces under its
# own name, noise does not, and WARDEN_ONLY keeps unmatched sessions unwatched.
set -u
here=$(cd "$(dirname "$0")" && pwd)
T=$(mktemp -d); pid=""
trap '[ -n "$pid" ] && kill $pid 2>/dev/null; wait $pid 2>/dev/null; rm -rf "$T"' EXIT
fail=0
human() { printf '{"type":"user","isMeta":false,"isSidechain":false,"message":{"content":"%s"}}\n' "$1"; }
edit()  { printf '{"type":"assistant","isSidechain":false,"message":{"content":[{"type":"tool_use","name":"Edit","input":{"file_path":"%s"}}]}}\n' "$1"; }
want()  { grep -q -- "$1" <<<"$out" || { echo "MISSING: $1"; fail=1; }; }
deny()  { grep -q -- "$1" <<<"$out" && { echo "LEAKED: $1"; fail=1; }; }

## every session watched
mkdir -p "$T/a/tr" "$T/a/state"
A="$T/a/tr/aaaaaaaa-1111-2222-3333-444444444444.jsonl"
human "already said" >"$A"
WARDEN_STATE="$T/a/state" bash "$here/watch.sh" "$T/a/tr" none 1 >"$T/a/out" 2>&1 & pid=$!
sleep 2
{
  human "no, not like that"
  human "<task-notification> <task-id>a123</task-id> <status>completed</status> </task-notification>"
  human "<cross-session-message from=\\\"warden\\\">stop</cross-session-message>"
  echo '{"type":"user","isSidechain":false,"message":{"content":[{"type":"tool_result","content":"out"}]}}'
  echo '{"type":"assistant","isSidechain":false,"message":{"content":[{"type":"tool_use","name":"Task","input":{"description":"rework auth","prompt":"rewrite the module"}}]}}'
  echo '{"type":"assistant","isSidechain":true,"message":{"content":[{"type":"tool_use","name":"Task","input":{"description":"sidechain","prompt":"must stay silent"}}]}}'
} >>"$A"
sleep 2
{ for _ in 1 2 3 4 5 6 7 8; do edit /repo/src/App.svelte; done; edit /repo/docs/product/notes.md; } >>"$A"
sleep 2
human "fresh session" >"$T/a/tr/bbbbbbbb-1111-2222-3333-444444444444.jsonl"
sleep 2
kill $pid 2>/dev/null; wait $pid 2>/dev/null; pid=""
out=$(cat "$T/a/out")
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

## WARDEN_ONLY narrows it
mkdir -p "$T/b/tr" "$T/b/state"
WARDEN_STATE="$T/b/state" WARDEN_ONLY='mycrew-developers:chief' bash "$here/watch.sh" "$T/b/tr" none 1 >"$T/b/out" 2>&1 & pid=$!
sleep 2
human "plain work nobody watches" >"$T/b/tr/cccccccc-1111-2222-3333-444444444444.jsonl"
{ human "run the product"
  echo '{"type":"agent-setting","agentSetting":"mycrew-developers:chief"}'
  human "carry F004 next"
} >"$T/b/tr/dddddddd-1111-2222-3333-444444444444.jsonl"
sleep 3
kill $pid 2>/dev/null; wait $pid 2>/dev/null; pid=""
out=$(cat "$T/b/out")
want "ATTACH dddddddd"
want "HUMAN dddddddd — carry F004 next"
deny "cccccccc"                 # never ran the chief, never watched
deny "NEW dddddddd"             # taken up, not merely noticed

[ "$fail" = 0 ] && echo "watch.sh: ok" || { echo "watch.sh: FAILED"; exit 1; }
