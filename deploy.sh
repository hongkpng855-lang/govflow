#!/bin/bash
# GovFlow Deploy Script
# Usage: ./deploy.sh "commit message"
# Generates version.json with git hash, then commits & pushes

set -e

MSG="${1:-Auto deploy}"
cd "$(dirname "$0")"

# Generate version
COMMIT=$(git log --oneline -1 | awk '{print $1}')
DATE=$(date '+%Y%m%d-%H%M')
cat > version.json <<EOF
{
  "version": "1.0.0",
  "commit": "${COMMIT}",
  "date": "$(date '+%Y-%m-%d')",
  "build": "${DATE}",
  "env": "github-pages"
}
EOF

# Update version badge in footers
sed -i "s/v[0-9.]\+ \?· [a-f0-9]\+/v1.0.0 · ${COMMIT}/g" index.html shareholder-transfer.html

git add -A
git commit -m "${MSG}"
git push

echo "✅ Deployed (${COMMIT} @ ${DATE})"
