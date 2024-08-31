from pathlib import Path
import pulumi
import pulumi_datarobot as datarobot
from kedro.framework.session import KedroSession
from kedro.framework.startup import bootstrap_project

bootstrap_project(Path("."))
with KedroSession.create() as session:
    # session.run(pipeline_name="deploy_guardrail")
    session.run(to_outputs=["application"])
# with KedroSession.create() as session:
#     session.run(pipeline_name="setup_custom_metrics")
# with KedroSession.create() as session:
#     session.run(pipeline_name="prep_dr_rag_custom_model")
