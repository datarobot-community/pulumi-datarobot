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

The `Upstream provider changes` and `Pulumi SDK surface` subsections are generated
during the upstream upgrade by `scripts/upstream-changelog.sh` and
`scripts/schema-diff.sh` — don't hand-edit them, they get regenerated.

Changes made in this repo rather than upstream go under `Unreleased` while unreleased,
and under a `### Provider changes` subsection once they ship in a version.
Regenerating a section preserves that subsection.

## [Unreleased]

### Added

- `CHANGELOG.md` plus `scripts/upstream-changelog.sh`, `scripts/schema-diff.sh`, and
  `scripts/changelog.sh`. Upstream bumps now record what changed upstream and what
  reached the generated SDKs; the same text is posted on the upgrade PR and reused as
  the GitHub Release body.

## [0.10.45] - 2026-07-27

### Provider changes

- Python SDK `config` module no longer fails to import `_utilities` after bridge
  codegen ([#341](https://github.com/datarobot-community/pulumi-datarobot/pull/341)).

### Upstream provider changes

[terraform-provider-datarobot](https://github.com/datarobot-community/terraform-provider-datarobot) `v0.10.43` → `v0.10.45`

#### [v0.10.44](https://github.com/datarobot-community/terraform-provider-datarobot/releases/tag/v0.10.44)

_No entry in the upstream CHANGELOG.md. Commits in this range:_

- [RAPTOR 18559] WAPI client replacement + settings + poll helpers (#337)
- [ RAPTOR 18241] Artifact Image Build Config (#325)
- [RAPTOR 18568] Core behavior: drop RequiresReplace; implement Update() replacement path (#338)
- [RAPTOR 18360] Artifact code source dir FilesAPI client (#334)
- [RAPTOR-18592] - Adapt to updated Workload API (autoscaling, api-key env, probe success_threshold) + fix flaky workload replacement (#340)
- Add notifyOnFailure variable to control Slack notifications in pipelines (#348)
- [RAPTOR 18360] Artifact source push directory (#335)
- [RAPTOR-18562] Fix Deployment missing model version updates via UseStateForUnknown (#346)

#### [v0.10.45](https://github.com/datarobot-community/terraform-provider-datarobot/releases/tag/v0.10.45) — 2026-07-27

##### Added

- updated autoscaling object scheme on workload resources according to the new API version
- new `api-key` source for artifact container `environment_vars`, injecting a platform-managed DataRobot API token (`name` is optional and defaults to `DATAROBOT_API_TOKEN`)
- plan-time validation aligned with the Workload API OpenAPI schema: `cpuAverageUtilization` scaling requires `min_replica_count > 0`, and policy `target` must be non-negative
- `success_threshold` on `datarobot_artifact` container probes (`startup_probe`, `readiness_probe`, `liveness_probe`): minimum consecutive successes for the probe to be considered successful after a failure (matches `ProbeConfig.successThreshold`)

##### Fixed

- `datarobot_deployment`: updating `registered_model_version_id` is no longer silently missed when the referenced value changes in the same apply (e.g. a new `datarobot_registered_model` version created upstream). The attribute's `UseStateForUnknown` plan modifier was substituting the prior state value whenever the config value was still unknown at plan time, suppressing the diff so `Update()` never ran and the deployment kept serving the previous model version. `Update()` already applied the model replacement correctly once triggered; only the missed diff detection needed fixing.
- `datarobot_deployment` updates no longer hangs when the new model version fails to start.
- `datarobot_workload` updates (artifact or runtime changes) no longer intermittently fail with `Error replacing Workload ... not found`. The provider now waits for the replacement by polling the workload record (`workload.replacement`) instead of the `/replacement` endpoint. The Workload API cleans up a `completed` replacement record almost immediately (~1s), so a `GET /replacement` between polls could 404 and was treated as a failure; the workload record makes completion (`replacement` cleared while `running`) and failure (`replacement.status == errored`, which persists) unambiguous and race-free.
- `datarobot_deployment`: the "deployment is not ready" timeout error now includes the deployment id and a console activity-log URL, so a failed activation/deactivation can be traced to the specific deployment and its logs.
- `datarobot_workload`: a container group that sets neither `replica_count` nor `autoscaling` no longer shows perpetual plan drift. The Workload API fills in a cluster-dependent scaling default (a scale-to-zero `autoscaling` block where `KEDA_DEFAULT_SCALE_TO_ZERO_ENABLED` is on, otherwise `replica_count`); that backend-owned `autoscaling` is now kept out of state so it matches the empty config, mirroring how `resource_bundles` and `bundle_selection_policy` are handled.

Full upstream diff: [https://github.com/datarobot-community/terraform-provider-datarobot/compare/v0.10.43...v0.10.45](https://github.com/datarobot-community/terraform-provider-datarobot/compare/v0.10.43...v0.10.45)

### Pulumi SDK surface

_Diff of the generated `schema.json` — what actually reached the SDKs._

> [!WARNING]
> **3 potentially breaking change(s)** — something present before is gone now.
> - `datarobot:index/WorkloadRuntimeContainerGroupAutoscalingPolicy:WorkloadRuntimeContainerGroupAutoscalingPolicy`: removed `maxCount`
> - `datarobot:index/WorkloadRuntimeContainerGroupAutoscalingPolicy:WorkloadRuntimeContainerGroupAutoscalingPolicy`: removed `minCount`
> - `datarobot:index/WorkloadRuntimeContainerGroupAutoscalingPolicy:WorkloadRuntimeContainerGroupAutoscalingPolicy`: removed `priority`

<details><summary>Nested types: 3 added, 0 removed, 12 changed</summary>

Added:

- `datarobot:index/ArtifactSpecContainerGroupContainerImageBuildConfig:ArtifactSpecContainerGroupContainerImageBuildConfig`
- `datarobot:index/ArtifactSpecContainerGroupContainerImageBuildConfigCodeRef:ArtifactSpecContainerGroupContainerImageBuildConfigCodeRef`
- `datarobot:index/ArtifactSpecContainerGroupContainerImageBuildConfigDockerfile:ArtifactSpecContainerGroupContainerImageBuildConfigDockerfile`

Changed:

- `datarobot:index/ArtifactSpecContainerGroupContainer:ArtifactSpecContainerGroupContainer`
  - new: `imageBuildConfig`
- `datarobot:index/ArtifactSpecContainerGroupContainerLivenessProbe:ArtifactSpecContainerGroupContainerLivenessProbe`
  - new: `successThreshold`
- `datarobot:index/ArtifactSpecContainerGroupContainerReadinessProbe:ArtifactSpecContainerGroupContainerReadinessProbe`
  - new: `successThreshold`
- `datarobot:index/ArtifactSpecContainerGroupContainerStartupProbe:ArtifactSpecContainerGroupContainerStartupProbe`
  - new: `successThreshold`
- `datarobot:index/WorkloadRuntimeContainerGroupAutoscaling:WorkloadRuntimeContainerGroupAutoscaling`
  - new: `maxReplicaCount`, `minReplicaCount`
- `datarobot:index/WorkloadRuntimeContainerGroupAutoscalingPolicy:WorkloadRuntimeContainerGroupAutoscalingPolicy`
  - ⚠️ removed: `maxCount`, `minCount`, `priority`
- `datarobot:index/getArtifactSpecContainerGroupContainerLivenessProbe:getArtifactSpecContainerGroupContainerLivenessProbe`
  - new: `successThreshold`
- `datarobot:index/getArtifactSpecContainerGroupContainerReadinessProbe:getArtifactSpecContainerGroupContainerReadinessProbe`
  - new: `successThreshold`
- `datarobot:index/getArtifactSpecContainerGroupContainerStartupProbe:getArtifactSpecContainerGroupContainerStartupProbe`
  - new: `successThreshold`
- `datarobot:index/getArtifactsArtifactSpecContainerGroupContainerLivenessProbe:getArtifactsArtifactSpecContainerGroupContainerLivenessProbe`
  - new: `successThreshold`
- `datarobot:index/getArtifactsArtifactSpecContainerGroupContainerReadinessProbe:getArtifactsArtifactSpecContainerGroupContainerReadinessProbe`
  - new: `successThreshold`
- `datarobot:index/getArtifactsArtifactSpecContainerGroupContainerStartupProbe:getArtifactsArtifactSpecContainerGroupContainerStartupProbe`
  - new: `successThreshold`

</details>

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

