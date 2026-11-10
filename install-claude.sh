#!/bin/sh
# Install or update the i-am-overwhelmed plugin for Claude Code, then check it.
# Usage: install-claude.sh          install or update, then check
#        install-claude.sh --check  only check
set -eu

MARKET=jinhuang712/i-am-overwhelmed
PLUGIN=i-am-overwhelmed@i-am-overwhelmed

if ! command -v claude >/dev/null 2>&1; then
  echo "Claude Code is missing: 'claude' is not on your PATH." >&2
  exit 1
fi

if [ "${1:-}" != "--check" ]; then
  # "add" and "install" succeed without a change when the thing is already
  # there, so the update always runs after them.
  # A failed "add" stays quiet: the update below reports a real problem.
  claude plugin marketplace add "$MARKET" >/dev/null 2>&1 || true
  claude plugin marketplace update i-am-overwhelmed
  claude plugin install "$PLUGIN" || true
  claude plugin update "$PLUGIN"
fi

# Read the plugin's version and status from the list of installed plugins.
found=$(claude plugin list | awk -v plugin="$PLUGIN" '
  seen && /Version:/ { version = $2 }
  seen && /Status:/  { sub(/^ *Status: */, ""); status = $0; exit }
  index($0, plugin)  { seen = 1 }
  END { if (seen) print version " " status }')

case "$found" in
  "")
    echo "Check failed: $PLUGIN is missing from 'claude plugin list'." >&2
    exit 1 ;;
  *disabled*)
    echo "Installed, version ${found%% *}, but disabled. Run: claude plugin enable $PLUGIN" >&2
    exit 1 ;;
  *)
    echo "Installed and enabled, version ${found%% *}. Restart Claude Code and the output style turns on by itself." ;;
esac
