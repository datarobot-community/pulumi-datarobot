import pulumi
import pulumi_datarobot as datarobot

print("Creating a DataRobot use case...")

# Create a DataRobot use case
use_case = datarobot.UseCase(
    "example fom python",
    name="An example fom python",
    description="Description for the example use case",
)

# Export the ID of the example use case
pulumi.export("example_id", use_case.id)
