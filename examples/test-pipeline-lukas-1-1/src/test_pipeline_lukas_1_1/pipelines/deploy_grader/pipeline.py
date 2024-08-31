# Copyright 2024 DataRobot, Inc. and its affiliates.
# All rights reserved.
# DataRobot, Inc.
# This is proprietary source code of DataRobot, Inc. and its
# affiliates.
# Released under the terms of DataRobot Tool and Utility Agreement.

from datarobotx.idp.custom_model_versions import get_or_create_custom_model_version
from datarobotx.idp.custom_models import get_or_create_custom_model
from datarobotx.idp.deployments import (
    get_replace_or_create_deployment_from_registered_model,
)
from datarobotx.idp.registered_model_versions import (
    get_or_create_registered_custom_model_version,
)
from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline

from .nodes import make_basic_deployment_asset


def create_pipeline(**kwargs) -> Pipeline:
    nodes = [
        node(
            name="make_grading_deployment_assets",
            func=make_basic_deployment_asset,
            inputs="custom_py",
            outputs="deployment_assets",
        ),
        node(
            name="make_grading_custom_model",
            func=get_or_create_custom_model,
            inputs={
                "endpoint": "params:credentials.datarobot.endpoint",
                "token": "params:credentials.datarobot.api_token",
                "name": "params:custom_model_name",
                "target_type": "params:target_type",
                "target_name": "params:target_name",
                "class_labels": "params:class_labels",
            },
            outputs="custom_model_id",
        ),
        node(
            name="make_grading_custom_model_version",
            func=get_or_create_custom_model_version,
            inputs={
                "endpoint": "params:credentials.datarobot.endpoint",
                "token": "params:credentials.datarobot.api_token",
                "custom_model_id": "custom_model_id",
                "base_environment_id": "params:base_environment_id",
                "folder_path": "deployment_assets",
            },
            outputs="custom_model_version_id",
        ),
        node(
            name="make_grading_registered_model",
            func=get_or_create_registered_custom_model_version,
            inputs={
                "endpoint": "params:credentials.datarobot.endpoint",
                "token": "params:credentials.datarobot.api_token",
                "custom_model_version_id": "custom_model_version_id",
                "registered_model_name": "params:registered_model_name",
            },
            outputs="custom_model_registered_version_id",
        ),
        node(
            name="make_grading_deployment",
            func=get_replace_or_create_deployment_from_registered_model,
            inputs={
                "endpoint": "params:credentials.datarobot.endpoint",
                "token": "params:credentials.datarobot.api_token",
                "registered_model_version_id": "custom_model_registered_version_id",
                "registered_model_name": "params:registered_model_name",
                "label": "params:deployment_name",
                "default_prediction_server_id": "params:credentials.datarobot.default_prediction_server_id",
            },
            outputs="grading_deployment_id",
        ),
    ]
    pipeline_inst = pipeline(nodes)
    return pipeline(
        pipeline_inst,
        namespace="deploy_grader",
        parameters={
            "params:credentials.datarobot.endpoint",
            "params:credentials.datarobot.api_token",
            "params:credentials.datarobot.default_prediction_server_id",
        },
        outputs="grading_deployment_id",
    )
