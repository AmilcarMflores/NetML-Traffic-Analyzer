# capture/feature_extractor.py
import requests
from scapy.layers.inet import IP, TCP, UDP
from datetime import datetime

def extract_features(packet):


    if IP in packet:
        timestamp = datetime.now().isoformat()
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto
        length = len(packet)


        ip=""
        if ".".join(str(src_ip).split(".")[:-1])=='192.168.0':
            ip=dst_ip
        if ".".join(str(dst_ip).split(".")[:-1])=='192.168.0':
            ip=src_ip

        #ip = dst_ip
        #headers = {"x-apikey": "0c8c7b204c33df8bce2965c2018d1d235eadf1dae971ca95bdc00c0a962fa44a"}
        #response = requests.get(f"https://www.virustotal.com/api/v3/ip_addresses/{ip}", headers=headers)

        #data = response.json()
        #print(data["data"]["attributes"])

        #api_key = '13a50cf3e816be9a1148b40a864dbb82772862a1528e85d6b85683b32eda179f9146ff9e7218591c'
        # IP que deseas verificar
        #ip = src_ip
        # Endpoint
        #url = 'https://api.abuseipdb.com/api/v2/check'
        # Parámetros
        #params = {
        #    'ipAddress': ip,
        #    'maxAgeInDays': 90,
        #    'verbose': True
        #}
        # Headers
        #headers = {
        #    'Key': api_key,
        #    'Accept': 'application/json'
        #}
        # Hacer la petición
        #response = requests.get(url, headers=headers, params=params)
        # Mostrar la respuesta
        #print(response.status_code)
        #print(response.json())

        print(ip)
        return [
            timestamp,
            src_ip,
            dst_ip,
            proto,     # Protocolo (6=TCP, 17=UDP)
            length,
            0          # Etiqueta por defecto (0 = no riesgoso). Se actualizará si se entrena.
        ]
    return None
