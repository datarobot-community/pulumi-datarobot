import json
import os
import pathlib
import shutil
import tempfile
from typing import Any
import pulumi
import pulumi_datarobot as datarobot
import yaml  # type: ignore[import-untyped]
from conf.schema.setup_custom_metrics import SetupCustomMetrics
from conf.schema.deploy_guardrail import DeployGuardRailConfig
from conf.schema.prep_dr_rag_custom_model import PrepDrRAGCustomModelConfig
from conf.schema.setup_use_case import SetupUseCase

print("Creating a DataRobot use case...")

import datarobot as dr

dr.Model.get_all_roc_curves()

with open("./conf/local/credentials.yml") as f:
    credentials = yaml.safe_load(f)

stack_name = pulumi.get_stack()

with open("./conf/base/parameters_setup_use_case.yml") as f:
    setup_use_case_config_dict = yaml.safe_load(f)["setup_use_case"]
setup_use_case_config = SetupUseCase.model_validate(setup_use_case_config_dict)

# ================================================================= #
# Deploy Guardrail Model                                            #
# ================================================================= #
if setup_use_case_config.serverless_predictions.use:
    prediction_environment = datarobot.PredictionEnvironment(
        resource_name="prediction-environment",
        name=setup_use_case_config.serverless_predictions.name,
        platform="datarobotServerless",
    )
    prediction_environment_id = prediction_environment.id
else:
    prediction_environment_id = credentials["datarobot"]["default_prediction_server_id"]

openai_credentials = datarobot.ApiTokenCredential(
    resource_name="openai_credentials",
    name=f"{setup_use_case_config.dr_credential.name}_{stack_name}",
    api_token=credentials["azure_openai_llm_credentials"]["api_key"],
)

rag_raw_docs = "include/raw_docs/datarobot_english_documentation_docsassist.zip"


def deploy_guardrail():
    with open("./conf/base/parameters_deploy_guardrail.yml") as f:
        deploy_guardrail_config_dict = yaml.safe_load(f)["deploy_guardrail"]
    deploy_guardrail_config = DeployGuardRailConfig.model_validate(
        deploy_guardrail_config_dict
    )
    guardrail_runtime_parameters = [
        datarobot.CustomModelRuntimeParameterValueArgs(
            key="blocklist",
            type="string",
            value=json.dumps(deploy_guardrail_config.blocklist),
        ),
        datarobot.CustomModelRuntimeParameterValueArgs(
            key="prompt_feature_name",
            type="string",
            value=deploy_guardrail_config.prompt_feature_name,
        ),
    ]

    # move custom.py from ./include/guard to . and reset timestamps for caching
    shutil.copyfile("./include/guard/custom.py", "./custom.py")
    shutil.copyfile("./include/guard/model-metadata.yaml", "./model-metadata.yaml")
    os.utime("./custom.py", (1, 1))
    os.utime("./model-metadata.yaml", (1, 1))

    guardrail_custom_model = datarobot.CustomModel(
        resource_name="guardrail_custom_model",
        name=deploy_guardrail_config.custom_model_name,
        description="Guardrail Custom Model",
        base_environment_id=deploy_guardrail_config.base_environment.id,
        base_environment_name=deploy_guardrail_config.base_environment.name,
        target=deploy_guardrail_config.target_name,
        target_type=deploy_guardrail_config.target_type,
        runtime_parameter_values=guardrail_runtime_parameters,
        local_files=["custom.py", "model-metadata.yaml"],
        negative_class_label=deploy_guardrail_config.negative_class_label,
        positive_class_label=deploy_guardrail_config.positive_class_label,
    )

    guardrail_registered_model = datarobot.RegisteredModel(
        resource_name="guardrail_registered_model",
        name=f"{deploy_guardrail_config.registered_model_name}_{stack_name}",
        custom_model_version_id=guardrail_custom_model.version_id,
    )

    guardrail_deployment = datarobot.Deployment(
        resource_name="guardrail_deployment",
        label=deploy_guardrail_config.deployment_name,
        registered_model_version_id=guardrail_registered_model.version_id,
        prediction_environment_id=prediction_environment_id,
        settings=datarobot.DeploymentSettingsArgs(
            predictions_settings=datarobot.DeploymentSettingsPredictionsSettingsArgs(
                max_computes=1, min_computes=0, real_time=True
            ),
        ),
    )
    return guardrail_deployment, deploy_guardrail_config


# ================================================================= #
# Setup Custom Metrics                                              #
# ================================================================= #


