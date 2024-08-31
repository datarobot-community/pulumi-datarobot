from pathlib import Path
import pulumi
import pulumi_datarobot as datarobot
from kedro.framework.session import KedroSession
from kedro.framework.startup import bootstrap_project

bootstrap_project(Path("."))
with KedroSession.create() as session:
    session.run()
