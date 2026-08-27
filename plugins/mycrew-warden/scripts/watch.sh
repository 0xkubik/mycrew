#!/usr/bin/env bash
# Eyes for the warden. Polls in the shell so waking costs nothing; prints one
# line per event worth a verdict. Every line becomes one Monitor notification.
#
# usage: watch.sh <transcript-dir> <own-session-id> [poll-seconds]
#   transcript-dir  ~/.claude/projects/<slug> for the project being watched
#   own-session-id  the warden's own session, never watched
#
# WARDEN_ONLY narrows the watch: a session is taken up only once it is running
# as, or has invoked, something matching that regex — e.g. mycrew-developers:chief.
# Unset watches everything.
set -u

DIR=${1:?transcript dir}
SELF=${2:?own session id}
POLL=${3:-5}
CAP=6
# ponytail: edit counts are cumulative and never decay, so a file touched slowly
# over days eventually speaks; add a time window if the false wakes get annoying.
CHURN=${WARDEN_CHURN:-8}
ONLY=${WARDEN_ONLY:-}
STATE=${WARDEN_STATE:-$PWD/.claude/warden/.cursors}
mkdir -p "$STATE"

FILTER='
select(.isSidechain != true)
| if .type == "user" and (.isMeta | not) and (.message.content | type == "string")
  then ( .message.content as $c
       | if ($c | test("^<task-notification"))
         then "RETURN \($s) — task \(($c | [scan("<task-id>([^<]*)</task-id>")] | flatten | first) // "?") \(($c | [scan("<status>([^<]*)</status>")] | flatten | first) // "")"
         elif ($c | test("^<(local-command|command-name|cross-session-message|system-reminder)"))
         then empty
         else "HUMAN \($s) — \($c | gsub("\\s+"; " ") | .[0:400])" end )
  elif .type == "assistant"
  then ( .message.content[]?
         | select(.type == "tool_use" and (.name == "Task" or .name == "Agent"))
         | "DISPATCH \($s) — \(.input.description // .input.subagent_type // "?") :: \((.input.prompt // "") | gsub("\\s+"; " ") | .[0:400])" )
  else empty end'

# What the session is running as, and what it has invoked. WARDEN_ONLY is matched
# against this and never against the prose, so naming a thing cannot summon the watch.
IDENT='
if .type == "agent-setting" then .agentSetting
elif .type == "user" and (.message.content | type == "string")
then (.message.content | [scan("<command-name>([^<]*)</command-name>")] | flatten | .[]?)
else empty end'

# Files the plane keeps are not the work — a chief editing them is doing its job.
EDITS='
select(.isSidechain != true and .type == "assistant")
| .message.content[]?
| select(.type == "tool_use" and (.name == "Edit" or .name == "Write" or .name == "MultiEdit"))
| .input.file_path // empty'

first=1
while :; do
  for f in "$DIR"/*.jsonl; do
    [ -e "$f" ] || continue
    id=$(basename "$f" .jsonl)
    [ "$id" = "$SELF" ] && continue
    total=$(wc -l <"$f" | tr -d ' ')
    fresh=0
    if [ ! -f "$STATE/$id" ]; then
      # At startup every session is already mid-flight: take its history as read.
      if [ "$first" = 1 ]; then echo "$total" >"$STATE/$id"; continue; fi
      fresh=1
      echo 0 >"$STATE/$id"
    fi
    cur=$(cat "$STATE/$id")
    [ "$total" -le "$cur" ] && continue
    new=$(head -n "$total" "$f" | tail -n "+$((cur+1))")
    echo "$total" >"$STATE/$id"
    [ -z "$new" ] && continue

    out=""
    if [ -n "$ONLY" ] && [ ! -f "$STATE/$id.on" ]; then
      hit=$(printf '%s\n' "$new" | jq -r "$IDENT" 2>/dev/null | grep -E "$ONLY" | head -1)
      # Nothing it is or has run matches: the delta is read and dropped, unwatched.
      [ -z "$hit" ] && continue
      : >"$STATE/$id.on"
      out="ATTACH ${id:0:8} — taken up, running or invoking $hit"
      fresh=0
    fi
    [ "$fresh" = 1 ] && out="NEW ${id:0:8} — a session appeared in this project"

    out=$(printf '%s\n%s' "$out" "$(printf '%s\n' "$new" | jq -r --arg s "${id:0:8}" "$FILTER" 2>/dev/null)")
    printf '%s\n' "$out" | grep -q '^DISPATCH ' && : >"$STATE/$id.dispatched"

    paths=$(printf '%s\n' "$new" | jq -r "$EDITS" 2>/dev/null | grep -vE '/(docs|\.claude)/' || true)
    if [ -n "$paths" ]; then
      if [ -f "$STATE/$id.dispatched" ] && [ ! -f "$STATE/$id.handson" ]; then
        : >"$STATE/$id.handson"
        out="$out
HANDSON ${id:0:8} — the session that dispatches workers is now editing files itself"
      fi
      churn=$(printf '%s\n' "$paths" | awk -v st="$STATE/$id.edits" -v n="$CHURN" -v s="${id:0:8}" '
        BEGIN { while ((getline l < st) > 0) { i = index(l, "\t"); c[substr(l, i + 1)] = substr(l, 1, i - 1) } close(st) }
        { was = c[$0] + 0; c[$0] = was + 1
          if (int((was + 1) / n) > int(was / n)) print "CHURN " s " — " $0 " ×" (was + 1) }
        END { printf "" > st; for (p in c) printf "%d\t%s\n", c[p], p > st }')
      [ -n "$churn" ] && out="$out
$churn"
    fi

    out=$(printf '%s\n' "$out" | grep -v '^$' || true)
    [ -z "$out" ] && continue
    n=$(printf '%s\n' "$out" | wc -l | tr -d ' ')
    printf '%s\n' "$out" | head -n "$CAP"
    [ "$n" -gt "$CAP" ] && echo "MORE ${id:0:8} — $((n - CAP)) further events this tick, unshown"
  done
  first=0
  sleep "$POLL"
done
