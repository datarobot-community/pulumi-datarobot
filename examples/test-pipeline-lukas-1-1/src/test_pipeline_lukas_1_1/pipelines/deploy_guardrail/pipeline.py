# Copyright 2024 DataRobot, Inc. and its affiliates.
# All rights reserved.
# DataRobot, Inc.
# This is proprietary source code of DataRobot, Inc. and its
# affiliates.
# Released under the terms of DataRobot Tool and Utility Agreement.

import pathlib
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

from .nodes import make_basic_deployment_asset, prepare_yaml_content

import pulumi_datarobot as datarobot
import logging

log = logging.getLogger(__name__)


def custom_model(
    name,
    target_type,
    target_name,
    positive_class_label,
    negative_class_label,
    base_environment_id,
    folder_path,
):
    log.info(folder_path)
    # log.info([str(f.resolve()) for f in pathlib.Path(folder_path).resolve().glob("*")])
    return datarobot.CustomModel(
        resource_name="guardrail_custom_model",
        name=name,
        base_environment_id=base_environment_id,
        base_environment_name="[DataRobot] Python 3.9 GenAI",
        local_files=[f.path for f in folder_path],
        target=target_name,
        target_type=target_type,
    )


def create_pipeline(**kwargs) -> Pipeline:
    nodes = [
        node(
            name="make_guard_parameters",
            func=prepare_yaml_content,
            inputs={
                "blocklist": "params:blocklist",
                "prompt_feature_name": "params:prompt_feature_name",
            },
            outputs="parameters",
        ),
        node(
            name="make_guard_deployment_assets",
            func=make_basic_deployment_asset,
            inputs={
                "custom_py": "custom_py",
                "parameters_yaml": "parameters",
            },
            outputs="deployment_assets",
        ),
        node(func=lambda x: log.info(x), inputs="deployment_assets", outputs=None),
        node(
            name="make_guard_custom_model",
            func=custom_model,
            inputs={
                "name": "params:custom_model_name",
                "target_type": "params:target_type",
                "target_name": "params:target_name",
                "positive_class_label": "params:positive_class_label",
                "negative_class_label": "params:negative_class_label",
                "base_environment_id": "params:base_environment_id",
                "folder_path": "deployment_assets",
            },
            outputs="custom_model",
        ),
        # node(
        #     name="make_guard_custom_model_version",
        #     func=get_or_create_custom_model_version,
        #     inputs={
        #         "endpoint": "params:credentials.datarobot.endpoint",
        #         "token": "params:credentials.datarobot.api_token",
        #         "custom_model_id": "custom_model_id",
        #         "base_environment_id": "params:base_environment_id",
        #         "folder_path": "deployment_assets",
        #     },
        #     outputs="custom_model_version_id",
        # ),
        node(
            name="make_guard_registered_model",
            func=lambda custom_model, registered_model_name: datarobot.RegisteredModel(
                resource_name="guardrail_registered_model",
                name=registered_model_name,
                custom_model_version_id=custom_model.version_id,
            ),
            inputs={
                "custom_model": "custom_model",
                "registered_model_name": "params:registered_model_name",
            },
            outputs="registered_model",
        ),
        node(
            name="make_guard_deployment",
            func=lambda registered_model,
            label,
            default_prediction_server_id: datarobot.Deployment(
                resource_name="guardrail_deployment",
                registered_model_version_id=registered_model.version_id,
                label=label,
                prediction_environment_id=default_prediction_server_id,
            ),
            inputs={
                "registered_model": "registered_model",
                "label": "params:deployment_name",
                "default_prediction_server_id": "params:credentials.datarobot.default_prediction_server_id",
            },
            outputs="guard_deployment",
        ),
    ]
    pipeline_inst = pipeline(nodes)
    return pipeline(
        pipeline_inst,
        namespace="deploy_guardrail",
        parameters={
            # "params:credentials.datarobot.endpoint",
            # "params:credentials.datarobot.api_token",
            "params:credentials.datarobot.default_prediction_server_id",
        },
        outputs="guard_deployment",
    )
