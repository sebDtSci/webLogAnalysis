import pandas as pd
import re

# Fonction pour vérifier si une adresse IP est valide
def is_valid_ip(ip_addr):
    return re.match(r'^(\d{1,3}\.){3}\d{1,3}$', ip_addr) is not None

data = pd.read_csv('E-commerce Website Logs.csv')
data['age'] = pd.to_numeric(data['age'], errors='coerce')  # Convertit en NaN les valeurs non numériques
data['age'].fillna(0, inplace=True)  # Remplace NaN par 0
data['age'] = data['age'].astype(int)

data = data[data['ip'].apply(is_valid_ip)]

data.to_csv('E-commerce Website Logs_cleaned.csv', index=False)
