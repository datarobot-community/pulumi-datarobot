# Copyright 2024 DataRobot, Inc. and its affiliates.
# All rights reserved.
# DataRobot, Inc.
# This is proprietary source code of DataRobot, Inc. and its
# affiliates.
# Released under the terms of DataRobot Tool and Utility Agreement.

from __future__ import annotations

from typing import Any
from pulumi import Output
import pulumi_datarobot as datarobot


def deploy_global_registered_models(
    endpoint: str,
    token: str,
    global_models: dict[str, Any],
    default_prediction_server_id: str,
) -> dict[str, Output[str]]:
    """Deploy all needed global registered models.

    Parameters
    ----------
    global_models : dict
        Dictionary whose values are dictionaries containing two keys: "registered_model_name"
        and "deployment_name". These keys specify the registered global models that should
        be deployed and the names of the resulting deployments.
    default_prediction_server_id : str
        The DataRobot prediction server id to use for deploying the global models.

    Returns
    -------
    dict
        Dictionary whose values are the deployment ids of the newly deployed global models.
    """

    deployment_ids = {}
    for global_model in global_models:
        registered_model_name = global_models[global_model]["registered_model_name"]
        deployment_name = global_models[global_model]["deployment_name"]

        registered_global_model = datarobot.get_global_model(name=registered_model_name)
        deployment = datarobot.Deployment(
            resource_name=f"deployment_{deployment_name}",
            label=deployment_name,
            prediction_environment_id=default_prediction_server_id,
            registered_model_version_id=registered_global_model.version_id,
        )

        deployment_ids[global_model] = deployment.id

    return deployment_ids
