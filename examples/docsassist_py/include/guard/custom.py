# Copyright 2024 DataRobot, Inc. and its affiliates.
# All rights reserved.
# DataRobot, Inc.
# This is proprietary source code of DataRobot, Inc. and its
# affiliates.
# Released under the terms of DataRobot Tool and Utility Agreement.

import re

import pandas as pd
import os
import json
from datarobot_drum import RuntimeParameters


def load_model(code_dir):
    print(os.environ)
    blocklist = json.loads(RuntimeParameters.get("blocklist"))
    prompt_feature_name = RuntimeParameters.get("prompt_feature_name")
    regex = "({})".format("|".join([keyword for keyword in blocklist]))
    return regex, prompt_feature_name


def score(data, model, **kwargs):
    regex, prompt_feature_name = model

    output = []
    positive_label = kwargs["positive_class_label"]
    negative_label = kwargs["negative_class_label"]
    for prompt in data[prompt_feature_name]:
        block_input = bool(re.search(regex, prompt, re.IGNORECASE))
        output.append(
            {positive_label: float(block_input), negative_label: 1 - float(block_input)}
        )
    return pd.DataFrame(output)
