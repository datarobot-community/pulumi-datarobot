# Development documentation

This repo is an automatic [bridge
provider](https://github.com/pulumi/pulumi-terraform-bridge) for the
[DataRobot Terraform
provider](https://github.com/datarobot-community/terraform-provider-datarobot)


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
* Run `make generate_sdk` and resolve any errors that occur. Warnings are okay. It will drop installers into the `sdk` folder by language
* Run `make provider`. This will compile the binary of the provider for your platform that is required in addition to install the platform specific SDK.

Now, in your example Pulumi project, you should be ready to install the local development version. Here is the procedure for that. We'll show Python here because that is our most critical SDK

* First, install the Python package `pip install -e ~/path/to/pulumi-datarobot/sdk/python`
* Next, install the provider binary with `pulumi plugin install resource datarobot v0.0.0 -f ~/path/to/pulumi-datarobot/bin/pulumi-resource-datarobot`

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

5. **Install and test** with a Pulumi project:
   ```bash
   # Install the Python SDK
   pip install -e ~/path/to/pulumi-datarobot/sdk/python

   # Install the provider binary
   pulumi plugin install resource datarobot v0.0.0 -f ~/path/to/pulumi-datarobot/bin/pulumi-resource-datarobot

   # Test with pulumi up
   pulumi up
   ```

   Alternatively, for a quick test, you can swap out the executable file on your test machine that is in `~/.pulumi/plugins/...`
   with the binaries produced and added to the `bin` folder on an existing install of the plugin.

6. **Clean up** when done:
   ```bash
   make clean_windows  # Remove Windows artifacts
   make clean          # Remove all SDK builds
   ```

### Notes

- All targets automatically manage go.mod replace directives and restore the original state
- The `+dirty` version suffix appears when you have uncommitted changes - this is normal during development
- Windows binaries cannot be executed on macOS, so SDK generation uses native binaries even during cross-compilation
- The local terraform provider path can be customized by modifying the `LOCAL_TF_PROVIDER_PATH` variable in the Makefile
- This will change the source code in your tree, do not commit it since it will not work outside of your local environment