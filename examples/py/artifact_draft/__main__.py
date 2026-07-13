import pulumi
import pulumi_datarobot as datarobot

artifact = datarobot.Artifact(
    "draft-example",
    name="pulumi-draft-artifact",
    description="Draft artifact for C2W iteration",
    status="draft",
    spec=datarobot.ArtifactSpecArgs(
        container_groups=[datarobot.ArtifactSpecContainerGroupArgs(
            containers=[datarobot.ArtifactSpecContainerGroupContainerArgs(
                image_uri="nginx:latest",
                primary=True,
                port=8080,
            )],
        )],
    ),
)

pulumi.export("artifact_id", artifact.artifact_id)
pulumi.export("status", artifact.status)