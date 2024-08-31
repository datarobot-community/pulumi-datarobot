# Copyright 2024 DataRobot, Inc. and its affiliates.
# All rights reserved.
# DataRobot, Inc.
# This is proprietary source code of DataRobot, Inc. and its
# affiliates.
# Released under the terms of DataRobot Tool and Utility Agreement.

import pytest


@pytest.fixture
def project_context(kedro_session):
    return kedro_session.load_context()


def test_app_running(project_context, dr_client):
    custom_app_id = project_context.catalog.load('deploy_dr_streamlit_app.application_id')

    url = f"customApplications/{custom_app_id}/"
    app_response = dr_client.get(url)

    assert app_response.json()['status'] == 'running' or app_response.json()['status'] == 'paused'
