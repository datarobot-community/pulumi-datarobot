from pydantic import BaseModel


class Credential(BaseModel):
    name: str = "docsassist_llm_credential"
    credential_type: str = "api_key"


class ServerlessPredictions(BaseModel):
    use: bool = True
    name: str = "DocsAssist Serverless Prediction Environment"


class SetupUseCase(BaseModel):
    dr_credential: Credential
    serverless_predictions: ServerlessPredictions
