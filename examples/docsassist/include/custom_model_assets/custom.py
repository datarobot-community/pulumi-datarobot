# Copyright 2024 DataRobot, Inc. and its affiliates.
# All rights reserved.
# DataRobot, Inc.
# This is proprietary source code of DataRobot, Inc. and its
# affiliates.
# Released under the terms of DataRobot Tool and Utility Agreement.

# Copyright 2023 DataRobot, Inc. and its affiliates.
#
# All rights reserved.
#
# This is proprietary source code of DataRobot, Inc. and its affiliates.
# Released under the terms of DataRobot Tool and Utility Agreement.
import os
from typing import Any

import pandas as pd
from custom_model_entities import get_custom_model_llm_blueprint_config
from custom_model_loader import custom_model_loader
from custom_model_score import custom_model_score
from language_models.language_model_interface import LanguageModel


def load_model(*args: Any, **kwargs: Any) -> LanguageModel:
    """Load the model object to be used in `score`. This custom model hook is called at runtime."""
    return custom_model_loader()


def score(data: pd.DataFrame, model: LanguageModel, **kwargs: Any) -> pd.DataFrame:
    config = get_custom_model_llm_blueprint_config()
    result_list, docs = custom_model_score(data, model, config)
    return pd.DataFrame({os.environ["TARGET_NAME"]: result_list, "references": docs})
