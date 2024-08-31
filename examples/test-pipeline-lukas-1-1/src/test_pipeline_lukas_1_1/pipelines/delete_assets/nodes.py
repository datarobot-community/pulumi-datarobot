# Copyright 2024 DataRobot, Inc. and its affiliates.
# All rights reserved.
# DataRobot, Inc.
# This is proprietary source code of DataRobot, Inc. and its
# affiliates.
# Released under the terms of DataRobot Tool and Utility Agreement.

import json
import logging

import datarobot as dr

log = logging.getLogger(__name__)


def _write_exception_message(asset_id: str, asset_type: str):
    log.info(
        f"Unable to delete the {asset_type} associated with {asset_id}; "
        "check that the asset(s) weren't previously deleted."
    )
    # log.info(traceback.format_exc())

def delete_assets(
    endpoint: str,
    token: str,
    global_model_deployment_ids: dict[str, str],
    grading_deployment_id: str,
    guard_deployment_id: str,
    rag_custom_model_id: str,
    rag_custom_model_version_id: str,
    rag_deployment_id: str,
    application_id: str,
):
    """Delete assets created by the pipeline."""
    client = dr.Client(endpoint=endpoint, token=token)

    def delete_deletable_assets_app(application_id):
        app_url = f"customApplications/{application_id}/"

        try:
            custom_app_json = client.get(app_url).json()
            client.delete(app_url)
            client.delete(
                f"customApplicationSources/{custom_app_json['customApplicationSourceId']}/"
            )
        except Exception:
            _write_exception_message(application_id, "application")
            pass

    def get_custom_model_llm_blueprint_id(custom_model_id, custom_model_version_id):
        items = client.get(f"customModels/{custom_model_id}/versions/{custom_model_version_id}/").json()["items"]
        custom_model_llm_blueprint_config_id = [i for i in items if i["fileName"] == "custom_model_llm_blueprint_config.json"][0]["id"]

        content = client.get(f"customModels/{custom_model_id}/versions/{custom_model_version_id}/items/{custom_model_llm_blueprint_config_id}").json()["content"]
        return json.loads(json.loads(content))["llm_blueprint_id"]

    def delete_deletable_assets_custom_model(custom_model_id, custom_model_version_id):
        llm_blueprint_id = None
        try:
            llm_blueprint_id = get_custom_model_llm_blueprint_id(custom_model_id, custom_model_version_id)
        except Exception:
            log.info("No llm blueprint found?")
            # print(e)
        if llm_blueprint_id:
            llm_blueprint = dr.models.genai.llm_blueprint.LLMBlueprint.get(llm_blueprint_id)
            playground = dr.models.genai.Playground.get(llm_blueprint.playground_id)
            use_case = dr.UseCase.get(playground.use_case_id)
            datasets: list[dr.Dataset] = use_case.list_datasets()
            vector_databases = dr.models.genai.vector_database.VectorDatabase.list(use_case=use_case)
            try:
                llm_blueprint.delete()
            except Exception:
                _write_exception_message(llm_blueprint.id, "llm_blueprint")
                pass
            try:
                playground.delete()
            except Exception:
                _write_exception_message(playground.id, "playground")
                pass
            for vdb in  vector_databases:
                try:
                    vdb.delete()
                except Exception:
                    _write_exception_message(vdb.id, "vector_database")
                    pass
            for ds in datasets:
                try:
                    ds.delete(dataset_id=ds.id)
                except Exception:
                    _write_exception_message(ds.id, "dataset")
                    pass
            try:
                use_case.delete(use_case_id=use_case.id)
            except Exception:
                _write_exception_message(use_case.id, "use_case")
                pass
        try:
            dr.CustomInferenceModel.get(custom_model_id).delete()
        except Exception:
            _write_exception_message(custom_model_id, "custom_model")
            pass

    def delete_deletable_assets_deployment(deployment_id):
        deployment = dr.Deployment.get(deployment_id)
        registered_model_id = deployment.model_package['registered_model_id']
        custom_model_id = deployment.model["custom_model_image"]["custom_model_id"]
        custom_model_version_id = deployment.model["custom_model_image"]["custom_model_version_id"]
        try:
            deployment.delete()
        except Exception:
            _write_exception_message(deployment.id, "deployment")
            pass
        try:
            client.delete(f"registeredModels/{registered_model_id}/")
        except Exception:
            _write_exception_message(registered_model_id, "registered_model")
            pass
        delete_deletable_assets_custom_model(custom_model_id, custom_model_version_id)




    delete_deletable_assets_app(application_id)
    log.info(global_model_deployment_ids)
    for deployment_id in global_model_deployment_ids.values():
        delete_deletable_assets_deployment(deployment_id)
    delete_deletable_assets_deployment(grading_deployment_id)
    delete_deletable_assets_deployment(guard_deployment_id)
    delete_deletable_assets_deployment(rag_deployment_id)
