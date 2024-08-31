# Copyright 2024 DataRobot, Inc. and its affiliates.
# All rights reserved.
# DataRobot, Inc.
# This is proprietary source code of DataRobot, Inc. and its
# affiliates.
# Released under the terms of DataRobot Tool and Utility Agreement.

from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline

from .nodes import delete_assets


def create_pipeline(**kwargs) -> Pipeline:
    nodes = [
        node(
            name="delete_assets",
            func=delete_assets,
            inputs={
                "endpoint": "params:credentials.datarobot.endpoint",
                "token": "params:credentials.datarobot.api_token",
                "global_model_deployment_ids": "global_model_deployment_ids",
                "grading_deployment_id": "grading_deployment_id",
                "guard_deployment_id": "guard_deployment_id",
                "rag_custom_model_id": "rag_custom_model_id",
                "rag_custom_model_version_id": "rag_custom_model_version_id",
                "rag_deployment_id": "rag_deployment_id",
                "application_id": "application_id",
            },
            outputs=None,
        ),
    ]
    return pipeline(
        pipeline(nodes),
        namespace="delete_assets",
        inputs={
            "rag_deployment_id",
            "application_id",
            "global_model_deployment_ids",
            "grading_deployment_id",
            "guard_deployment_id",
            "rag_custom_model_id",
            "rag_custom_model_version_id",
        },
        parameters={
            "params:credentials.datarobot.endpoint",
            "params:credentials.datarobot.api_token",
        },
    )
