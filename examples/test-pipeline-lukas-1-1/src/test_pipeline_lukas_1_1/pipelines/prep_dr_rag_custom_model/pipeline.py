# Copyright 2024 DataRobot, Inc. and its affiliates.
# All rights reserved.
# DataRobot, Inc.
# This is proprietary source code of DataRobot, Inc. and its
# affiliates.
# Released under the terms of DataRobot Tool and Utility Agreement.

"""
This is a boilerplate pipeline 'prep_dr_rag_custom_model'
generated using Kedro 0.19.3
"""

from pathlib import Path
from datarobotx.idp.credentials import get_replace_or_create_credential
from datarobotx.idp.llm_blueprints import (
    get_or_create_llm_blueprint,
    get_or_register_llm_blueprint_custom_model_version,
)
from datarobotx.idp.playgrounds import get_or_create_playground
from datarobotx.idp.use_cases import get_or_create_use_case
from datarobotx.idp.vector_databases import get_or_create_vector_database_from_dataset
from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline
import pulumi_datarobot as datarobot

from .nodes import (
    upload_vector_database,
)
import logging

log = logging.getLogger(__name__)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                name="create_use_case",
                func=lambda **kwargs: datarobot.UseCase(
                    resource_name="example", **kwargs
                ),
                inputs={
                    "name": "params:use_case.name",
                    "description": "params:use_case.description",
                },
                outputs="use_case",
            ),
            node(
                name="make_datarobot_RAG_credential",
                func=lambda **kwargs: datarobot.ApiTokenCredential(
                    resource_name="example", **kwargs
                ),
                inputs={
                    "name": "params:dr_credential.name",
                    "api_token": "params:credentials.azure_openai_llm_credentials.api_key",
                },
                outputs="dr_credential",
            ),
            node(
                name="create_playground",
                func=lambda use_case, name: datarobot.Playground(
                    resource_name="example",
                    use_case_id=use_case.id,
                    name=name,
                ),
                inputs={
                    "use_case": "use_case",
                    "name": "params:playground.name",
                },
                outputs="playground",
            ),
            node(
                func=lambda use_case, file_path: datarobot.DatasetFromFile(
                    resource_name="example",
                    use_case_id=use_case.id,
                    source_file=file_path,
                    # name=name,
                ),
                inputs={
                    "use_case": "use_case",
                    "file_path": "params:rag_raw_docs",
                    # "name": "params:vector_database.name",
                },
                outputs="vector_database_dataset",
                name="upload_vector_database",
            ),
            node(
                name="add_vector_database",
                func=lambda dataset,
                use_case,
                chunking_parameters,
                name: datarobot.VectorDatabase(
                    resource_name="example",
                    dataset_id=dataset.id,
                    use_case_id=use_case.id,
                    chunking_parameters=chunking_parameters,
                    name=name,
                ),
                inputs={
                    "dataset": "vector_database_dataset",
                    "use_case": "use_case",
                    "chunking_parameters": "params:vector_database.chunking_parameters",
                    "name": "params:vector_database.name",
                },
                outputs="vector_database",
            ),
            node(
                name="create_pre_baked_blueprint",
                func=lambda playground,
                name,
                llm,
                llm_settings,
                vector_database,
                vector_database_settings: datarobot.LlmBlueprint(
                    resource_name="example",
                    playground_id=playground.id,
                    name=name,
                    llm_id=llm,
                    # llm_settings=llm_settings,
                    vector_database_id=vector_database.id,
                    # vector_database_settings=vector_database_settings,
                ),
                inputs={
                    "playground": "playground",
                    "name": "params:llm_blueprint.name",
                    "llm": "params:llm_blueprint.llm.id",
                    "llm_settings": "params:llm_blueprint.llm_settings",
                    "vector_database": "vector_database",
                    "vector_database_settings": "params:llm_blueprint.vector_database_settings",
                },
                outputs="llm_blueprint",
            ),
            node(
                name="make_custom_model_version_args",
                func=lambda credential, azure_endpoint, base_environment_id: {
                    "runtime_parameter_values": [
                        {
                            "key": "OPENAI_API_KEY",
                            "type": "credential",
                            "value": credential.id,
                        },
                        {
                            "key": "OPENAI_API_BASE",
                            "type": "string",
                            "value": azure_endpoint,
                        },
                    ],
                    "base_environment_id": base_environment_id,
                },
                inputs={
                    "credential": "dr_credential",
                    "azure_endpoint": "params:credentials.azure_openai_llm_credentials.azure_endpoint",
                    "base_environment_id": "params:custom_model.base_environment_id",
                },
                outputs="custom_model_version_args",
            ),
            node(
                name="create_custom_model_from_llm_blueprint",
                func=lambda llm_blueprint,
                custom_model_version_args,
                guard_configs,
                prompt_column_name,
                target_column_name: datarobot.CustomModel(
                    resource_name="example",
                    source_llm_blueprint_id=llm_blueprint.id,
                    base_environment_id=custom_model_version_args[
                        "base_environment_id"
                    ],
                    base_environment_name="[GenAI] Python 3.11 with Moderations",
                    runtime_parameters=custom_model_version_args[
                        "runtime_parameter_values"
                    ],
                    guard_configurations=guard_configs,
                    # prompt_column_name=prompt_column_name,
                    target=target_column_name,
                ),
                inputs={
                    "llm_blueprint": "llm_blueprint",
                    "custom_model_version_args": "custom_model_version_args",
                    "guard_configs": "guard_configs",
                    "prompt_column_name": "params:custom_model.prompt_feature_name",
                    "target_column_name": "params:custom_model.target_name",
                },
                outputs="rag_custom_model",
            ),
        ],
        inputs={"guard_configs": "guard_configs"},
        namespace="prep_dr_rag_custom_model",
        parameters={
            # "params:credentials.datarobot.endpoint": "params:credentials.datarobot.endpoint",
            # "params:credentials.datarobot.api_token": "params:credentials.datarobot.api_token",
            "params:credentials.azure_openai_llm_credentials.api_key": "params:credentials.azure_openai_llm_credentials.api_key",
            "params:credentials.azure_openai_llm_credentials.azure_endpoint": "params:credentials.azure_openai_llm_credentials.azure_endpoint",
        },
        outputs={"rag_custom_model"},
    )
