# Copyright 2024 DataRobot, Inc. and its affiliates.
# All rights reserved.
# DataRobot, Inc.
# This is proprietary source code of DataRobot, Inc. and its
# affiliates.
# Released under the terms of DataRobot Tool and Utility Agreement.

from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline

from .nodes import (
    deploy_global_registered_models,
)


def create_pipeline(**kwargs) -> Pipeline:
    nodes = [
        node(
            name="make_global_model_deployments",
            func=deploy_global_registered_models,
            inputs={
                "endpoint": "params:credentials.datarobot.endpoint",
                "token": "params:credentials.datarobot.api_token",
                "global_models": "params:global_models",
                "default_prediction_server_id": "params:credentials.datarobot.default_prediction_server_id",
            },
            outputs="global_model_deployment_ids",
        ),
        # node(
        #     name="make_prompt_injection_settings",
        #     func=lambda global_model_deployment_ids: {
        #         "deployment_id": str(global_model_deployment_ids["injection"]),
        #     },
        #     inputs={
        #         "global_model_deployment_ids": "global_model_deployment_ids",
        #     },
        #     outputs="prompt_injection_settings",
        # ),
        node(
            name="set_prompt_injection_metric",
            func=lambda prompt_injection_template, global_model_deployment_ids: {
                **prompt_injection_template,
                "deployment_id": global_model_deployment_ids["injection"],
            },
            inputs={
                "prompt_injection_template": "params:guardrails.prompt_injection",
                "global_model_deployment_ids": "global_model_deployment_ids",
            },
            outputs="prompt_injection_guard_config",
        ),
        node(
            name="set_toxicity_metric",
            func=lambda toxicity_template, global_model_deployment_ids: {
                **toxicity_template,
                "deployment_id": global_model_deployment_ids["toxicity"],
            },
            inputs={
                "toxicity_template": "params:guardrails.toxicity",
                "global_model_deployment_ids": "global_model_deployment_ids",
            },
            outputs="toxicity_guard_config",
        ),
        node(
            name="set_keyword_guard_metric",
            func=lambda keyword_guard_template,
            guard_deployment,
            deploy_guardrail_conf: {
                **keyword_guard_template,
                "deployment_id": guard_deployment.id,
                "model_info": {
                    "input_column_name": deploy_guardrail_conf["prompt_feature_name"],
                    "output_column_name": f"{deploy_guardrail_conf['target_name']}_{deploy_guardrail_conf['positive_class_label']}_PREDICTION",
                    "target_type": deploy_guardrail_conf["target_type"],
                    "class_names": [],
                },
            },
            inputs={
                "keyword_guard_template": "params:guardrails.keyword_guard",
                # "guard_config_template_settings": "keyword_guard_settings",
                "guard_deployment": "guard_deployment",
                "deploy_guardrail_conf": "params:deploy_guardrail",
            },
            outputs="keyword_guard_config",
        ),
        node(
            name="collect_guard_configs",
            func=lambda *guard_configs: list(guard_configs),
            inputs=[
                "keyword_guard_config",
                "prompt_injection_guard_config",
                "toxicity_guard_config",
            ],
            outputs="guard_configs",
        ),
    ]
    pipeline_inst = pipeline(nodes)
    return pipeline(
        pipeline_inst,
        namespace="setup_custom_metrics",
        inputs={"guard_deployment": "guard_deployment"},
        parameters={
            "params:credentials.datarobot.endpoint": "params:credentials.datarobot.endpoint",
            "params:credentials.datarobot.api_token": "params:credentials.datarobot.api_token",
            "params:credentials.datarobot.default_prediction_server_id": "params:credentials.datarobot.default_prediction_server_id",
            "params:deploy_guardrail": "params:deploy_guardrail",
        },
        outputs={
            "guard_configs": "guard_configs",
            "global_model_deployment_ids": "global_model_deployment_ids",
        },
    )
