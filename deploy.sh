#!/bin/bash
# ESGov Deploy Script
# Usage: ./deploy.sh "commit message" [version]
# Examples:
#   ./deploy.sh "Fix typo"          # keep current version
#   ./deploy.sh "Major update" v9.1 # bump to v9.1

set -e

cd "$(dirname "$0")"

MSG="${1:-Auto deploy}"
VERSION="${2}"

# 🛡️ Safety check: detect new HTML pages not yet approved
if [ -z "$SKIP_SAFETY" ]; then
  # Known allowed product HTML pages
  ALLOWED_PAGES="index.html shareholder-transfer/index.html sold-note-generator/index.html instrument-transfer-generator/index.html letter-of-transferee-generator/index.html nar1-generator/index.html nsc1-generator/index.html audit-report-generator/index.html"
  for f in *.html; do
    if ! echo "$ALLOWED_PAGES" | grep -q "$f"; then
      echo "⚠️  Unrecognised HTML page detected: $f"
      echo "   Run with SKIP_SAFETY=1 to bypass, or remove the file first."
      echo "   Aborting deploy."
      exit 1
    fi
  done
fi

# Get current version from index.html (format: vX.Y)
CURRENT_VER=$(grep -oP 'class="mt-2 opacity-40">\Kv[0-9]+\.[0-9]+' index.html | head -1)
NEW_VER="${VERSION:-$CURRENT_VER}"

if [ -z "$NEW_VER" ]; then
  echo "❌ Cannot detect current version"
  exit 1
fi

COMMIT=$(git log --oneline -1 | awk '{print $1}')
DATE=$(date '+%Y%m%d-%H%M')
VER_NUM="${NEW_VER#v}"  # strip v prefix for JSON

# Generate version.json
cat > version.json <<EOF
{
  "version": "${VER_NUM}",
  "commit": "${COMMIT}",
  "date": "$(date '+%Y-%m-%d')",
  "build": "${DATE}",
  "env": "github-pages"
}
EOF

# Update version badge in footers (inside the <p> tags only)
# Pattern: mt-2 opacity-40">vX.Y ...
sed -i "s|\\(mt-2 opacity-40\\\">\\)v[0-9.]\\+|\\1${NEW_VER}|g" index.html shareholder-transfer/index.html sold-note-generator/index.html instrument-transfer-generator/index.html letter-of-transferee-generator/index.html nar1-generator/index.html nsc1-generator/index.html audit-report-generator/index.html

git add -A
git commit -m "${MSG}"
git push

echo "✅ Deployed ${NEW_VER} (${COMMIT} @ ${DATE})"