import pulumi
import pulumi_datarobot as dr

# Mirrors terraform-provider-datarobot's
# examples/workflows/workload_replacement/main.tf: ONE Artifact resource whose
# spec is driven by config. Artifacts default to status="locked", so any spec
# change (here: `container_image`) produces a NEW artifact version/artifact_id
# on `pulumi up` — which is what triggers the Workload's in-place replacement.

config = pulumi.Config()
workload_name = config.get("workloadName") or "workload-replacement-example"
# Change this (pulumi config set containerImage <image>) and re-apply to
# trigger an in-place workload replacement.
container_image = config.get("containerImage") or "containous/whoami:latest"
replica_count = config.get_int("replicaCount") or 2

app = dr.Artifact(
    "app",
    name=f"{workload_name}-artifact",
    type="service",
    spec=dr.ArtifactSpecArgs(
        container_groups=[
            dr.ArtifactSpecContainerGroupArgs(
                containers=[
                    dr.ArtifactSpecContainerGroupContainerArgs(
                        name="main",
                        image_uri=container_image,
                        port=8080,
                        primary=True,
                        entrypoints=["/whoami", "--port", "8080"],
                    ),
                ],
            ),
        ],
    ),
)

api = dr.Workload(
    "api",
    name=workload_name,
    description="Workload replacement workflow example",
    artifact_id=app.artifact_id,
    # replacement_policy (warmup_minutes / keep_old_version_minutes) is
    # omitted: the locally installed pulumi_datarobot build predates that
    # field (see README "Known local SDK gap"). Platform defaults apply.
    runtime=dr.WorkloadRuntimeArgs(
        container_groups=[
            dr.WorkloadRuntimeContainerGroupArgs(
                replica_count=replica_count,
                resource_bundles=["cpu.small"],
            ),
        ],
    ),
)

pulumi.export("workload_id", api.id)
pulumi.export("workload_endpoint", api.endpoint)
pulumi.export("artifact_version_id", app.artifact_id)