def setup_custom_metrics(guardrail_deployment, deploy_guardrail_config):
    with open("./conf/base/parameters_setup_custom_metrics.yml") as f:
        setup_custom_metrics_dict = yaml.safe_load(f)["setup_custom_metrics"]

    setup_custom_metrics_config = SetupCustomMetrics.model_validate(
        setup_custom_metrics_dict
    )
    guard_config = []
    for guardrail in setup_custom_metrics_config.guardrails.values():
        guardrail_name = guardrail.name
        guardrail_dict = guardrail.model_dump(mode="json")
        guardrail_dict.pop("registered_model_name")
        if guardrail.registered_model_name is not None:
            registered_global_model = datarobot.get_global_model(
                name=guardrail.registered_model_name.value
            )
            deployment = datarobot.Deployment(
                resource_name=f"global_model_deployment_{guardrail_name}",
                label=guardrail_name,
                prediction_environment_id=prediction_environment_id,
                registered_model_version_id=registered_global_model.version_id,
                settings=datarobot.DeploymentSettingsArgs(
                    predictions_settings=datarobot.DeploymentSettingsPredictionsSettingsArgs(
                        max_computes=1, min_computes=0, real_time=True
                    )
                ),
            )
            guardrail_dict["deployment_id"] = deployment.id
        elif guardrail_name == "Keyword Guard":
            deployment = guardrail_deployment
            guardrail_dict["deployment_id"] = deployment.id
            guardrail_dict["model_info"] = {
                "input_column_name": deploy_guardrail_config.prompt_feature_name,
                "output_column_name": f"{deploy_guardrail_config.target_name}_{deploy_guardrail_config.positive_class_label}_PREDICTION",
                "target_type": deploy_guardrail_config.target_type,
                "class_names": [],
            }
        else:
            raise ValueError(f"Unknown guardrail: {guardrail_name}")
        guard_config.append(guardrail_dict)
    return guard_config


# ================================================================= #
# Prep DR RAG Model                                                 #
# ================================================================= #


def prep_dr_rag_custom_model(guard_configs):
    with open("./conf/base/parameters_prep_dr_rag_custom_model.yml") as f:
        prep_dr_rag_custom_model_dict = yaml.safe_load(f)["prep_dr_rag_custom_model"]

    prep_dr_rag_custom_model_config = PrepDrRAGCustomModelConfig.model_validate(
        prep_dr_rag_custom_model_dict
    )

    use_case = datarobot.UseCase(
        resource_name="use_case",
        **prep_dr_rag_custom_model_config.use_case.model_dump(mode="json"),
    )
    playground = datarobot.Playground(
        resource_name="playground",
        use_case_id=use_case.id,
        name=prep_dr_rag_custom_model_config.playground.name,
    )

    vdb_dataset = datarobot.DatasetFromFile(
        resource_name="vdb_dataset",
        use_case_id=use_case.id,
        source_file=rag_raw_docs,
        # name=name,
    )
    vector_database = datarobot.VectorDatabase(
        resource_name="vdb_vector_database",
        dataset_id=vdb_dataset.id,
        use_case_id=use_case.id,
        **prep_dr_rag_custom_model_config.vector_database.model_dump(mode="json"),
    )
    llm_blueprint = datarobot.LlmBlueprint(
        resource_name="llm_blueprint",
        playground_id=playground.id,
        name=prep_dr_rag_custom_model_config.llm_blueprint.name,
        llm_id=prep_dr_rag_custom_model_config.llm_blueprint.llm.id,
        # llm_settings=llm_settings,
        vector_database_id=vector_database.id,
        # vector_database_settings=vector_database_settings,
    )

    runtime_parameters = [
        datarobot.CustomModelRuntimeParameterValueArgs(
            key="OPENAI_API_KEY",
            type="credential",
            value=openai_credentials.id,
        ),
        datarobot.CustomModelRuntimeParameterValueArgs(
            key="OPENAI_API_BASE",
            type="string",
            value=credentials["azure_openai_llm_credentials"]["azure_endpoint"],
        ),
    ]

    rag_custom_model = datarobot.CustomModel(
        resource_name="rag_custom_model",
        name=prep_dr_rag_custom_model_config.custom_model.name,
        description="RAG Custom Model for Azure OpenAI",
        source_llm_blueprint_id=llm_blueprint.id,
        base_environment_id=prep_dr_rag_custom_model_config.custom_model.base_environment.id,
        base_environment_name=prep_dr_rag_custom_model_config.custom_model.base_environment.name,
        runtime_parameter_values=runtime_parameters,
        guard_configurations=guard_configs,
        # prompt_column_name=prompt_column_name,
        target=prep_dr_rag_custom_model_config.custom_model.target_name,
    )
    return rag_custom_model


# ================================================================= #
# Prep User Rag Custom Model                                        #
# ================================================================= #


