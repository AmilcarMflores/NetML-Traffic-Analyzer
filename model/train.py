# model/train.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from model.model_utils import save_model

def train_model(csv_path="../data/captured_packets.csv"):
    df = pd.read_csv(csv_path)

    if 'label' not in df.columns:
        raise ValueError("El dataset no contiene la columna 'label'.")

    # Filtrar características (excluimos timestamp, IPs y etiquetas)
    X = df[['protocol', 'length']]
    y = df['label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    acc = clf.score(X_test, y_test)
    print(f"[+] Precisión en test: {acc:.2%}")

    save_model(clf)
