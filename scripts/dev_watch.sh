#!/usr/bin/env bash
# Local-only dev helper: rebuilds on every change to build/generate.py or
# the asset files it reads, then appends a tiny polling script to the
# dist/ output so an already-open browser tab reloads automatically.
#
# NOT part of the committed build — generate.py's own output never
# includes this script, so it can't leak into what actually gets
# deployed. This just post-processes the local dist/ copy after each
# build, for convenience while iterating in this session.
set -euo pipefail
cd "$(dirname "$0")/.."

RELOAD_SNIPPET='<script>(function(){var last=null;setInterval(function(){fetch("/.reload?t="+Date.now()).then(function(r){return r.text()}).then(function(t){if(last===null){last=t;return}if(t!==last){location.reload()}}).catch(function(){})},1000)})();</script>'

build_and_inject() {
  python3 build/generate.py
  date +%s > dist/.reload
  for f in dist/index.html dist/menu.html; do
    printf '%s\n' "$RELOAD_SNIPPET" >> "$f"
  done
  echo "[dev_watch] rebuilt at $(date '+%H:%M:%S')"
}

hash_sources() {
  find build -type f \( -name '*.py' -o -name '*.b64' -o -name '*.js' \) -exec stat -f '%m %N' {} \; 2>/dev/null | sort | shasum | awk '{print $1}'
}

build_and_inject
last_hash=$(hash_sources)

while true; do
  cur_hash=$(hash_sources)
  if [ "$cur_hash" != "$last_hash" ]; then
    last_hash="$cur_hash"
    build_and_inject || echo "[dev_watch] build failed, waiting for next change"
  fi
  sleep 1
done
