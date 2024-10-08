def load_model(input_dir):
    return 6 / 0

def score(data, model, **kwargs):
    import pandas as pd
    preds = pd.DataFrame([42 for _ in range(data.shape[0])], columns=["Predictions"])
    return preds