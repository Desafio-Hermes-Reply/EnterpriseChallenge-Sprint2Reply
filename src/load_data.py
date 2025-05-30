import pandas as pd
import os

# 📁 Caminho da pasta data
DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data')

# 🔧 Funções para carregar os datasets
def load_temperatura_motor():
    path = os.path.join(DATA_PATH, 'electric-motor-temperature', 'measures_v2.csv')
    return pd.read_csv(path)

def load_luminosidade_ambiente():
    path = os.path.join(DATA_PATH, 'cubems-smart-building-energy-and-iaq-data', '2018Floor1.csv')
    return pd.read_csv(path)

def load_vibracao_maquinas():
    path = os.path.join(DATA_PATH, 'gear-vibration', 'eccentricity.csv')
    return pd.read_csv(path)
