# Development documentation

This repo is an automatic [bridge
provider](https://github.com/pulumi/pulumi-terraform-bridge) for the
[DataRobot Terraform
provider](https://github.com/datarobot-community/terraform-provider-datarobot)


## Versioning

Local development builds automatically compute a version based on git tags:

- **On an exact tag** (e.g., `v0.10.28`): Uses the tag as-is (release build)
- **After commits past a tag**: Computes the next patch version (no suffix)

For example, if the latest tag is `v0.10.28`:

| Variable | Value | Usage |
|----------|-------|-------|
| `VERSION` | `v0.10.29` | Provider binary |
| `VERSION_PYTHON` | `0.10.29` | Python SDK |
| `VERSION_NODEJS` | `0.10.29` | Node.js SDK |
| `VERSION_DOTNET` | `0.10.29` | .NET SDK |

This ensures:
- Local dev builds use the next patch version
- No pre-release suffix (avoids semver/PEP440 conversion issues)
- The version is constant during development - you always replace the same version
- **Important**: Only create git tags when doing official releases

You can check the computed versions with:
```bash
make -np 2>/dev/null | grep -E '^VERSION'
```

## Releasing

To release, run the ["Upgrade provider"
Action](https://github.com/datarobot-community/pulumi-datarobot/actions/workflows/upgrade-provider.yml)
after the release of the Terraform provider.

If all goes well, it will generate PR. Review that PR after you've
confirmed it has picked up the correct Terraform provider version
([Sample
PR](https://github.com/datarobot-community/pulumi-datarobot/pull/202)).


After the merge, you are ready to release the new version. To do so,
create a Release matching the same tag as the Terraform Release. In
the sample, that is `v0.10.2`. After you do so, the
[Release](https://github.com/datarobot-community/pulumi-datarobot/actions/workflows/release.yml)
Action will pick it up and run go-releaser for all of our supported
SDKs and attach them back to the release tag you created.


## Validating Locally Prior to Release

We cannot pull back Pulumi releases easily as it requires a manual
e-mail process to do so. So, we recommend you do some smoke testing
locally with the newest release.

### Local testing procedure

* Checkout the main branch locally after the PR created above is merged.
* Ensure you have a valid NodeJS, .NET, JVM, and Python installation available locally in the environment when you are in the repo.
* **Set up Python virtual environment** (recommended to avoid conflicts with system packages):
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate  # On macOS/Linux
  # Or on Windows: .venv\Scripts\activate
  pip install --upgrade pip setuptools wheel
  ```
* Run `make generate_sdk` and resolve any errors that occur. Warnings are okay. It will drop installers into the `sdk` folder by language
* Run `make provider`. This will compile the binary of the provider for your platform that is required in addition to install the platform specific SDK.

Now, in your example Pulumi project, you should be ready to install the local development version. Here is the procedure for that. We'll show Python here because that is our most critical SDK

* First, install the Python package (from the built version with correct VERSION):
  ```bash
  # Using pip
  pip install -e ~/path/to/pulumi-datarobot/sdk/python/bin

  # Or using uv (updates pyproject.toml)
  uv add --editable ~/path/to/pulumi-datarobot/sdk/python/bin
  ```
* Next, clean old plugins, rebuild, and install the provider binary:
  ```bash
  # If the latest git tag is v0.10.28, use v0.10.29 (next patch)
  rm -r ~/.pulumi/plugins/resource-datarobot* && \
    make provider && \
    pulumi plugin install resource datarobot v0.10.29 -f ~/path/to/pulumi-datarobot/bin/pulumi-resource-datarobot
  ```
  
  **Note**: The cleanup step ensures you always have a fresh binary without cached artifacts.

From there, you should have everything ready to test with a `pulumi up`!

## Development with Local Terraform Provider

For developing and testing changes across both the terraform provider and pulumi provider repositories, this repository includes targets that allow you to build using a local copy of the terraform provider.

### Prerequisites

- Clone the [terraform-provider-datarobot](https://github.com/datarobot-community/terraform-provider-datarobot) repository adjacent to this one:
  ```bash
  # Your directory structure should look like:
  # code/
  # ├── pulumi-datarobot/          (this repo)
  # └── terraform-provider-datarobot/
  ```
- Set up a Python virtual environment (recommended):
  ```bash
  cd pulumi-datarobot
  python3 -m venv .venv
  source .venv/bin/activate
  pip install --upgrade pip setuptools wheel
  ```

### Local Development Targets

#### `make build_local_provider`
Builds native binaries for your current platform using the local terraform provider:
- Uses your local terraform provider from `../terraform-provider-datarobot`
- Builds native binaries for your current platform (macOS ARM64, Linux x86_64, etc.)
- Keeps the binaries in `bin/` directory for testing
- Generates schema using the local provider
- Automatically manages go.mod replace directives

Example:
```bash
make build_local_provider
# Results in:
# - bin/pulumi-tfgen-datarobot
# - bin/pulumi-resource-datarobot
```

#### `make test_local_provider`
Complete test build including SDK generation and installation:
- Uses your local terraform provider
- Builds provider binaries
- Generates all SDKs (Node.js, Python, Go, .NET)
- Installs SDKs locally for testing
- Cleans up temporary files when complete

#### `make cross_compile_windows`
Cross-compiles for Windows using your local terraform provider:
- Builds the local terraform provider for Windows
- Cross-compiles Pulumi binaries for Windows (x86-64)
- Generates all SDKs using native binaries (since Windows .exe can't run on macOS)
- Creates both native and Windows binaries in `bin/` directory

Example:
```bash
make cross_compile_windows
# Results in:
# - bin/pulumi-tfgen-datarobot.exe         (Windows)
# - bin/pulumi-resource-datarobot.exe      (Windows)
# - ../terraform-provider-datarobot/terraform-provider-datarobot.exe
```

#### `make clean_windows`
Cleans up Windows cross-compilation artifacts:
```bash
make clean_windows
```

### Local Development Workflow

1. **Make changes** to your terraform provider in `../terraform-provider-datarobot`

2. **Test locally first** (recommended):
   ```bash
   make test_local_provider
   ```

3. **Build local binaries** for development:
   ```bash
   make build_local_provider
   ```

4. **Cross-compile for Windows** testing:
   ```bash
   make cross_compile_windows
   ```

5. **Generate SDKs** (if you ran `build_local_provider` instead of `test_local_provider`):
   ```bash
   make generate_sdk
   ```

6. **Install and test** with a Pulumi project:
   ```bash
   # Install the Python SDK (from the built version with correct VERSION)
   # Using pip:
   pip install -e ~/path/to/pulumi-datarobot/sdk/python/bin
   # Or using uv (updates pyproject.toml):
   uv add --editable ~/path/to/pulumi-datarobot/sdk/python/bin

   # Clean old plugins, rebuild, and install the provider binary
   # If the latest git tag is v0.10.28, use v0.10.29 (next patch)
   rm -r ~/.pulumi/plugins/resource-datarobot* && \
     make build_local_provider && \
     pulumi plugin install resource datarobot v0.10.29 -f ~/path/to/pulumi-datarobot/bin/pulumi-resource-datarobot

   # Test with pulumi up
   cd ~/path/to/your-pulumi-project
   pulumi up
   ```
   
   **Note**: The cleanup step (`rm -r ~/.pulumi/plugins/resource-datarobot*`) ensures you always have a fresh binary without cached artifacts. This is important when iterating during development.

   Alternatively, for a quick test, you can swap out the executable file on your test machine that is in `~/.pulumi/plugins/...`
   with the binaries produced and added to the `bin` folder on an existing install of the plugin.

### Managing Plugin Versions in Pulumi Stacks

When switching between different versions of the DataRobot provider during development, your Pulumi stack state may reference a different plugin version than the one you have installed. This can cause errors like:

```
error: could not load plugin for datarobot provider 'urn:pulumi:stack::project::pulumi:providers:datarobot::default': 
no resource plugin 'pulumi-resource-datarobot' found in the workspace at version v0.10.28
```

To fix this, you need to update the plugin version in your stack state:

1. **Export the stack state**:
   ```bash
   pulumi stack export > export.json
   ```

2. **Edit the plugin version**:
   Open `export.json` and find the `provider` section. Look for entries like:
   ```json
   "urn:pulumi:dev::my-project::pulumi:providers:datarobot::default_0_10_28": {
   ```
   Update the version number to match your installed plugin (e.g., change `0_10_28` to `0_10_29`).
   
   Also update any `pluginDownloadURL` references if present.

3. **Import the updated state**:
   ```bash
   pulumi stack import < export.json
   ```

4. **Verify the change**:
   ```bash
   pulumi preview
   ```

**Tip**: When developing locally, it's often easier to create a new test stack rather than updating plugin versions in existing stacks:
```bash
pulumi stack init dev-local
# ... test your changes ...
pulumi stack rm dev-local  # Clean up when done
```

7. **Clean up** when done:
   ```bash
   make clean_windows  # Remove Windows artifacts
   make clean          # Remove all SDK builds
   ```

### Notes

- All targets automatically manage go.mod replace directives and restore the original state
- Version is auto-computed from git tags (see [Versioning](#versioning) section above)
- Python virtual environment: If you created a `.venv` at the repo root, keep it activated when running `make` commands that build Python SDKs
- **Important**: Always install from `sdk/python/bin`, not `sdk/python`. The source template in `sdk/python/` has `VERSION = "0.0.0"`. The build process copies to `sdk/python/bin/` and injects the correct version there.
- Windows binaries cannot be executed on macOS, so SDK generation uses native binaries even during cross-compilation
- The local terraform provider path can be customized by modifying the `LOCAL_TF_PROVIDER_PATH` variable in the Makefile
- This will change the source code in your tree, do not commit it since it will not work outside of your local environment
