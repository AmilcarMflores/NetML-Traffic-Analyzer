# model/model_utils.py

import joblib
import os

MODEL_PATH = "/home/romerproblem/PycharmProjects/Sniffer/saved_model/classifier_model.pkl"

def save_model(model):
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"[+] Modelo guardado en: {MODEL_PATH}")

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("No se encontró el modelo entrenado. ¿Ya lo entrenaste?")
    return joblib.load(MODEL_PATH)
