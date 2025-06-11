# scripts/run_predict.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scapy.all import sniff
from scapy.layers.inet import IP
from capture.feature_extractor import extract_features
from model.predict import predict

def packet_callback(packet):
    features = extract_features(packet)
    if features:
        # Extraer solo columnas requeridas para el modelo
        protocol = int(features[3])
        length = int(features[4])
        prediction, proba = predict([protocol, length])

        estado = "RIESGOSO ⚠️" if prediction == 1 else "Seguro ✅"
        print(f"[{estado}] Protocolo: {protocol} | Longitud: {length} | Confianza: {proba:.2%}")

def main():
    print("[+] Monitoreando tráfico en tiempo real...")
    try:
        sniff(prn=packet_callback, iface="wlp3s0", store=False)
    except PermissionError:
        print("[!] Este script necesita permisos de superusuario (sudo).")
    except KeyboardInterrupt:
        print("\n[+] Captura interrumpida por el usuario.")

if __name__ == "__main__":
    main()
