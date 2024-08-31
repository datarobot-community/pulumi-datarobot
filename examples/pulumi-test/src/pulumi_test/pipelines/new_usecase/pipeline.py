"""
This is a boilerplate pipeline 'new_usecase'
generated using Kedro 0.19.6
"""

from kedro.pipeline import Pipeline, pipeline, node
import pulumi_datarobot


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=pulumi_datarobot.UseCase,
                inputs={
                    "resource_name": "params:usecase.resource_name",
                    "name": "params:usecase.name",
                    "description": "params:usecase.description",
                },
                outputs="use_case",
            )
        ]
    )
