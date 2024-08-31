# Copyright 2024 DataRobot, Inc. and its affiliates.
# All rights reserved.
# DataRobot, Inc.
# This is proprietary source code of DataRobot, Inc. and its
# affiliates.
# Released under the terms of DataRobot Tool and Utility Agreement.

import re
from typing import Any

import datarobot as dr
import pandas as pd  # type: ignore
import requests  # type: ignore
from datarobot_predict.deployment import predict  # type: ignore


def predict_grade(data, association_id, grading_deployment_id):
    input_data = {k: [data[k]] for k in ["question", "answer"]}
    for i, doc in enumerate(data["references"]):
        input_data[f"context{i + 1}"] = doc["page_content"]
        input_data[f"source{i + 1}"] = doc["metadata"]["source"]
    if "usage" in data:
        for k, v in data["usage"].items():
            input_data[k] = v
    df = pd.DataFrame(input_data)
    df.rename(columns={"question": "prompt", "answer": "response"}, inplace=True)
    df["association_id"] = association_id
    grading_deployment = dr.Deployment.get(grading_deployment_id)
    predictions_df = predict(grading_deployment, data_frame=df).dataframe

    predictions = predictions_df.to_dict(orient="records")[0]
    out_dict = {}
    # st.json(predictions)
    target_name = grading_deployment.model["target_name"]
    out_dict["grade"] = predictions[f"{target_name}_PREDICTION"]
    for key, value in predictions.items():
        if key.startswith(target_name) and key != f"{target_name}_PREDICTION":
            # Extract the grade type from the key
            grade_type = re.search(r"_(.+?)_PREDICTION", key).group(1)
            out_dict[f"class_{grade_type}"] = value
    return out_dict


def submit_grade(deployment_id, grade, association_id):
    data = [{"association_id": association_id, "actual_value": grade}]

    deployment = dr.Deployment.get(deployment_id)
    deployment.submit_actuals(data)

    return 0


def get_rag_predictions(
    data: dict,
    deployment_id_rag: str,
    api_token: str,
    datarobot_key: str,
    pred_server_url: str,
    rag_prompt_feature_name: str,
) -> dict[str, Any]:
    """Retrieve predictions from a DataRobot RAG deployment and DataRobot guard deployment"""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_token}",
        "DataRobot-key": datarobot_key,
    }
    url = "{pred_server_url}/predApi/v1.0/deployments/{deployment_id}/predictions"

    rag_input = [
        {
            rag_prompt_feature_name: data["question"],
            "association_id": data["association_id"],
            "messages": data["messages"],
        }
    ]
    print(rag_input)
    rag_response = requests.post(
        url.format(pred_server_url=pred_server_url, deployment_id=deployment_id_rag),
        headers=headers,
        json=rag_input,
    ).json()
    # print(rag_response)

    rag_df = pd.DataFrame(rag_response["data"])
    extra_model_output = rag_response["data"][0]["extraModelOutput"]
    try:
        references = extra_model_output["references"]
    except:
        references = []
        # read keys 'CITATION_CONTENT_1', 'CITATION_CONTENT_2', etc.
        for key in sorted(extra_model_output.keys()):
            if "CITATION_CONTENT" in key and extra_model_output[key]:
                doc = {}
                doc["page_content"] = extra_model_output[key]
                doc["metadata"] = {}
                source = extra_model_output[key.replace("CONTENT", "SOURCE")]
                if key.replace("CONTENT", "PAGE") in extra_model_output:
                    page = extra_model_output[key.replace("CONTENT", "PAGE")]
                    doc["metadata"]["source"] = f"{source}, page {page}"
                else:
                    doc["metadata"]["source"] = source
                references.append(doc)

    rag_response = {
        "answer": rag_df.iloc[0]["prediction"],
        "references": references,
    }
    if "usage" in extra_model_output:
        rag_response["usage"] = extra_model_output["usage"]

    return rag_response
