# Copyright 2024 DataRobot, Inc. and its affiliates.
# All rights reserved.
# DataRobot, Inc.
# This is proprietary source code of DataRobot, Inc. and its
# affiliates.
# Released under the terms of DataRobot Tool and Utility Agreement.

import datetime as dt
import uuid


def test_rag_deployment_prediction(project_context, make_prediction):
    rag_deployment_id = project_context.catalog.load('rag_deployment_id')
    prompt_feature_name = project_context.params['prep_dr_rag_custom_model']['custom_model']['prompt_feature_name']

    association_id = f"{uuid.uuid4().hex}_{dt.datetime.now()}"

    rag_input = [{prompt_feature_name: "tell me about DataRobot", "association_id": association_id}]
    rag_output = make_prediction(rag_input, rag_deployment_id)

    answer = rag_output["data"][0]['prediction']
    references = rag_output["data"][0]['extraModelOutput']['CITATION_CONTENT_0']
    latency = rag_output["data"][0]['extraModelOutput']['datarobot_latency']

    assert len(answer) > 0 and len(references) > 0 and latency > 0
