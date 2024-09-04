from enum import Enum
from typing import Optional
from pydantic import BaseModel


class RegisteredGlobalModelName(Enum):
    toxicity = "[Hugging Face] Toxicity Classifier"
    sentiment = "[Hugging Face] Sentiment Classifier"
    refusal = "[DataRobot] LLM Refusal Score"
    prompt_injection = "[Guard] Prompt Injection Classifier from Hugging Face"


class GuardrailTemplateName(Enum):
    CUSTOM_DEPLOYMENT = "Custom Deployment"
    FAITHFULNESS = "Faithfulness"
    PII_DETECTION = "PII Detection"
    PROMPT_INJECTION = "Prompt Injection"
    ROUGE_1 = "Rouge 1"
    SENTIMENT_CLASSIFIER = "Sentiment Classifier"
    STAY_ON_TOPIC_FOR_INPUTS = "Stay on topic for inputs"
    STAY_ON_TOPIC_FOR_OUTPUTS = "Stay on topic for output"
    TOKEN_COUNT = "Token Count"
    TOXICITY = "Toxicity"


class Stage(str, Enum):
    PROMPT = "prompt"
    RESPONSE = "response"


class ModerationAction(str, Enum):
    BLOCK = "block"
    REPORT = "report"
    REPORT_AND_BLOCK = "reportAndBlock"


class GuardConditionComparator(Enum):
    """The comparator used in a guard condition."""

    GREATER_THAN = "greaterThan"
    LESS_THAN = "lessThan"
    EQUALS = "equals"
    NOT_EQUALS = "notEquals"
    IS = "is"
    IS_NOT = "isNot"
    MATCHES = "matches"
    DOES_NOT_MATCH = "doesNotMatch"
    CONTAINS = "contains"
    DOES_NOT_CONTAIN = "doesNotContain"


class Condition(BaseModel):
    comparand: float | str | bool | list[str]
    comparator: GuardConditionComparator


class Intervention(BaseModel):
    action: ModerationAction
    condition: Condition
    message: str
    send_notification: bool


class GuardrailTemplate(BaseModel):
    template_name: GuardrailTemplateName
    registered_model_name: Optional[RegisteredGlobalModelName] = None
    name: str
    stages: list[Stage]
    intervention: Intervention


class SetupCustomMetrics(BaseModel):
    guardrails: dict[str, GuardrailTemplate]
