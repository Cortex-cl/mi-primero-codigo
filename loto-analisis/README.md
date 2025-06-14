# 📊 Análisis de Resultados del Loto 2025

Este script procesa un archivo de Excel con los resultados del Loto de Chile del año 2025, agrupando los datos por mes para mostrar las frecuencias de:

- Los 6 números principales
- El número Comodín
- El Multiplicador

## 🧪 Requisitos

- Python 3.10+
- pandas
- openpyxl (para leer archivos `.xlsx`)
- locale compatible con español (`es_ES.UTF-8`)

## 🗂 Estructura del proyecto

loto-analisis/
├── data/
│ └── loto_2025.xlsx
├── loto_analisis.py
├── README.md
├── .gitignore
└── requirements.txt



## 🚀 Cómo usar

1. Clonar el repositorio:
   git clone https://github.com/tu-usuario/loto-analisis.git
   cd loto-analisis

2. Crear entorno virtual (opcional pero recomendado):
python -m venv venv
source venv/bin/activate  # o .\venv\Scripts\activate en Windows
Instalar dependencias:


3. pip install -r requirements.txt

4. Ejecutar el script:
python loto_analisis.py

📌 Notas

El script usa locale.setlocale para leer fechas en español. Asegúrate de tener el locale es_ES.UTF-8 habilitado en tu sistema.

El archivo Excel debe estar en la carpeta data/ y llamarse loto_2025.xlsx.

🧠 Futuras mejoras

Generar gráficos de frecuencias

Interfaz en línea de comandos (CLI)

Exportar resultados a CSV o HTML

Autor: [Cortex-cl]