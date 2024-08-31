# Copyright 2024 DataRobot, Inc. and its affiliates.
# All rights reserved.
# DataRobot, Inc.
# This is proprietary source code of DataRobot, Inc. and its
# affiliates.
# Released under the terms of DataRobot Tool and Utility Agreement.


from datarobotx.idp.deployments import (
    get_replace_or_create_deployment_from_registered_model,
)
from datarobotx.idp.registered_model_versions import (
    get_or_create_registered_custom_model_version,
)
from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline

from .nodes import (
    ensure_deployment_settings,
)
import pulumi_datarobot as datarobot


def create_pipeline(**kwargs) -> Pipeline:
    nodes = [
        node(
            func=lambda custom_model, registered_model_name: datarobot.RegisteredModel(
                resource_name="rag_registered_model",
                custom_model_version_id=custom_model.version_id,
                name=registered_model_name,
            ),
            inputs={
                "custom_model": "rag_custom_model",
                "registered_model_name": "params:registered_model_name",
            },
            outputs="registered_model",
            name="get_or_create_registered_model",
        ),
        node(
            # "default_prediction_server_id": "params:credentials.datarobot.default_prediction_server_id",
            #     "registered_model_version_id": "registered_custom_model_version_id",
            #     "registered_model_name": "params:registered_model_name",
            #     "label"
            func=lambda default_prediction_server_id,
            registered_model,
            label: datarobot.Deployment(
                resource_name="rag_deployment",
                prediction_environment_id=default_prediction_server_id,
                registered_model_version_id=registered_model.version_id,
                label=label,
                settings=datarobot.DeploymentSettingsArgs(
                    association_id=datarobot.DeploymentSettingsAssociationIdArgs(
                        feature_name="association_id", auto_generate_id=False
                    ),
                    prediction_row_storage=True,
                ),
            ),
            inputs={
                "default_prediction_server_id": "params:credentials.datarobot.default_prediction_server_id",
                "registered_model": "registered_model",
                "label": "params:rag_deployment_name",
            },
            outputs="rag_deployment",
            name="create_deployment",
        ),
        # node(
        #     name="ensure_deployment_settings",
        #     func=ensure_deployment_settings,
        #     inputs={
        #         "endpoint": "params:credentials.datarobot.endpoint",
        #         "token": "params:credentials.datarobot.api_token",
        #         "rag_deployment": "rag_deployment",
        #         "grading_deployment": "grading_deployment",
        #         "guard_deployment": "guard_deployment",
        #     },
        #     outputs=None,
        # ),
    ]
    pipeline_inst = pipeline(nodes)
    return pipeline(
        pipeline_inst,
        namespace="deploy_rag",
        parameters={
            # "params:credentials.datarobot.endpoint": "params:credentials.datarobot.endpoint",
            # "params:credentials.datarobot.api_token": "params:credentials.datarobot.api_token",
            "params:credentials.datarobot.default_prediction_server_id": "params:credentials.datarobot.default_prediction_server_id",
        },
        inputs={
            "rag_custom_model",
            # "grading_deployment",
            # "guard_deployment",
        },
        outputs={"rag_deployment"},
    )
