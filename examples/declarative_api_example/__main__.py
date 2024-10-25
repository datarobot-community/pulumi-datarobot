"""A Python Pulumi program"""

import pulumi
import pulumi_datarobot as datarobot

# Create a DataRobot use case
use_case = datarobot.UseCase("example fom python",
    name="An example fom python",
    description="Description for the example use case"
)

# Create a Custom Model
custom_model = datarobot.CustomModel(
    resource_name="test-custom-model",
    name="pytest custom model 2",
    description="pytest custom model",
    base_environment_id="65f9b27eab986d30d4c64268",
    folder_path="model_dir",
    target_type="Regression",
    target_name="dummy",
)

# Create a Registered Model
registered_model = datarobot.RegisteredModel(
    resource_name="test-registered-model",
    custom_model_version_id=custom_model.version_id,
    name="pytest registered model",
)

# Create a Prediction Environment
prediction_environment = datarobot.PredictionEnvironment(
    resource_name="test-prediction-environment",
    name="pytest prediction environment",
    platform="datarobotServerless",
)

# Create a Deployment
deployment = datarobot.Deployment(
    resource_name="test-deployment",
    registered_model_version_id=registered_model.version_id,
    label="pytest deployment",
    prediction_environment_id=prediction_environment.id,
)

pulumi.export("custom_model_id", custom_model.id)
pulumi.export("custom_model_version_id", custom_model.version_id)