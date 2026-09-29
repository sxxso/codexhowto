#!/usr/bin/env bash
#
# Example Codex CLI `notify` hook.
#
# Wire it up in ~/.codex/config.toml:
#
#     notify = ["bash", "/home/you/.codex/notify.sh"]
#
# Codex runs this program when notable events occur (e.g. a turn finishes or
# Codex is blocked waiting for approval). It passes a JSON payload describing
# the event as the first argument. This script parses it and shows a desktop
# or terminal notification.
#
# Keep this script small and audited: it runs on your machine, with your
# permissions, OUTSIDE the Codex sandbox.

set -euo pipefail

# Codex passes the event as a JSON string in $1. Guard against an empty call.
payload="${1:-}"
if [[ -z "$payload" ]]; then
  # Some versions may pipe the payload on stdin instead of argv.
  payload="$(cat || true)"
fi

# Extract a couple of fields if `jq` is available; fall back to the raw string.
if command -v jq >/dev/null 2>&1 && [[ -n "$payload" ]]; then
  event_type="$(printf '%s' "$payload" | jq -r '.type // "codex-event"' 2>/dev/null || echo "codex-event")"
  message="$(printf '%s' "$payload" | jq -r '.message // .last_assistant_message // "Codex needs your attention"' 2>/dev/null || echo "Codex needs your attention")"
else
  event_type="codex-event"
  message="Codex: ${payload:-turn complete}"
fi

title="Codex (${event_type})"

# Try the native notifier for each platform, then fall back to a terminal bell.
if command -v terminal-notifier >/dev/null 2>&1; then          # macOS (brew)
  terminal-notifier -title "$title" -message "$message"
elif command -v osascript >/dev/null 2>&1; then                # macOS built-in
  osascript -e "display notification \"${message//\"/\\\"}\" with title \"${title//\"/\\\"}\""
elif command -v notify-send >/dev/null 2>&1; then              # Linux (libnotify)
  notify-send "$title" "$message"
elif command -v powershell.exe >/dev/null 2>&1; then           # Windows / WSL
  powershell.exe -NoProfile -Command "[console]::beep(880,300); Write-Host '$title: $message'"
else
  # Last resort: ring the terminal bell and print.
  printf '\a%s: %s\n' "$title" "$message"
fi

# Optional: also append to a log you can tail.
printf '%s\t%s\t%s\n' "$(date -Iseconds)" "$event_type" "$message" \
  >> "${CODEX_HOME:-$HOME/.codex}/notify.log" 2>/dev/null || true
