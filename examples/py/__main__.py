import json
import pulumi
import pulumi_datarobot as datarobot
import datarobot as dr

print("Creating a DataRobot use case...")

# Create a DataRobot use case
use_case = datarobot.UseCase(
    "example fom python",
    name="An example fom python",
    description="Description for the example use case",
)

keyword_guard_target_name = "flagged"
keyword_guard_positive_class_label = "true"
keyword_guard_negative_class_label = "false"
# name="[GenAI] Python 3.11 with Moderations", id="65f9b27eab986d30d4c64268"
custom_model = datarobot.CustomModel(
    resource_name="keyword-guard-model",
    name="Keyword Guard Model",
    description="This model is designed to guard against questions about competitors",
    base_environment_id="65f9b27eab986d30d4c64268",
    base_environment_name="[GenAI] Python 3.11 with Moderations",
    target_name=keyword_guard_target_name,
    target_type=dr.enums.TARGET_TYPE.BINARY,
    positive_class_label=keyword_guard_positive_class_label,
    negative_class_label=keyword_guard_negative_class_label,
    runtime_parameter_values=[
        datarobot.CustomModelRuntimeParameterValueArgs(
            key="blocklist",
            type="string",
            value=json.dumps(
                [
                    "dataiku",
                    "databrick",
                    "h20",
                    "aws",
                    "amazon",
                    "azure",
                    "microsoft",
                    "gcp",
                    "google",
                    "vertex\\s*ai",
                    "compet",
                ]
            ),
        ),
        datarobot.CustomModelRuntimeParameterValueArgs(
            key="prompt_feature_name",
            type="string",
            value="guardrailText",
        ),
    ],
    folder_path="grading/",
    # files=[
    #     ("./grading/custom.py", "custom.py"),
    #     ("./grading/model-metadata.yaml", "model-metadata.yaml"),
    # ],
)

registered_model = datarobot.RegisteredModel(
    resource_name="keyword-guard-model",
    name="Keyword Guard Model",
    custom_model_version_id=custom_model.version_id,
)

prediction_environment = datarobot.PredictionEnvironment(
    resource_name="keyword-guard-prediction-environment",
    name="test-env",
    platform="datarobotServerless",
)

deployment = datarobot.Deployment(
    resource_name="keyword-guard-deployment",
    label="Keyword Guard Deployment",
    registered_model_version_id=registered_model.version_id,
    prediction_environment_id=prediction_environment.id,  # "Moderations" environment
)
