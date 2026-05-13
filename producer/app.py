import subprocess
import time
import os
import random
import datetime as dt



# Cartella dove salvare i log (montata come volume)
LOG_DIR = "/data"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

print("Avvio Producer...")

try:
    while True:
        # Genera un timestamp per il nome del file
        timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        filename = f"{LOG_DIR}/data_{timestamp}.csv"
        # Media (mu) = 50, Deviazione Standard (sigma) = 10
        valore_normale = random.gauss(50, 10)

        # Opzionale: converti in intero e assicurati che non sia negativo
        numero_utenti = max(0, int(valore_normale))
        print(f"File salvato su: {filename}")
        
        with open(filename,'w') as f:
            f.write(f'{timestamp},{numero_utenti}')

            
        # Breve pausa per evitare loop infiniti in caso di errore immediato
        time.sleep(30)

except KeyboardInterrupt:
    print("Arresto in corso...")