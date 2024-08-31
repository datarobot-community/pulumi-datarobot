# Copyright 2024 DataRobot, Inc. and its affiliates.
# All rights reserved.
# DataRobot, Inc.
# This is proprietary source code of DataRobot, Inc. and its
# affiliates.
# Released under the terms of DataRobot Tool and Utility Agreement.

from datarobotx.idp.custom_applications import get_or_create_qanda_app
from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline

from .nodes import log_outputs

import pulumi_datarobot as datarobot


def create_pipeline(**kwargs) -> Pipeline:
    nodes = [
        node(
            name="deploy_app",
            func=lambda deployment, name: datarobot.ChatApplication(
                resource_name="qanda_application",
                deployment_id=deployment.id,
                name=name,
            ),
            inputs={
                "deployment": "rag_deployment",
                # "environment_id": "params:base_environment_id",
                "name": "params:custom_app_name",
            },
            outputs="application",
        ),
        # node(
        #     name="log_outputs",
        #     func=log_outputs,
        #     inputs={
        #         "endpoint": "params:credentials.datarobot.endpoint",
        #         "rag_deployment_id": "rag_deployment_id",
        #         "grading_deployment_id": "grading_deployment_id",
        #         "guard_deployment_id": "guard_deployment_id",
        #         "application_id": "application_id",
        #         "rag_deployment_name": "params:rag_deployment_name",
        #         "grading_deployment_name": "params:grading_deployment_name",
        #         "guard_deployment_name": "params:guard_deployment_name",
        #         "app_name": "params:custom_app_name",
        #     },
        #     outputs=None,
        # ),
    ]
    pipeline_inst = pipeline(nodes)
    return pipeline(
        pipeline_inst,
        namespace="deploy_dr_streamlit_app",
        parameters={
            # "params:credentials.datarobot.endpoint": "params:credentials.datarobot.endpoint",
            # "params:credentials.datarobot.api_token": "params:credentials.datarobot.api_token",
            # "grading_deployment_name": "params:deploy_grader.deployment_name",
            # "rag_deployment_name": "params:deploy_rag.rag_deployment_name",
            # "guard_deployment_name": "params:deploy_guardrail.deployment_name",
        },
        inputs={
            "rag_deployment",
            # "grading_deployment_id",
            # "guard_deployment_id",
        },
        outputs={"application"},
    )
