# Copyright 2024 DataRobot, Inc. and its affiliates.
# All rights reserved.
# DataRobot, Inc.
# This is proprietary source code of DataRobot, Inc. and its
# affiliates.
# Released under the terms of DataRobot Tool and Utility Agreement.

import datetime as dt
import uuid

import pandas as pd


def test_grade_deployment_prediction(project_context, make_prediction):
    grading_deployment_id = project_context.catalog.load('grading_deployment_id')

    input_df = pd.DataFrame({'prompt': ["tell me about DataRobot"]})
    input_df["association_id"] = f"{uuid.uuid4().hex}_{dt.datetime.now()}"

    grade_output = make_prediction(input_df.to_dict(orient="records"), grading_deployment_id)
    grade_df = pd.DataFrame(grade_output["data"])

    assert len(grade_df.index) > 0


def test_guard_deployment_prediction(project_context, make_prediction):
    guard_deployment_id = project_context.catalog.load('guard_deployment_id')
    prompt_feature_name = project_context.params['deploy_guardrail']['prompt_feature_name']

    guard_input = [{prompt_feature_name: "tell me about DataRobot"}]
    guard_output = make_prediction(guard_input, guard_deployment_id)

    guard_df = pd.DataFrame(guard_output["data"])

    assert len(guard_df.index) > 0


def test_toxicity_deployment_prediction(project_context, make_prediction):
    deployment_id = project_context.catalog.load('global_model_deployment_ids')['toxicity']

    pred_data = [{"text": "tell me about DataRobot"}]
    response = make_prediction(pred_data, deployment_id)

    assert len(pd.DataFrame(response["data"]).index) > 0


def test_refusal_deployment_prediction(project_context, make_prediction):
    deployment_id = project_context.catalog.load('global_model_deployment_ids')['refusal']

    pred_data = [{"text": "tell me about DataRobot"}]
    response = make_prediction(pred_data, deployment_id)

    assert len(pd.DataFrame(response["data"]).index) > 0


def test_sentiment_deployment_prediction(project_context, make_prediction):
    deployment_id = project_context.catalog.load('global_model_deployment_ids')['sentiment']

    pred_data = [{"text": "tell me about DataRobot"}]
    response = make_prediction(pred_data, deployment_id)

    assert len(pd.DataFrame(response["data"]).index) > 0


def test_injection_deployment_prediction(project_context, make_prediction):
    deployment_id = project_context.catalog.load('global_model_deployment_ids')['injection']

    pred_data = [{"text": "tell me about DataRobot"}]
    response = make_prediction(pred_data, deployment_id)

    assert len(pd.DataFrame(response["data"]).index) > 0
