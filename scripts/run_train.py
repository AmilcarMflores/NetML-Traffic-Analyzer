# scripts/run_train.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.train import train_model

def main():
    print("[+] Entrenando modelo con datos en 'data/captured_packets.csv'...")
    try:
        train_model()
    except Exception as e:
        print(f"[!] Error durante el entrenamiento: {e}")

if __name__ == "__main__":
    main()
