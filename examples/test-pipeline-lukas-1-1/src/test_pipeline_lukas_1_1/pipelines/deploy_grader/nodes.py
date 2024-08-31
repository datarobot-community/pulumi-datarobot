# Copyright 2024 DataRobot, Inc. and its affiliates.
# All rights reserved.
# DataRobot, Inc.
# This is proprietary source code of DataRobot, Inc. and its
# affiliates.
# Released under the terms of DataRobot Tool and Utility Agreement.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    import tempfile


def make_basic_deployment_asset(
    custom_py: str, parameters_yaml: Any | None = None
) -> tempfile.TemporaryDirectory:
    """Assemble a directory with a custom.py for a simple custom model deployment.

    Parameters
    ----------
    custom_py : str
        custom.py contents for the custom model deployment
    parameters_yaml : str, optional
        parameters_yaml contents for the custom model deployment

    Returns
    -------
    tempfile.TemporaryDirectory :
        Temp directory containing the custom.py for the custom model deployment.
    """
    import os
    import tempfile

    import yaml

    d = tempfile.TemporaryDirectory()
    path_to_d = d.name

    with open(os.path.join(path_to_d, "custom.py"), "w") as f:
        f.write(custom_py)

    if parameters_yaml is not None:
        with open(os.path.join(path_to_d, "parameters.yaml"), "w") as f:
            f.write(yaml.dump(parameters_yaml))

    return d
