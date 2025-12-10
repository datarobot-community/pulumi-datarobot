# DataRobot Resource Provider

The DataRobot Resource Provider lets you manage [DataRobot](https://www.datarobot.com/) resources.
The provider is built on [terraform-provider-datarobot](https://github.com/datarobot-community/terraform-provider-datarobot).
To use this package, please install the [Pulumi CLI](https://pulumi.io/) first.

## Installing

This package is available for several languages/platforms:

- Python: [`pulumi-datarobot`](https://pypi.org/project/pulumi-datarobot/)
- JavaScript/TypeScript: [`@datarobot/pulumi-datarobot`](https://www.npmjs.com/package/@datarobot/pulumi-datarobot)
- Go: [`github.com/datarobot-community/pulumi-datarobot/sdk`](https://pkg.go.dev/github.com/datarobot-community/pulumi-datarobot/sdk)
- .NET: [`DataRobotPulumi.Datarobot`](https://www.nuget.org/packages/DataRobotPulumi.Datarobot)

### Python

To use from Python, install using `pip`:

```bash
pip install pulumi_datarobot
```

### Javascript/Typescript

To use from JavaScript or TypeScript in Node.js, install using either `npm`:

```bash
npm install @datarobot/pulumi-datarobot
```

or `yarn`:

```bash
yarn add @datarobot/pulumi-datarobot
```

### Go

```
go get github.com/datarobot-community/pulumi-datarobot/sdk/go/...
```

### .NET

To use from .NET, install using `dotnet add package`:

```
dotnet add package DataRobotPulumi.Datarobot
```

### YAML

No install necessary, just run `pulumi up`.

## Configuration

The following configuration points are available for the DataRobot provider:

- `datarobot:apikey` (environment: `DATAROBOT_API_TOKEN`) - the API key for DataRobot
- `datarobot:endpoint` (environment: `DATAROBOT_ENDPOINT`) - the endpoint for DataRobot

## Examples

See [datarobot-pulumi examples](https://github.com/datarobot-community/pulumi-datarobot/tree/main/examples)

## Air-Gapped Environments

Keep the following items in mind if running in an air-gapped environment:

- Run `pulumi login --local` to store state files on your local filesystem, instead of the default Pulumi Cloud. Pulumi binaries are available [here](https://www.pulumi.com/docs/iac/download-install/).
- Set `DATAROBOT_ENDPOINT`: https://{datarobot.example.com}/api/v2
    (replacing {datarobot.example.com} with your specific deployment endpoint)
- For Python, the [pulumi](https://pypi.org/project/pulumi/) and [pulumi-datarobot](https://pypi.org/project/pulumi-datarobot/) packages must be installed in the air-gapped system.

    Example using `pip wheel`:

    1. create a directory where you want to store package wheels.

    ```bash
    mkdir folder_containing_wheel
    ```

    2. Now install wheels of the python library you want to install

    ```bash
    pip wheel pulumi-datarobot -w folder_containing_wheel
    ```

    This will store all your required dependent wheels of the `pulumi-datarobot` package in the folder. you can check it with doing ls -ltr`.

    3. Now, you can make a tar file of this folder.

    ```bash
    tar cf folder_containing_wheel.tar folder_containing_wheel/
    ```

    and you can transfer it to your air-gapped system.

    Now untar the folder.

    ```bash
    tar xf folder_containing_wheel.tar
    cd folder_containing_wheel/
    ```

    now install wheels from the folder.

    ```bash
    pip install * -f ./ --no-index
    ```

You will also need to download the binary plugin from this repository. Click on the version that matches the Python package
version from our [Releases](https://github.com/datarobot-community/pulumi-datarobot/releases) page, download the tar.gz
for the correct architecture of your computer. For Codespaces, that is `*-linux-amd64.tar.gz`. After you've extracted it
install it with:

```bash
pulumi plugin install resource datarobot <version> -f <path-to-extracted-folder>
```
---

## Custom Plugin Download Locations

If you need to host the pulumi-datarobot plugin in your own artifact repository or air-gapped environment, you can use Pulumi's `PLUGIN_DOWNLOAD_URL_OVERRIDES` environment variable to redirect plugin downloads to your custom location.

### Basic Usage

The `PLUGIN_DOWNLOAD_URL_OVERRIDES` environment variable allows you to override plugin download URLs using regular expressions. The format is:

```
PLUGIN_DOWNLOAD_URL_OVERRIDES="regexp=URL"
```

Multiple overrides can be specified by separating them with commas:

```
PLUGIN_DOWNLOAD_URL_OVERRIDES="regexp1=URL1,regexp2=URL2"
```

### Redirecting DataRobot Plugin Downloads

The pulumi-datarobot plugin is hosted on GitHub at:
```
github://api.github.com/datarobot-community/pulumi-datarobot
```

#### Example 1: Redirect to Your Internal Artifactory

To redirect all DataRobot plugin downloads to your internal artifact repository:

```bash
export PLUGIN_DOWNLOAD_URL_OVERRIDES="^github://api.github.com/datarobot-community/pulumi-datarobot=https://artifactory.yourcompany.com/pulumi/datarobot"
```

Your artifact repository should host the plugin binaries with the same structure as GitHub releases. For example, for version v0.10.26, the plugin binary should be available at:
```
https://artifactory.yourcompany.com/pulumi/datarobot/pulumi-resource-datarobot-v0.10.26-darwin-amd64.tar.gz
https://artifactory.yourcompany.com/pulumi/datarobot/pulumi-resource-datarobot-v0.10.26-linux-amd64.tar.gz
https://artifactory.yourcompany.com/pulumi/datarobot/pulumi-resource-datarobot-v0.10.26-windows-amd64.tar.gz
```

#### Example 2: Redirect All GitHub Plugins

To redirect all GitHub-hosted plugins to your internal mirror:

```bash
export PLUGIN_DOWNLOAD_URL_OVERRIDES="^github://=https://internal-mirror.yourcompany.com/github-plugins/"
```

#### Example 3: Using Named Capture Groups

You can use named regular expression groups to dynamically build redirect URLs. This is useful for maintaining the same folder structure in your artifact repository:

```bash
export PLUGIN_DOWNLOAD_URL_OVERRIDES="^github://api.github.com/(?P<org>[^/]+)/(?P<repo>[^/]+)=https://artifactory.yourcompany.com/pulumi/\${org}/\${repo}"
```

With this configuration, the DataRobot plugin would be downloaded from:
```
https://artifactory.yourcompany.com/pulumi/datarobot-community/pulumi-datarobot
```

You can also use numeric capture groups like `$1`, `$2`, etc.:

```bash
export PLUGIN_DOWNLOAD_URL_OVERRIDES="^github://api.github.com/([^/]+)/([^/]+)=https://artifactory.yourcompany.com/pulumi/$1/$2"
```

#### Example 4: Air-Gapped Environment with Local File Server

For completely air-gapped environments, you can host plugins on a local HTTP server:

```bash
export PLUGIN_DOWNLOAD_URL_OVERRIDES="^github://api.github.com/datarobot-community/pulumi-datarobot=http://local-server.internal/pulumi-plugins/datarobot"
```

### Setting Up Your Artifact Repository

When hosting the DataRobot plugin in your own repository:

1. **Download the plugin binaries** from the [official releases page](https://github.com/datarobot-community/pulumi-datarobot/releases)

2. **Upload to your artifact repository** maintaining the naming convention:
   ```
   pulumi-resource-datarobot-v{VERSION}-{OS}-{ARCH}.tar.gz
   ```

3. **Ensure proper permissions** so that your CI/CD systems and developers can access the repository

4. **Set the environment variable** in your CI/CD configuration, container images, or developer setup scripts

### Testing Locally with Artifactory

Here's a step-by-step guide to test plugin download overrides with your Artifactory instance.

#### Step 1: Set Up a Generic Repository in Artifactory

Pulumi plugins are binary `.tar.gz` files, so you need a **generic** (raw) repository in Artifactory, not PyPI. Create a repository path like:
```
https://artifactory.infra.io/artifactory/pulumi-plugins/datarobot/
```

#### Step 2: Download and Upload Plugin Binaries

```bash
# Download the plugin binary for your platform from GitHub releases
VERSION="v0.10.26"

# For macOS (Intel)
curl -LO "https://github.com/datarobot-community/pulumi-datarobot/releases/download/${VERSION}/pulumi-resource-datarobot-${VERSION}-darwin-amd64.tar.gz"

# For macOS (Apple Silicon)
curl -LO "https://github.com/datarobot-community/pulumi-datarobot/releases/download/${VERSION}/pulumi-resource-datarobot-${VERSION}-darwin-arm64.tar.gz"

# For Linux
curl -LO "https://github.com/datarobot-community/pulumi-datarobot/releases/download/${VERSION}/pulumi-resource-datarobot-${VERSION}-linux-amd64.tar.gz"

# Upload to your Artifactory (adjust the path as needed)
curl -u "${ARTIFACTORY_USER}:${ARTIFACTORY_TOKEN}" \
  -T "pulumi-resource-datarobot-${VERSION}-darwin-amd64.tar.gz" \
  "https://artifactory.infra.io/artifactory/pulumi-plugins/datarobot/pulumi-resource-datarobot-${VERSION}-darwin-amd64.tar.gz"
```

#### Step 3: Configure the Environment Variable

```bash
# Set the override to redirect DataRobot plugin downloads to your Artifactory
export PLUGIN_DOWNLOAD_URL_OVERRIDES="^github://api.github.com/datarobot-community/pulumi-datarobot=https://artifactory.infra.io/artifactory/pulumi-plugins/datarobot"
```

#### Step 4: Remove Existing Plugin (for Testing)

```bash
# Remove the existing plugin to force a fresh download
pulumi plugin rm resource datarobot --yes

# Verify it's removed
pulumi plugin ls
```

#### Step 5: Test the Plugin Download

```bash
# Navigate to your Pulumi project
cd examples/py

# Run pulumi preview (this will trigger plugin download)
pulumi preview

# Or explicitly install the plugin
pulumi plugin install resource datarobot ${VERSION}
```

#### Step 6: Verify the Download Source

You can enable verbose logging to verify the plugin is being downloaded from your Artifactory:

```bash
# Enable debug logging
export PULUMI_DEBUG_COMMANDS=true

# Run pulumi and check the output for download URLs
pulumi preview --logtostderr -v=9 2>&1 | grep -i "download\|artifactory"
```

#### Troubleshooting

If the download fails, check:

1. **URL accessibility**: Verify the URL is accessible
   ```bash
   curl -I "https://artifactory.infra.io/artifactory/pulumi-plugins/datarobot/pulumi-resource-datarobot-v0.10.26-darwin-amd64.tar.gz"
   ```

2. **Authentication**: If your Artifactory requires authentication, you may need to configure credentials:
   ```bash
   # For basic auth, include credentials in the URL (not recommended for production)
   export PLUGIN_DOWNLOAD_URL_OVERRIDES="^github://api.github.com/datarobot-community/pulumi-datarobot=https://${ARTIFACTORY_USER}:${ARTIFACTORY_TOKEN}@artifactory.infra.io/artifactory/pulumi-plugins/datarobot"
   ```

3. **File naming**: Ensure the uploaded files match the expected naming convention exactly:
   ```
   pulumi-resource-datarobot-v0.10.26-darwin-amd64.tar.gz
   pulumi-resource-datarobot-v0.10.26-darwin-arm64.tar.gz
   pulumi-resource-datarobot-v0.10.26-linux-amd64.tar.gz
   pulumi-resource-datarobot-v0.10.26-linux-arm64.tar.gz
   pulumi-resource-datarobot-v0.10.26-windows-amd64.tar.gz
   ```

4. **Regex matching**: Test your regex pattern:
   ```bash
   # The plugin URL that needs to match is:
   # github://api.github.com/datarobot-community/pulumi-datarobot

   # Your regex should match this exactly
   echo "github://api.github.com/datarobot-community/pulumi-datarobot" | grep -E "^github://api.github.com/datarobot-community/pulumi-datarobot"
   ```

#### Complete Test Script

```bash
#!/bin/bash
set -e

VERSION="v0.10.26"
ARTIFACTORY_BASE="https://artifactory.infra.io/artifactory/pulumi-plugins/datarobot"

# Configure plugin download override
export PLUGIN_DOWNLOAD_URL_OVERRIDES="^github://api.github.com/datarobot-community/pulumi-datarobot=${ARTIFACTORY_BASE}"

# Skip update checks to avoid GitHub API calls
export PULUMI_SKIP_UPDATE_CHECK=true

# Remove existing plugin
pulumi plugin rm resource datarobot --yes 2>/dev/null || true

# Install plugin (should download from Artifactory)
echo "Installing plugin from: ${ARTIFACTORY_BASE}"
pulumi plugin install resource datarobot ${VERSION}

# Verify installation
pulumi plugin ls | grep datarobot

echo "✅ Plugin successfully installed from Artifactory!"
```

### Combining with Other Air-Gapped Settings

For fully air-gapped deployments, combine `PLUGIN_DOWNLOAD_URL_OVERRIDES` with other settings:

```bash
# Skip update checks to avoid GitHub API calls
export PULUMI_SKIP_UPDATE_CHECK=true

# Redirect plugin downloads to internal repository
export PLUGIN_DOWNLOAD_URL_OVERRIDES="^github://api.github.com/datarobot-community/pulumi-datarobot=https://artifactory.yourcompany.com/pulumi/datarobot"

# Use local state storage
pulumi login --local

# Set DataRobot endpoint
export DATAROBOT_ENDPOINT=https://datarobot.yourcompany.com/api/v2
```
---

## Rate limited by GitHub?

> [!IMPORTANT]
> GitHub has hard limits on API calls that cannot be changed. If you are
running into this when running deployment tasks you have a couple of
options. You can wait until the [rate
limit](https://docs.github.com/en/enterprise-cloud@latest/rest/using-the-rest-api/rate-limits-for-the-rest-api?apiVersion=2022-11-28#primary-rate-limit-for-unauthenticated-users)
expires or you can do a direct download from the releases page which
will not use the API and hit the limit.

To directly download the plugin and bypass the GitHub API run:
```bash
pulumi plugin install resource datarobot <version> --server https://github.com/datarobot-community/pulumi-datarobot/releases/download/<version>/
```
For example, to download version **0.10.14**, you can run:

```bash
pulumi plugin install resource datarobot v0.10.14 --server https://github.com/datarobot-community/pulumi-datarobot/releases/download/v0.10.14/
```
prior to running the deploy to directly install the plugin.

After you have it downloaded, it will still attempt to query for
updates via the GitHub API that can trigger rate limits. To bypass
that, set the environment variable: `PULUMI_SKIP_UPDATE_CHECK`

```bash
export PULUMI_SKIP_UPDATE_CHECK=1
# OR
export PULUMI_SKIP_UPDATE_CHECK=true
```
