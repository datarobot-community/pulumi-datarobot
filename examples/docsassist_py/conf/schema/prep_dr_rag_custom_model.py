import textwrap
from typing import Optional
from pydantic import BaseModel, Field, field_validator
from .common.globals import (
    GlobalRuntimeEnvironment,
    LLM,
    GlobalLLMs,
    EnvironmentConfig,
)
from datarobot.enums import VectorDatabaseChunkingMethod, VectorDatabaseEmbeddingModel


class Playground(BaseModel):
    name: str


class CustomModel(BaseModel):
    name: str
    target_name: str
    prompt_feature_name: str
    base_environment: EnvironmentConfig = Field(
        default_factory=lambda: EnvironmentConfig(
            environment=GlobalRuntimeEnvironment.PYTHON_311_MODERATIONS
        )
    )


class LLMSettings(BaseModel):
    max_completion_length: int = Field(int, le=512)
    system_prompt: str = textwrap.dedent("""\
        Use the following pieces of context to answer the user's question.
        If you don't know the answer, just say that you don't know, don't try to make up an answer.
        ----------------
        {context}
        """)


class VectorDatabaseSettings(BaseModel):
    max_documents_retrieved_per_prompt: Optional[int] = 10
    max_tokens: Optional[int] = None


class LLMBlueprint(BaseModel):
    name: str = "gpt-3.5-turbo"
    llm_settings: LLMSettings
    llm: LLM = Field(default=GlobalLLMs.AZURE_OPENAI_GPT_3_5_TURBO)
    vector_database_settings: VectorDatabaseSettings

    @field_validator("llm")
    def validate_llm(cls, v):
        for env in GlobalLLMs:
            if env.value.id == v.id:
                return env.value
        raise ValueError(f"Invalid LLM ID: {v.id}")


# from datarobot.models.genai.vector_database


class ChunkingParameters(BaseModel):
    embedding_model: VectorDatabaseEmbeddingModel = (
        VectorDatabaseEmbeddingModel.JINA_EMBEDDING_T_EN_V1
    )
    chunking_method: VectorDatabaseChunkingMethod = (
        VectorDatabaseChunkingMethod.RECURSIVE
    )
    chunk_size: int = 256
    chunk_overlap_percentage: int = 10
    separators: list[str] = []


class VectorDatabase(BaseModel):
    name: str
    chunking_parameters: ChunkingParameters


class UseCase(BaseModel):
    name: str
    description: str


class PrepDrRAGCustomModelConfig(BaseModel):
    playground: Playground
    custom_model: CustomModel
    llm_blueprint: LLMBlueprint
    vector_database: VectorDatabase
    use_case: UseCase
