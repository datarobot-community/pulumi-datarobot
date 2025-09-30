#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")"; pwd)"
TEMPLATES_DIR="$ROOT/templates"

# Get version from provider
VERSION_FILE="$ROOT/provider/cmd/pulumi-resource-datarobot/version.txt"
if [[ -f "$VERSION_FILE" ]]; then
  VERSION="$(cat "$VERSION_FILE" | tr -d '\n')"
else
  VERSION="$(git describe --tags --abbrev=0 2>/dev/null || echo 'dev')"
fi

# SDK configurations using arrays (compatible with older bash)
SDKS=(python nodejs go dotnet)
PACKAGES=(
  "pulumi_datarobot"
  "@datarobot/pulumi-datarobot"
  "github.com/datarobot-community/pulumi-datarobot/sdk/go/datarobot"
  "DataRobotPulumi.Datarobot"
)

echo "Applying SDK-specific READMEs (version: $VERSION)"

for i in "${!SDKS[@]}"; do
  sdk="${SDKS[$i]}"
  package_name="${PACKAGES[$i]}"
  template_file="$TEMPLATES_DIR/README.$sdk.md"
  sdk_dir="$ROOT/sdk/$sdk"
  target_file="$sdk_dir/README.md"

  if [[ ! -f "$template_file" ]]; then
    echo "WARN: Template $template_file not found - skipping $sdk"
    continue
  fi

  if [[ ! -d "$sdk_dir" ]]; then
    echo "WARN: SDK directory $sdk_dir not found - skipping $sdk"
    continue
  fi

  echo "  $sdk: $template_file -> $target_file"

  # Replace template variables
  sed -e "s/{{VERSION}}/$VERSION/g" \
      -e "s|{{PACKAGE_NAME}}|$package_name|g" \
      -e "s|{{EXAMPLES_PATH}}|examples/$sdk|g" \
      "$template_file" > "$target_file"
done

echo "SDK READMEs applied successfully"
