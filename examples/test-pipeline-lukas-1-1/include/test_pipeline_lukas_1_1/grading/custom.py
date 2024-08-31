# Copyright 2024 DataRobot, Inc. and its affiliates.
# All rights reserved.
# DataRobot, Inc.
# This is proprietary source code of DataRobot, Inc. and its
# affiliates.
# Released under the terms of DataRobot Tool and Utility Agreement.

CLASS_LABELS = ["correct", "incorrect", "incomplete", "digress", "no_answer"]


# dummy load model function to overwrite the default
def load_model(code_dir):
    return ""


# equal prediction on each class
def score(data, model, **kwargs):
    equal_weight = 1.0 / len(CLASS_LABELS)
    for col in CLASS_LABELS:
        data[col] = equal_weight
    return data[CLASS_LABELS]
