#!/usr/bin/env bash
# Post-process the generated schema.json to add README configurations
set -euo pipefail

SCHEMA_FILE="$1"

if [[ ! -f "$SCHEMA_FILE" ]]; then
    echo "Error: Schema file $SCHEMA_FILE not found"
    exit 1
fi

echo "Post-processing schema.json to add README configurations..."

# Use jq to add README configurations to the schema
jq '
    .language.csharp.packageReadmeFile = "README.md" |
    .language.nodejs.readme = "README.md" |
    .language.python.readme = "README.md"
' "$SCHEMA_FILE" > "${SCHEMA_FILE}.tmp"

mv "${SCHEMA_FILE}.tmp" "$SCHEMA_FILE"

echo "Schema post-processing completed"
