# capture/sniffer.py

from scapy.all import sniff
from capture.feature_extractor import extract_features
import csv
from datetime import datetime

def packet_callback(packet):
    features = extract_features(packet)
    if features:
        with open('data/captured_packets.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(features)

def start_sniffing(interface="eth0", packet_count=0):
    sniff(prn=packet_callback, iface=interface, store=False, count=packet_count)
