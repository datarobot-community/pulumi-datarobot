# Pulumi DataRobot Provider

This is a Pulumi provider for [DataRobot](https://www.datarobot.com/), automatically bridged from the [terraform-provider-datarobot](https://github.com/datarobot-community/terraform-provider-datarobot) using [pulumi-terraform-bridge](https://github.com/pulumi/pulumi-terraform-bridge).

## Project Structure

```
pulumi-datarobot/
├── provider/           # Go code for the Pulumi provider bridge
│   ├── cmd/            # CLI entry points (pulumi-tfgen-datarobot, pulumi-resource-datarobot)
│   ├── pkg/            # Version info
│   └── resources.go    # Provider bridge configuration
├── sdk/                # Generated SDKs for different languages
│   ├── dotnet/         # .NET SDK
│   ├── go/             # Go SDK
│   ├── nodejs/         # Node.js/TypeScript SDK
│   └── python/         # Python SDK
├── examples/           # Example Pulumi programs
│   ├── py/             # Python examples
│   ├── ts/             # TypeScript examples
│   └── low_code_rag/   # RAG example
├── templates/          # README templates for SDKs
├── scripts/            # Build scripts
└── docs/               # Documentation
```

## Pre-commit Hooks Setup

This project uses pre-commit hooks to ensure code quality. To set up:

```bash
# Install pre-commit (if not already installed)
pip install pre-commit

# Install the git hooks
pre-commit install

# Run hooks manually on all files (optional)
pre-commit run --all-files
```

The hooks will automatically run golangci-lint and other checks before each commit.

## Key Commands

### Build & Development

```bash
make development          # Full dev build: plugins, provider, SDKs, install
make provider             # Build only the provider binary
make generate_sdk         # Generate all SDKs (nodejs, python, go, dotnet)
make build_nodejs         # Build only Node.js SDK
make build_python         # Build only Python SDK
make build_go             # Build only Go SDK
make build_dotnet         # Build only .NET SDK
```

### Local Testing

```bash
make build_local_provider   # Build using local terraform-provider-datarobot
make test_local_provider    # Full test with local terraform provider
make cross_compile_windows  # Cross-compile for Windows
```

### Cleanup

```bash
make clean                # Remove generated SDK directories
make clean_windows        # Remove Windows cross-compilation artifacts
```

### Testing

```bash
make test                 # Run integration tests in examples/
```

## Development Workflow

1. **For provider changes**: Edit `provider/resources.go` to configure bridge mappings
2. **To upgrade upstream provider**: Run the "Upgrade provider" GitHub Action
3. **To test locally**: 
   - Clone terraform-provider-datarobot adjacent to this repo
   - Run `make test_local_provider`

## SDK Installation (Local Dev)

```bash
# Python
pip install -e sdk/python

# Node.js
yarn link --cwd sdk/nodejs/bin

# Install provider binary
pulumi plugin install resource datarobot v0.0.0 -f bin/pulumi-resource-datarobot
```

## Configuration

Environment variables:
- `DATAROBOT_API_TOKEN` - API key for DataRobot
- `DATAROBOT_ENDPOINT` - DataRobot API endpoint

Pulumi config:
- `datarobot:apikey`
- `datarobot:endpoint`

## CI/CD

- **build.yml**: Runs on PRs, builds provider and SDKs
- **release.yml**: Triggered on tags, publishes to package registries
- **upgrade-provider.yml**: Automatically upgrades terraform provider version

## Important Notes

- SDKs are auto-generated from terraform provider schema - do not edit directly
- Version is derived from git tags (e.g., `v0.10.28`)
- Provider uses `terraform-plugin-framework` (plugin framework, not SDK v2)
- The bridge uses `pfbridge.ShimProvider` for plugin-framework compatibility
