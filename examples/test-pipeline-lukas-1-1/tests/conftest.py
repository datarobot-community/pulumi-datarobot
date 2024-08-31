# Copyright 2024 DataRobot, Inc. and its affiliates.
# All rights reserved.
# DataRobot, Inc.
# This is proprietary source code of DataRobot, Inc. and its
# affiliates.
# Released under the terms of DataRobot Tool and Utility Agreement.

import pathlib

import datarobot as dr
import pytest
import requests
from kedro.framework.session import KedroSession
from kedro.framework.startup import bootstrap_project
from kedro.runner import ThreadRunner


@pytest.fixture(scope="session", autouse=True)
def kedro_session():
    project_path = pathlib.Path(".").resolve()
    bootstrap_project(project_path)
    kedro_session = KedroSession.create(project_path)
    kedro_session.run(runner=ThreadRunner())  # runs the pipeline
    return kedro_session


@pytest.fixture
def project_context(kedro_session):
    return kedro_session.load_context()


@pytest.fixture
def dr_client(project_context):
    dr_api_key = project_context.config_loader["credentials"]["datarobot"]["api_token"]
    dr_endpoint = project_context.config_loader["credentials"]["datarobot"]["endpoint"]

    client = dr.Client(dr_api_key, dr_endpoint)
    dr.client.set_client(client)

    return client


@pytest.fixture  # all models deployed in the same prediction server
def pred_server(project_context, dr_client):
    rag_deployment_id = project_context.catalog.load("rag_deployment_id")
    pred_server = dr_client.get(f"deployments/{rag_deployment_id}").json()[
        "defaultPredictionServer"
    ]
    return pred_server


@pytest.fixture
def make_prediction(project_context, pred_server):
    def predict(input_json, deployment_id):
        pred_server_url = pred_server["url"]
        datarobot_key = pred_server["datarobot-key"]

        dr_api_key = project_context.config_loader["credentials"]["datarobot"][
            "api_token"
        ]
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {dr_api_key}",
            "DataRobot-key": datarobot_key,
        }

        url = "{pred_server_url}/predApi/v1.0/deployments/{deployment_id}/predictions"
        response = requests.post(
            url.format(pred_server_url=pred_server_url, deployment_id=deployment_id),
            headers=headers,
            json=input_json,
        ).json()
        return response

    return predict
