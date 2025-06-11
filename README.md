# 🚀 NETML-TRAFFIC-ANALYZER 
**Machine Learning-based Network Traffic Analyzer**  
*Clasifica tráfico de red en tiempo real como seguro o riesgoso usando Random Forest.*

---

## 📌 Características Principales
- **Captura de paquetes** en tiempo real con `scapy` (IPv4, TCP/UDP).
- **Extracción de features**: IPs, protocolo, longitud del paquete.
- **Modelo de ML**: Random Forest entrenado para detectar tráfico sospechoso.
- **Predicción en tiempo real** con confianza (%).
- **Fácil integración**: Soporta CSV para almacenamiento y análisis posterior.

---

## 🛠️ Tecnologías Usadas
- **Lenguaje**: Python 3.8+
- **Librerías**:  
  ![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
  ![Scapy](https://img.shields.io/badge/Scapy-2.4.0%2B-orange)
  ![Pandas](https://img.shields.io/badge/Pandas-1.0.0%2B-red)
  ![Scikit-learn](https://img.shields.io/badge/scikit--learn-0.22.0%2B-green)
  ![Joblib](https://img.shields.io/badge/joblib-0.14.0%2B-yellow)

---

## Instala las dependencias

`pip install -r requirements.txt`

---

## ⚡ Instalación Rápida
1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/NETML-TRAFFIC-ANALYZER.git
   cd NETML-TRAFFIC-ANALYZER

# Uso

`# Capture packets (sudo required)`
`sudo python scripts/run_capture.py -i eth0 -c 100`

# Train model (requires labeled data)
`python scripts/run_train.py`

# Real-time prediction
`sudo python scripts/run_predict.py`