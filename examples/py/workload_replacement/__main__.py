import pulumi
import pulumi_datarobot as dr

# Two independent Artifact/Workload pairs so you can trigger — and observe —
# in-place replacement on each one separately (or both at once).
#
# Artifacts default to status="locked", so any spec change (here:
# containerImage1 / containerImage2) produces a NEW artifact version /
# artifact_id on `pulumi up` — which is what triggers each Workload's
# in-place replacement.

config = pulumi.Config()
workload_name = config.get("workloadName") or "workload-replacement-example"
replica_count = config.get_int("replicaCount") or 2

# Change either of these (pulumi config set containerImage1/2 <image>) and
# re-apply to trigger that pair's in-place workload replacement.
container_image_1 = config.get("containerImage1") or "containous/whoami:latest"
container_image_2 = config.get("containerImage2") or "containous/whoami:latest"


def make_pair(suffix: str, container_image: str) -> tuple[dr.Artifact, dr.Workload]:
    name = f"{workload_name}-{suffix}"

    artifact = dr.Artifact(
        f"app-{suffix}",
        name=f"{name}-artifact",
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

    workload = dr.Workload(
        f"api-{suffix}",
        name=name,
        description=f"Workload replacement workflow example ({suffix})",
        artifact_id=artifact.artifact_id,
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

    return artifact, workload


artifact_1, api_1 = make_pair("1", container_image_1)
artifact_2, api_2 = make_pair("2", container_image_2)

pulumi.export("workload_1_id", api_1.id)
pulumi.export("workload_1_endpoint", api_1.endpoint)
pulumi.export("artifact_1_version_id", artifact_1.artifact_id)

pulumi.export("workload_2_id", api_2.id)
pulumi.export("workload_2_endpoint", api_2.endpoint)
pulumi.export("artifact_2_version_id", artifact_2.artifact_id)