def prep_user_rag_custom_model():
    with open("conf/base/parameters_prep_user_rag_custom_model.yml") as f:
        prep_user_rag_custom_model_config = yaml.safe_load(f)

    def make_chunks(
        path_to_source_documents: pathlib.Path, chunk_size: int, chunk_overlap: int
    ) -> dict[str, Any]:
        """Convert raw documents into document chunks that can be ingested into a vector db.

        This node will often need to be tailored to your source documents.

        Parameters
        ----------
        path_to_source_documents : pathlib.Path
            Path to a directory containing the source documents
        chunk_size : int
            Document splitting chunk size
        chunk_overlap : int
            Document splitting overlap size

        Returns
        -------
        str :
            Document chunks as a list of langchain.schema.document.Document objects serialized to
            json. Each document should have its metadata['source'] attribute populated to allow
            the front end to report citations back to the user.
        """
        import re

        import nltk
        from langchain.text_splitter import MarkdownTextSplitter
        from langchain_community.document_loaders import DirectoryLoader

        def _format_metadata():
            """
            this function helps formatting the metadata to create a URL
            edit to your needs
            """
            https_string = re.compile(r".+(https://.+)$")

            for doc in docs:
                doc.metadata["source"] = (
                    doc.metadata["source"]
                    .replace("|", "/")
                    .replace(str(path_to_source_documents.resolve()), "")
                )

                doc.metadata["source"] = re.sub(
                    r"datarobot_docs/en/(.+)\.txt",
                    r"https://docs.datarobot.com/en/docs/\1.html",
                    doc.metadata["source"],
                )
                try:
                    doc.metadata["source"] = https_string.findall(
                        doc.metadata["source"]
                    )[0]
                except:
                    pass

        SOURCE_DOCUMENTS_FILTER = "**/*.*"  # "**/*.pdf" or "**/*.txt"

        loader = DirectoryLoader(
            str(path_to_source_documents.resolve()), glob=SOURCE_DOCUMENTS_FILTER
        )
        splitter = MarkdownTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

        nltk.download("punkt", quiet=True)
        nltk.download("punkt_tab", quiet=True)
        nltk.download("averaged_perceptron_tagger_eng", quiet=True)

        data = loader.load()
        docs = splitter.split_documents(data)

        _format_metadata()

        return {"docs": [doc.to_json() for doc in docs]}

    def make_vector_db_assets(
        docs: dict[str, Any], embedding_model_name: str
    ) -> tempfile.TemporaryDirectory:
        """Build the vector db and prepare it to be persisted.

        Parameters
        ----------
        docs : str
            json-serialized list of langchain.schema.document.Document objects corresponding
            to the chunked raw documents (and associated source metadata)
        embedding_model_name : str
            Name of the sentence-transformers embedding model to use with the vectorstore
            that will be built

        Returns
        -------
        tempfile.TemporaryDirectory :
            Temp directory containing all vector db assets that should be included in the
            custom model deployment.
        """
        import os
        import tempfile

        from langchain.schema import Document
        from langchain_community.vectorstores.faiss import FAISS
        from langchain_huggingface import HuggingFaceEmbeddings

        d = tempfile.TemporaryDirectory()
        path_to_d = d.name

        documents = [Document(**doc["kwargs"]) for doc in docs["docs"]]

        embedding_function = HuggingFaceEmbeddings(
            model_name=embedding_model_name,
            cache_folder=os.path.join(path_to_d, "sentencetransformers"),
        )
        texts = [doc.page_content for doc in documents]
        metadatas = [doc.metadata for doc in documents]

        db = FAISS.from_texts(texts, embedding_function, metadatas=metadatas)
        db.save_local(os.path.join(path_to_d, "faiss_db"))
        return d


# ================================================================= #
# Deploy Rag                                                        #
# ================================================================= #


def deploy_rag(rag_custom_model):
    with open("conf/base/parameters_deploy_rag.yml") as f:
        deploy_rag_config = yaml.safe_load(f)["deploy_rag"]

    rag_registered_model = datarobot.RegisteredModel(
        resource_name="rag_registered_model",
        custom_model_version_id=rag_custom_model.version_id,
        name=f'{deploy_rag_config["registered_model_name"]}_{stack_name}',
    )

    rag_deployment = datarobot.Deployment(
        resource_name="rag_deployment",
        registered_model_version_id=rag_registered_model.version_id,
        label=deploy_rag_config["rag_deployment_name"],
        prediction_environment_id=prediction_environment_id,
        settings=datarobot.DeploymentSettingsArgs(
            association_id=datarobot.DeploymentSettingsAssociationIdArgs(
                feature_name="association_id", auto_generate_id=False
            ),
            prediction_row_storage=True,
            predictions_settings=datarobot.DeploymentSettingsPredictionsSettingsArgs(
                max_computes=1, min_computes=0, real_time=True
            ),
        ),
    )
    return rag_deployment


# ================================================================= #
# Deploy DR Streamlit App                                           #
# ================================================================= #


def deploy_dr_streamlit_app(rag_deployment):
    with open("conf/base/parameters_deploy_dr_streamlit_app.yml") as f:
        deploy_dr_streamlit_app_config = yaml.safe_load(f)["deploy_dr_streamlit_app"]

    chat_application = datarobot.ChatApplication(
        resource_name="chat_application",
        deployment_id=rag_deployment.id,
        name=f'{deploy_dr_streamlit_app_config["custom_app_name"]}_{stack_name}',
    )
    return chat_application


guardrail_deployment, deploy_guardrail_config = deploy_guardrail()
guard_configs = setup_custom_metrics(guardrail_deployment, deploy_guardrail_config)
rag_custom_model = prep_dr_rag_custom_model(guard_configs)
rag_deployment = deploy_rag(rag_custom_model)
chat_application = deploy_dr_streamlit_app(rag_deployment)

pulumi.export("chat app", chat_application.id)
