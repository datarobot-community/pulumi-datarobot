# Copyright 2024 DataRobot, Inc. and its affiliates.
# All rights reserved.
# DataRobot, Inc.
# This is proprietary source code of DataRobot, Inc. and its
# affiliates.
# Released under the terms of DataRobot Tool and Utility Agreement.

from __future__ import annotations


def ensure_deployment_settings(
    endpoint: str,
    token: str,
    rag_deployment_id: str,
    grading_deployment_id: str,
    guard_deployment_id: str,
) -> None:
    """Ensure deployment settings are properly configured.

    Turns on data collection, drift tracking, etc.

    Parameters
    ----------
    rag_deployment_id : str
        DataRobot id of the RAG deployment
    grading_deployment_id : str
        DataRobot id of the grading deployment
    guard_deployment_id : str
        DataRobot id of the guardrail deployment
    """
    import datarobot as dr

    dr.Client(endpoint=endpoint, token=token)
    rag_deployment = dr.Deployment.get(rag_deployment_id)

    rag_deployment.update_predictions_data_collection_settings(enabled=True)
    rag_deployment.update_association_id_settings(
        column_names=["association_id"], required_in_prediction_requests=True
    )

    grading_deployment = dr.Deployment.get(grading_deployment_id)
    grading_deployment.update_predictions_data_collection_settings(enabled=True)
    grading_deployment.update_drift_tracking_settings(target_drift_enabled=True)
    grading_deployment.update_association_id_settings(
        column_names=["association_id"], required_in_prediction_requests=True
    )

    guard_deployment = dr.Deployment.get(guard_deployment_id)
    guard_deployment.update_predictions_data_collection_settings(enabled=True)
    guard_deployment.update_drift_tracking_settings(target_drift_enabled=True)

