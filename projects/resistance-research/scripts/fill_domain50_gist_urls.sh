#!/bin/bash
# Domain 50 Gist URL Filler
# Usage: ./fill_domain50_gist_urls.sh "https://gist.github.com/esca8peArtist/abc123..."
# This script replaces all [INSERT GIST URL HERE] placeholders with the provided Gist URL

set -e

if [ -z "$1" ]; then
    echo "❌ Usage: $0 <gist-url>"
    echo ""
    echo "Example: $0 'https://gist.github.com/esca8peArtist/abc123def456'"
    exit 1
fi

GIST_URL="$1"
TARGET_DIR="/home/awank/dev/SuperClaude_Framework/projects/resistance-research"

# Verify the Gist URL looks valid
if [[ ! "$GIST_URL" =~ ^https://gist\.github\.com/ ]]; then
    echo "❌ Invalid Gist URL: must start with https://gist.github.com/"
    exit 1
fi

echo "🔍 Searching for files containing [INSERT GIST URL HERE]..."
FILES_TO_UPDATE=$(grep -r "INSERT GIST URL" "$TARGET_DIR" --files-with-matches)

if [ -z "$FILES_TO_UPDATE" ]; then
    echo "✅ No placeholders found — all Domain 50 URLs already filled!"
    exit 0
fi

echo ""
echo "📝 Files to update:"
echo "$FILES_TO_UPDATE" | sed 's/^/  - /'

echo ""
echo "🔄 Replacing [INSERT GIST URL HERE] with: $GIST_URL"
echo ""

# Update each file
for FILE in $FILES_TO_UPDATE; do
    COUNT=$(grep -c "INSERT GIST URL" "$FILE" || true)
    sed -i "s|\[INSERT GIST URL HERE\]|$GIST_URL|g" "$FILE"
    echo "✅ $FILE — $COUNT placeholder(s) replaced"
done

echo ""
echo "🎉 All placeholders replaced!"
echo ""
echo "Next steps:"
echo "  1. Review the updated files to confirm URLs are correct"
echo "  2. Commit the changes:"
echo "     git add projects/resistance-research/SCOTUS_*.md"
echo "     git commit -m 'chore(resistance-research): Domain 50 Gist URL filled in'"
echo "  3. Execute the SCOTUS rapid-response framework if decision is announced"
