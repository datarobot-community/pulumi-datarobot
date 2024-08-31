# Copyright 2024 DataRobot, Inc. and its affiliates.
# All rights reserved.
# DataRobot, Inc.
# This is proprietary source code of DataRobot, Inc. and its
# affiliates.
# Released under the terms of DataRobot Tool and Utility Agreement.

from __future__ import annotations


def log_outputs(
    endpoint: str,
    rag_deployment_id: str,
    grading_deployment_id: str,
    guard_deployment_id: str,
    application_id: str,
    rag_deployment_name: str,
    grading_deployment_name: str,
    guard_deployment_name: str,
    app_name: str,
) -> None:
    """Log URLs for DR deployments and app.

    Parameters
    ----------
    rag_deployment_id : str
        DataRobot id of the RAG deployment
    grading_deployment_id : str
        DataRobot id of the grading deployment
    guard_deployment_id : str
        DataRobot id of the guardrail deployment
    application_id : str
        DataRobot id of the custom application
    rag_deployment_name : str
        Name of the RAG deployment
    grading_deployment_name : str
        Name of the grading deployment
    guard_deployment_name : str
        Name of the guardrail deployment
    app_name : str
        Name of the deployed custom application
    """
    import logging
    from urllib.parse import urljoin

    base_url = urljoin(endpoint, "/")
    deployment_url = base_url + "console/{deployment_id}/overview"
    application_url = base_url + "custom_applications/{application_id}/"

    logger = logging.getLogger(__name__)
    logger.info("Application is live!")
    msg = (
        "RAG deployment: "
        f"[link={deployment_url.format(deployment_id=rag_deployment_id)}]"
        f"{rag_deployment_name}[/link]"
    )
    logger.info(msg)
    msg = (
        "Grading deployment: "
        f"[link={deployment_url.format(deployment_id=grading_deployment_id)}]"
        f"{grading_deployment_name}[/link]"
    )
    logger.info(msg)
    msg = (
        "Guardrail deployment: "
        f"[link={deployment_url.format(deployment_id=guard_deployment_id)}]"
        f"{guard_deployment_name}[/link]"
    )
    logger.info(msg)
    msg = (
        "Custom application: "
        f"[link={application_url.format(application_id=application_id)}]"
        f"{app_name}[/link]"
    )
    logger.info(msg)
