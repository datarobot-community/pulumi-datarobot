from enum import Enum
from typing import List, Optional, Union
from pydantic import BaseModel, Field, field_validator, validator


class RuntimeEnvironment(BaseModel):
    name: str
    id: str


class GlobalRuntimeEnvironment(Enum):
    PYTHON_311_NOTEBOOK_BASE = RuntimeEnvironment(
        name="[DataRobot] Python 3.11 Notebook Base Image",
        id="664388ff6d426582042bb3e4",
    )
    PYTHON_311_MODERATIONS = RuntimeEnvironment(
        name="[GenAI] Python 3.11 with Moderations", id="65f9b27eab986d30d4c64268"
    )
    PYTHON_39_CUSTOM_METRICS = RuntimeEnvironment(
        name="[DataRobot] Python 3.9 Custom Metrics Templates Drop-In",
        id="659bf1626529ceb502d12ae2",
    )
    PYTHON_311_NOTEBOOK_DROP_IN = RuntimeEnvironment(
        name="[DataRobot] Python 3.11 Notebook Drop-In", id="6583d56f5627082b3cff990e"
    )
    PYTHON_39_STREAMLIT = RuntimeEnvironment(
        name="[Experimental] Python 3.9 Streamlit", id="6542cd582a9d3d51bf4ac71e"
    )
    PYTHON_311_GENAI = RuntimeEnvironment(
        name="[DataRobot] Python 3.11 GenAI", id="64d2ba178dd3f0b1fa2162f0"
    )
    PYTHON_39_GENAI = RuntimeEnvironment(
        name="[DataRobot] Python 3.9 GenAI", id="64c964448dd3f0c07f47d040"
    )
    PYTHON_39_ONNX = RuntimeEnvironment(
        name="[DataRobot] Python 3.9 ONNX Drop-In", id="62059a573f7d5f5cebabcba5"
    )
    JULIA_DROP_IN = RuntimeEnvironment(
        name="[DataRobot] Julia Drop-In", id="606234e1879feab31ec1abdd"
    )
    PYTHON_39_PMML = RuntimeEnvironment(
        name="[DataRobot] Python 3.9 PMML Drop-In", id="5ee7dfc6433a8423386102ce"
    )
    R_421_DROP_IN = RuntimeEnvironment(
        name="[DataRobot] R 4.2.1 Drop-In", id="5ea850ca1d41c8173c2feef6"
    )
    PYTHON_39_PYTORCH = RuntimeEnvironment(
        name="[DataRobot] Python 3.9 PyTorch Drop-In", id="5e8c888007389fe0f466c72b"
    )
    JAVA_11_DROP_IN = RuntimeEnvironment(
        name="[DataRobot] Java 11 Drop-In (DR Codegen, H2O)",
        id="5e3028d9c38741266ef86452",
    )
    PYTHON_39_SCIKIT_LEARN = RuntimeEnvironment(
        name="[DataRobot] Python 3.9 Scikit-Learn Drop-In",
        id="5e8c889607389fe0f466c72d",
    )
    PYTHON_39_XGBOOST = RuntimeEnvironment(
        name="[DataRobot] Python 3.9 XGBoost Drop-In", id="5e8c88a407389fe0f466c72f"
    )
    PYTHON_39_KERAS = RuntimeEnvironment(
        name="[DataRobot] Python 3.9 Keras Drop-In", id="5e8c886607389fe0f466c729"
    )


class EnvironmentConfig(BaseModel):
    environment: Union[GlobalRuntimeEnvironment, RuntimeEnvironment]

    @property
    def name(self):
        if isinstance(self.environment, GlobalRuntimeEnvironment):
            return self.environment.value.name
        else:
            return self.environment.name

    @property
    def id(self):
        if isinstance(self.environment, GlobalRuntimeEnvironment):
            return self.environment.value.id
        else:
            return self.environment.id


class GlobalRuntimeEnvironments(BaseModel):
    environments: List[EnvironmentConfig]

    @field_validator("environments")
    def validate_unique_environments(cls, v):
        env_ids = [env.id for env in v]
        if len(set(env_ids)) != len(env_ids):
            raise ValueError("Duplicate environments are not allowed")
        return v


class LLM(BaseModel):
    name: Optional[str] = None
    id: str


class GlobalLLMs(Enum):
    AZURE_OPENAI_GPT_3_5_TURBO = LLM(
        name="Azure OpenAI GPT-3.5 Turbo", id="azure-openai-gpt-3.5-turbo"
    )
    AZURE_OPENAI_GPT_3_5_TURBO_16K = LLM(
        name="Azure OpenAI GPT-3.5 Turbo 16k", id="azure-openai-gpt-3.5-turbo-16k"
    )
    AZURE_OPENAI_GPT_4 = LLM(name="Azure OpenAI GPT-4", id="azure-openai-gpt-4")
    AZURE_OPENAI_GPT_4_32K = LLM(
        name="Azure OpenAI GPT-4 32k", id="azure-openai-gpt-4-32k"
    )
    AZURE_OPENAI_GPT_4_TURBO = LLM(
        name="Azure OpenAI GPT-4 Turbo", id="azure-openai-gpt-4-turbo"
    )
    AMAZON_TITAN = LLM(name="Amazon Titan", id="amazon-titan")
    ANTHROPIC_CLAUDE_2_1 = LLM(name="Anthropic Claude 2.1", id="anthropic-claude-2")
    ANTROHIC_CLAUDE_3_HAIKU = LLM(
        name="Anthropic Claude 3 Haiku", id="anthropic-claude-3-haiku"
    )
    ANTROHIC_CLAUDE_3_SONNET = LLM(
        name="Anthropic Claude 3 Sonnet", id="anthropic-claude-3-sonnet"
    )
    GOOGLE_BISON = LLM(name="Google Bison", id="google-bison")
    GOOGLE_GEMINI_1_5_FLASH = LLM(
        name="Google Gemini 1.5 Flash", id="google-gemini-1.5-flash"
    )
    GOOGLE_1_5_PRO = LLM(name="Google Gemini 1.5 Pro", id="google-gemini-1.5-pro")
    DEPLOYED_LLM = LLM(name="Deployed LLM", id="custom-model")
