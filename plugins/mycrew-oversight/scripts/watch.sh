#!/usr/bin/env bash
# Eyes for the overseer. Polls in the shell so waking costs nothing; prints one
# line per event worth a verdict. Every line becomes one Monitor notification.
#
# usage: watch.sh <transcript-dir> <own-session-id> [poll-seconds]
#   transcript-dir  ~/.claude/projects/<slug> for the project being watched
#   own-session-id  the overseer's own session, never watched
set -u

DIR=${1:?transcript dir}
SELF=${2:?own session id}
POLL=${3:-5}
CAP=6
STATE=${OVERSIGHT_STATE:-$PWD/.claude/oversight/.cursors}
mkdir -p "$STATE"

FILTER='
select(.isSidechain != true)
| if .type == "user" and (.isMeta | not) and (.message.content | type == "string")
     and (.message.content | test("^<(local-command|command-name|cross-session-message)") | not)
  then "HUMAN \($s) — \(.message.content | gsub("\\s+"; " ") | .[0:400])"
  elif .type == "assistant"
  then ( .message.content[]?
         | select(.type == "tool_use" and (.name == "Task" or .name == "Agent"))
         | "DISPATCH \($s) — \(.input.description // .input.subagent_type // "?") :: \((.input.prompt // "") | gsub("\\s+"; " ") | .[0:400])" )
  else empty end'

first=1
while :; do
  for f in "$DIR"/*.jsonl; do
    [ -e "$f" ] || continue
    id=$(basename "$f" .jsonl)
    [ "$id" = "$SELF" ] && continue
    total=$(wc -l <"$f" | tr -d ' ')
    if [ ! -f "$STATE/$id" ]; then
      # At startup every session is already mid-flight: take its history as read.
      if [ "$first" = 1 ]; then echo "$total" >"$STATE/$id"; continue; fi
      echo "NEW ${id:0:8} — a session appeared in this project"
      echo 0 >"$STATE/$id"
    fi
    cur=$(cat "$STATE/$id")
    [ "$total" -le "$cur" ] && continue
    out=$(head -n "$total" "$f" | tail -n "+$((cur+1))" \
          | jq -r --arg s "${id:0:8}" "$FILTER" 2>/dev/null)
    echo "$total" >"$STATE/$id"
    [ -z "$out" ] && continue
    n=$(printf '%s\n' "$out" | wc -l | tr -d ' ')
    printf '%s\n' "$out" | head -n "$CAP"
    [ "$n" -gt "$CAP" ] && echo "MORE ${id:0:8} — $((n - CAP)) further events this tick, unshown"
  done
  first=0
  sleep "$POLL"
done
