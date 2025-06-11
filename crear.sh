#!/bin/bash

mkdir -p {capture,model,data,scripts,saved_model}

touch requirements.txt
touch .gitignore
touch README.md

# Archivos de captura
touch capture/sniffer.py
touch capture/feature_extractor.py

# Archivos del modelo
touch model/train.py
touch model/predict.py
touch model/model_utils.py

# Scripts de ejecución
touch scripts/run_capture.py
touch scripts/run_train.py
touch scripts/run_predict.py

# Dataset inicial vacío
echo "timestamp,src_ip,dst_ip,protocol,length,label" > data/captured_packets.csv

echo "Proyecto creado en packet_inspector_ml/"
