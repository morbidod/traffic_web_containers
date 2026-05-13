import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Seed per coerenza dei risultati
np.random.seed(42)

# Data corrente (simulata 2026 come da istruzioni)
base_time = datetime(2026, 5, 8, 9, 0, 0)
rows = []

# Liste di entità per arricchire il log
normal_users = ['alessandro.verdi', 'giulia.bianchi', 'marco.rossi', 'luca.neri', 'elena.gialli']
attack_users = ['admin', 'root', 'user', 'guest', 'support', 'test', 'manager', 'administrator', 'oracle', 'webmaster']

# 1. Generazione Traffico Normale (45 minuti)
# Comportamento: Pochi login, successo elevato, IP variegati
for i in range(45):
    current_minute = base_time + timedelta(minutes=i)
    num_logs = np.random.randint(1, 4)
    for _ in range(num_logs):
        log_time = current_minute + timedelta(seconds=np.random.randint(0, 60))
        rows.append({
            'timestamp': log_time.strftime('%Y-%m-%d %H:%M:%S'),
            'user': np.random.choice(normal_users),
            'ip_source': f'192.168.1.{np.random.randint(10, 50)}',
            'status': np.random.choice(['success', 'failed'], p=[0.9, 0.1])
        })

# 2. Generazione Traffico di Attacco (15 minuti)
# Comportamento: Alta frequenza (Credential Stuffing), tutti falliti, IP singolo (10.0.0.5)
attack_ip = '10.0.0.5'
for i in range(45, 60):
    current_minute = base_time + timedelta(minutes=i)
    num_logs = np.random.randint(15, 30) 
    for _ in range(num_logs):
        log_time = current_minute + timedelta(seconds=np.random.randint(0, 60))
        rows.append({
            'timestamp': log_time.strftime('%Y-%m-%d %H:%M:%S'),
            'user': np.random.choice(attack_users),
            'ip_source': attack_ip,
            'status': 'failed'
        })

# Creazione DataFrame e salvataggio
df_concorso = pd.DataFrame(rows)
df_concorso.to_csv('log_vpn_cyber_analysis.csv', index=False)

print(f"Dataset generato con {len(df_concorso)} righe.")
print(df_concorso.tail(5)) # Mostra la fase di attacco finale