# Copyright 2024 DataRobot, Inc. and its affiliates.
# All rights reserved.
# DataRobot, Inc.
# This is proprietary source code of DataRobot, Inc. and its
# affiliates.
# Released under the terms of DataRobot Tool and Utility Agreement.

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    import tempfile
import logging

log = logging.getLogger(__name__)


def prepare_yaml_content(*args: Any, **kwargs: Any) -> dict[str, Any] | list[Any]:
    """Passthrough node for gathering content to be serialized to yaml from upstream node(s).

    Parameters
    ----------
    args : Any
        Positional arguments to be passed as a list to the yaml renderer. If
        specified, all keyword arguments will be ignored.
    kwargs : Any
        Keyword arguments to be passed as a dict to the yaml render. Ignored
        if any positional arguments are passed.

    Returns
    -------
    list or dict :
        The yaml-serializable python object to pass to the yaml renderer.
    """
    if len(args):
        return list(args)
    else:
        return kwargs


def make_basic_deployment_asset(
    custom_py: str, parameters_yaml: Any | None = None
) -> Path:
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
    import pulumi

    import yaml

    d = Path(".")
    d.mkdir(parents=True, exist_ok=True)

    path_to_d = str(d)

    log.info("Creating temporary directory for deployment assets at %s", path_to_d)
    file_assets = []
    with open(Path(path_to_d, "custom.py"), "w") as f:
        f.write(custom_py)
        file_assets.append(pulumi.FileAsset(str(Path(path_to_d, "custom.py"))))

    if parameters_yaml is not None:
        with open(Path(path_to_d, "parameters.yaml"), "w") as f:
            f.write(yaml.dump(parameters_yaml))
        file_assets.append(pulumi.FileAsset(str(Path(path_to_d, "parameters.yaml"))))
    return file_assets
