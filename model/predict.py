# model/predict.py

import pandas as pd
from model.model_utils import load_model

def predict(features):
    """
    features: lista o diccionario con ['protocol', 'length']
    """
    model = load_model()

    if isinstance(features, list):
        input_df = pd.DataFrame([features], columns=["protocol", "length"])
    elif isinstance(features, dict):
        input_df = pd.DataFrame([features])
    else:
        raise ValueError("El input debe ser una lista o un diccionario.")

    prediction = model.predict(input_df)[0]
    proba = model.predict_proba(input_df)[0][prediction]

    return prediction, proba
