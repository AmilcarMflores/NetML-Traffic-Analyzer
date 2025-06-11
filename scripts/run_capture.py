# scripts/run_capture.py

import argparse


import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from capture.sniffer import start_sniffing

def main():
    parser = argparse.ArgumentParser(description="Captura paquetes de red y extrae características.")
    parser.add_argument(
        "-i", "--interface", type=str, default="eth0",
        help="Nombre de la interfaz de red (por ejemplo, eth0, wlan0)"
    )
    parser.add_argument(
        "-c", "--count", type=int, default=0,
        help="Cantidad de paquetes a capturar (0 = infinito)"
    )

    args = parser.parse_args()

    print(f"[+] Iniciando captura en interfaz: {args.interface}")
    print(f"[+] Capturando {args.count if args.count else 'ilimitados'} paquetes...")
    try:
        start_sniffing(interface=args.interface, packet_count=args.count)
    except PermissionError:
        print("[!] Error: Este script requiere privilegios de superusuario (sudo).")

if __name__ == "__main__":
    main()
