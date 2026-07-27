# Changelog

All notable changes to the Pulumi DataRobot provider are recorded here. The format is
based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

This provider is bridged from
[terraform-provider-datarobot](https://github.com/datarobot-community/terraform-provider-datarobot),
and its version tracks the upstream provider's version. Each released section therefore
carries two things:

- **Upstream provider changes** — what changed in the Terraform provider, taken from its
  own changelog (or its commit log where an entry is missing).
- **Pulumi SDK surface** — what those changes actually did to the generated
  `schema.json`, and so to the Python, Node.js, Go, and .NET SDKs. The two do not always
  agree; the diff is what ships.

Released sections below the `Unreleased` heading are generated during the upstream
upgrade by `scripts/upstream-changelog.sh` and `scripts/schema-diff.sh`. Add
hand-written entries for provider-repo changes under `Unreleased`.

## [Unreleased]

### Added

- `CHANGELOG.md` plus `scripts/upstream-changelog.sh`, `scripts/schema-diff.sh`, and
  `scripts/changelog.sh`. Upstream bumps now record what changed upstream and what
  reached the generated SDKs; the same text is posted on the upgrade PR and reused as
  the GitHub Release body.

### Fixed

- Python SDK `config` module no longer fails to import `_utilities` after bridge
  codegen (see the `build_python` fixup in the `Makefile`).

## [0.10.43] - 2026-07-16

### Upstream provider changes

[terraform-provider-datarobot](https://github.com/datarobot-community/terraform-provider-datarobot) `v0.10.42` → `v0.10.43`

#### [v0.10.43](https://github.com/datarobot-community/terraform-provider-datarobot/releases/tag/v0.10.43) — 2026-07-15

##### Added

- `status` attribute on `datarobot_artifact`: `draft` (the current artifact version is mutable; spec changes are applied in-place and `artifact_id` stays the same) or `locked` (artifact versions are immutable; spec changes create a new version with a new `artifact_id` in the same `artifact_repository_id`). Defaults to `locked`. Locking a draft artifact is one-way. Changing `status` from `locked` to `draft` creates a new draft artifact (the Workload API cannot unlock in place).
- `datarobot_artifact` data source for looking up an existing Workload API artifact by ID
- `datarobot_artifacts` data source for listing Workload API artifacts with optional `status` and `limit` filters

##### Fixed

- `datarobot_deployment` creation no longer hangs for the full timeout when the creation task reports a definitive `ERROR` status (e.g. custom model failed to start). The provider now fails fast with the task's error message instead of blind-polling deployment status, which never resolves in that case.
- `datarobot_deployment` activation and deactivation (e.g. around runtime parameter updates) now track the async status-change task and fail fast with the task's error message when it reports `ERROR`, instead of blind-polling deployment status until the timeout.
- Deployment model replacement updates now wait for backend `modelPackageId` propagation after the deployment returns to `active`, reducing false positives from short consistency delays. The update now fails only after a bounded wait if the deployment still serves the previous model package, and reports a clear mismatch error instead of writing incorrect planned state.
- Added integration-style mock tests for deployment model replacement success and mismatch scenarios to validate backend `modelPackageId` verification behavior.
- Bumped the Go toolchain target from `1.26.4` to `1.26.5` to pick up the standard-library `crypto/tls` fix for `GO-2026-5856` detected by `govulncheck`.
- when custom model is created with `source_llm_blueprint_id` and user defines `runtime_parameter_values` on the resource, default LLM blueprint runtime parameters are not removed overwritten anymore

Full upstream diff: [https://github.com/datarobot-community/terraform-provider-datarobot/compare/v0.10.42...v0.10.43](https://github.com/datarobot-community/terraform-provider-datarobot/compare/v0.10.42...v0.10.43)

### Pulumi SDK surface

_Diff of the generated `schema.json` — what actually reached the SDKs._

**New functions (2)**

- `datarobot:index/getArtifact:getArtifact`
- `datarobot:index/getArtifacts:getArtifacts`

**Changed resources (1)**

- `datarobot:index/artifact:Artifact`
  - new inputs: `status`
  - new outputs: `status`

<details><summary>Nested types: 37 added, 0 removed, 0 changed</summary>

Added:

- `datarobot:index/getArtifactCreator:getArtifactCreator`
- `datarobot:index/getArtifactSpec:getArtifactSpec`
- `datarobot:index/getArtifactSpecContainerGroup:getArtifactSpecContainerGroup`
- `datarobot:index/getArtifactSpecContainerGroupContainer:getArtifactSpecContainerGroupContainer`
- `datarobot:index/getArtifactSpecContainerGroupContainerBuild:getArtifactSpecContainerGroupContainerBuild`
- `datarobot:index/getArtifactSpecContainerGroupContainerEnvironmentVar:getArtifactSpecContainerGroupContainerEnvironmentVar`
- `datarobot:index/getArtifactSpecContainerGroupContainerImageBuildConfig:getArtifactSpecContainerGroupContainerImageBuildConfig`
- `datarobot:index/getArtifactSpecContainerGroupContainerImageBuildConfigCodeRef:getArtifactSpecContainerGroupContainerImageBuildConfigCodeRef`
- `datarobot:index/getArtifactSpecContainerGroupContainerImageBuildConfigCodeRefDatarobot:getArtifactSpecContainerGroupContainerImageBuildConfigCodeRefDatarobot`
- `datarobot:index/getArtifactSpecContainerGroupContainerImageBuildConfigDockerfile:getArtifactSpecContainerGroupContainerImageBuildConfigDockerfile`
- `datarobot:index/getArtifactSpecContainerGroupContainerLivenessProbe:getArtifactSpecContainerGroupContainerLivenessProbe`
- `datarobot:index/getArtifactSpecContainerGroupContainerReadinessProbe:getArtifactSpecContainerGroupContainerReadinessProbe`
- `datarobot:index/getArtifactSpecContainerGroupContainerSecurityContext:getArtifactSpecContainerGroupContainerSecurityContext`
- `datarobot:index/getArtifactSpecContainerGroupContainerSecurityContextCapabilities:getArtifactSpecContainerGroupContainerSecurityContextCapabilities`
- `datarobot:index/getArtifactSpecContainerGroupContainerSecurityContextSeccompProfile:getArtifactSpecContainerGroupContainerSecurityContextSeccompProfile`
- `datarobot:index/getArtifactSpecContainerGroupContainerStartupProbe:getArtifactSpecContainerGroupContainerStartupProbe`
- `datarobot:index/getArtifactSpecStorage:getArtifactSpecStorage`
- `datarobot:index/getArtifactTag:getArtifactTag`
- `datarobot:index/getArtifactsArtifact:getArtifactsArtifact`
- `datarobot:index/getArtifactsArtifactCreator:getArtifactsArtifactCreator`
- `datarobot:index/getArtifactsArtifactSpec:getArtifactsArtifactSpec`
- `datarobot:index/getArtifactsArtifactSpecContainerGroup:getArtifactsArtifactSpecContainerGroup`
- `datarobot:index/getArtifactsArtifactSpecContainerGroupContainer:getArtifactsArtifactSpecContainerGroupContainer`
- `datarobot:index/getArtifactsArtifactSpecContainerGroupContainerBuild:getArtifactsArtifactSpecContainerGroupContainerBuild`
- `datarobot:index/getArtifactsArtifactSpecContainerGroupContainerEnvironmentVar:getArtifactsArtifactSpecContainerGroupContainerEnvironmentVar`
- `datarobot:index/getArtifactsArtifactSpecContainerGroupContainerImageBuildConfig:getArtifactsArtifactSpecContainerGroupContainerImageBuildConfig`
- `datarobot:index/getArtifactsArtifactSpecContainerGroupContainerImageBuildConfigCodeRef:getArtifactsArtifactSpecContainerGroupContainerImageBuildConfigCodeRef`
- `datarobot:index/getArtifactsArtifactSpecContainerGroupContainerImageBuildConfigCodeRefDatarobot:getArtifactsArtifactSpecContainerGroupContainerImageBuildConfigCodeRefDatarobot`
- `datarobot:index/getArtifactsArtifactSpecContainerGroupContainerImageBuildConfigDockerfile:getArtifactsArtifactSpecContainerGroupContainerImageBuildConfigDockerfile`
- `datarobot:index/getArtifactsArtifactSpecContainerGroupContainerLivenessProbe:getArtifactsArtifactSpecContainerGroupContainerLivenessProbe`
- `datarobot:index/getArtifactsArtifactSpecContainerGroupContainerReadinessProbe:getArtifactsArtifactSpecContainerGroupContainerReadinessProbe`
- `datarobot:index/getArtifactsArtifactSpecContainerGroupContainerSecurityContext:getArtifactsArtifactSpecContainerGroupContainerSecurityContext`
- `datarobot:index/getArtifactsArtifactSpecContainerGroupContainerSecurityContextCapabilities:getArtifactsArtifactSpecContainerGroupContainerSecurityContextCapabilities`
- `datarobot:index/getArtifactsArtifactSpecContainerGroupContainerSecurityContextSeccompProfile:getArtifactsArtifactSpecContainerGroupContainerSecurityContextSeccompProfile`
- `datarobot:index/getArtifactsArtifactSpecContainerGroupContainerStartupProbe:getArtifactsArtifactSpecContainerGroupContainerStartupProbe`
- `datarobot:index/getArtifactsArtifactSpecStorage:getArtifactsArtifactSpecStorage`
- `datarobot:index/getArtifactsArtifactTag:getArtifactsArtifactTag`

</details>

## [0.10.42] - 2026-07-01

### Upstream provider changes

[terraform-provider-datarobot](https://github.com/datarobot-community/terraform-provider-datarobot) `v0.10.41` → `v0.10.42`

#### [v0.10.42](https://github.com/datarobot-community/terraform-provider-datarobot/releases/tag/v0.10.42) — 2026-07-01

##### Added

- `MemorySpace` resource now supports `llm_model_name`, `llm_base_url`, and `custom_instructions` fields

Full upstream diff: [https://github.com/datarobot-community/terraform-provider-datarobot/compare/v0.10.41...v0.10.42](https://github.com/datarobot-community/terraform-provider-datarobot/compare/v0.10.41...v0.10.42)

### Pulumi SDK surface

_Diff of the generated `schema.json` — what actually reached the SDKs._

**Changed resources (1)**

- `datarobot:index/memorySpace:MemorySpace`
  - new inputs: `customInstructions`, `llmBaseUrl`, `llmModelName`
  - new outputs: `customInstructions`, `llmBaseUrl`, `llmModelName`

