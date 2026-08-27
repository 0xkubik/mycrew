#!/usr/bin/env bash
# Eyes for the warden. Watches the board, not the sessions: a card only changes
# when someone actually did something, so waking is rare and every wake has a
# subject. Polls in the shell; each stdout line becomes one Monitor notification.
#
# usage: watch.sh <board-tasks-dir> [poll-seconds]
#   board-tasks-dir  backlog/tasks of the product being watched
#
# Lines it prints:
#   CARD <id> <status> — the card changed
#   UNGATED <id>       — agent-born work in progress that never passed the gate
#   NOPLAN <id>        — a card serving no feature
#   EARLYDONE <id>     — done with criteria still unchecked
#   STALE <id> <days>  — in progress and untouched for too long
set -u

DIR=${1:?board tasks dir}
POLL=${2:-5}
STALE=${WARDEN_STALE_DAYS:-2}
CAP=${WARDEN_CAP:-8}
STATE=${WARDEN_STATE:-$PWD/.claude/warden/.cursors}
mkdir -p "$STATE"

# Everything a verdict needs, read out of one card in one pass.
read_card() {
  awk '
    NR == 1 && $0 == "---" { fm = 1; next }
    fm && $0 == "---" { fm = 0; next }
    fm && /^status:/ { sub(/^status:[ ]*/, ""); status = $0 }
    fm && /^milestone:/ { sub(/^milestone:[ ]*/, ""); milestone = $0 }
    fm && /^labels:/ { inl = 1; next }
    fm && inl && /^  - / { sub(/^  - /, ""); labels = labels "," $0; next }
    fm && inl && /^[a-z]/ { inl = 0 }
    !fm && /^- \[ \] #/ { open++ }
    END { printf "%s\034%s\034%s\034%d\n", status, milestone, labels, open }
  ' "$1"
}

judge() {
  local id=$1 status=$2 milestone=$3 labels=$4 open=$5 file=$6
  [ -z "$milestone" ] && echo "NOPLAN $id — serves no feature"
  case "$status" in
    "In Progress")
      case ",$labels," in
        *,from-lead,*|*,from-worker,*)
          case ",$labels," in *,gated,*) ;; *) echo "UNGATED $id — agent-born work in progress, never gated" ;; esac ;;
      esac
      if [ -n "$(find "$file" -mtime +"$STALE" 2>/dev/null)" ]; then
        echo "STALE $id — in progress, untouched $STALE+ days"
      fi ;;
    Done)
      [ "$open" -gt 0 ] && echo "EARLYDONE $id — done with $open criteria unchecked" ;;
  esac
}

first=1
while :; do
  out=""
  for f in "$DIR"/*.md; do
    [ -e "$f" ] || continue
    id=$(sed -n 's/^id:[ ]*//p' "$f" | head -1); [ -z "$id" ] && continue
    sum=$(cksum <"$f" | cut -d' ' -f1)
    prev=""; [ -f "$STATE/$id" ] && prev=$(cat "$STATE/$id")
    echo "$sum" >"$STATE/$id"

    # \034 and not a tab: bash folds runs of whitespace in IFS, so an empty
  # milestone would silently shift every field after it.
  IFS=$'\034' read -r status milestone labels open <<<"$(read_card "$f")"
    # At startup the board is already mid-flight: take its state as read, but a
    # violation standing right now is news whether or not anyone just touched it.
    if [ "$first" = 1 ]; then
      out="$out
$(judge "$id" "$status" "$milestone" "$labels" "$open" "$f")"
      continue
    fi
    [ "$sum" = "$prev" ] && { out="$out
$(judge "$id" "$status" "$milestone" "$labels" "$open" "$f" | grep '^STALE ' || true)"; continue; }
    out="$out
CARD $id — $status
$(judge "$id" "$status" "$milestone" "$labels" "$open" "$f")"
  done
  first=0
  out=$(printf '%s\n' "$out" | grep -v '^$' || true)
  if [ -n "$out" ]; then
    n=$(printf '%s\n' "$out" | wc -l | tr -d ' ')
    printf '%s\n' "$out" | head -n "$CAP"
    [ "$n" -gt "$CAP" ] && echo "MORE — $((n - CAP)) further board events this tick, unshown"
  fi
  sleep "$POLL"
done
