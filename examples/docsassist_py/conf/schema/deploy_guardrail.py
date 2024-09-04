from pydantic import BaseModel
from .common.globals import GlobalRuntimeEnvironment, RuntimeEnvironment
from datarobot.enums import TARGET_TYPE


class DeployGuardRailConfig(BaseModel):
    deployment_name: str = "Keyword Guard Deployment"
    registered_model_name: str = "Keyword Guard Model"
    custom_model_name: str = "Keyword Guard Model"
    prompt_feature_name: str = "guardrailText"
    target_name: str = "flagged"
    target_type: str = TARGET_TYPE.BINARY
    positive_class_label: str = "true"
    negative_class_label: str = "false"
    base_environment: RuntimeEnvironment = GlobalRuntimeEnvironment.PYTHON_39_GENAI
    blocklist: list[str] = [
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
