#!/usr/bin/env bash
# Pull-based auto-deploy for the VPS. Cron runs this every 5 minutes; it does nothing unless
# origin/main has a commit that has not been deployed yet.
#
#   push to GitHub  ->  (within 5 min) VPS fetches, fast-forwards, rebuilds, runs db/apply.sh
#
# No secrets involved: the repo is public, so the VPS only needs to read it.
#
# Usage on the VPS:
#   bash deploy/auto-deploy.sh            # deploy if origin/main is new (what cron runs)
#   bash deploy/auto-deploy.sh --init     # mark the current commit as deployed, deploy nothing
#   bash deploy/auto-deploy.sh --force    # deploy origin/main now, even if it failed before
#   bash deploy/auto-deploy.sh --status   # show deployed / remote / failed commits
#
# A commit whose deploy fails is tried once only; it is retried on the next push or with --force.
# Log (when installed with the cron line in the README): /var/log/rigconfigurator-deploy.log
set -uo pipefail

# Everything runs inside main() so bash has read the whole file before a deploy replaces it.
main() {
  export PATH="$PATH:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

  REPO="${REPO:-/docker/rigconfigurator}"
  BRANCH="${BRANCH:-main}"
  STATE="$REPO/.deploy-state"
  local MODE="${1:-}"

  log() { echo "$(date -u +%FT%TZ) $*"; }

  cd "$REPO" || { log "repo not found: $REPO"; exit 1; }
  mkdir -p "$STATE"

  # one run at a time; a build can outlast the 5-minute cron interval
  exec 9>"$STATE/lock"
  flock -n 9 || exit 0

  short() { echo "${1:0:7}"; }
  deployed="$(cat "$STATE/deployed" 2>/dev/null || true)"
  failed="$(cat "$STATE/failed" 2>/dev/null || true)"

  if [ "$MODE" = "--init" ]; then
    git rev-parse HEAD > "$STATE/deployed"; rm -f "$STATE/failed"
    log "init: marked $(short "$(cat "$STATE/deployed")") as deployed"
    exit 0
  fi

  git fetch --quiet origin "$BRANCH" || { log "git fetch failed"; exit 1; }
  remote="$(git rev-parse "origin/$BRANCH")"

  if [ "$MODE" = "--status" ]; then
    echo "deployed: ${deployed:-none}"; echo "remote:   $remote"; echo "failed:   ${failed:-none}"; echo "HEAD:     $(git rev-parse HEAD)"
    exit 0
  fi

  [ "$MODE" = "--force" ] && { failed=""; deployed=""; }
  [ "$remote" = "$deployed" ] && exit 0
  [ "$remote" = "$failed" ] && exit 0

  log "deploying $(short "$remote") (deployed: $(short "${deployed:-none}"))"
  if git merge --ff-only --quiet "origin/$BRANCH" \
     && docker compose up -d --build \
     && bash db/apply.sh; then
    echo "$remote" > "$STATE/deployed"; rm -f "$STATE/failed"
    log "OK $(short "$remote")"
  else
    echo "$remote" > "$STATE/failed"
    log "FAILED $(short "$remote"): fix the cause, then run: bash deploy/auto-deploy.sh --force"
    exit 1
  fi
}

main "$@"
