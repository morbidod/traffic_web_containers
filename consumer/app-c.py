import time
import os
import random
from datetime import datetime
import matplotlib.pyplot as plt



# Ho bisogno di una cartella dove leggere i dati
# Cartella dove salvare l'output (montata come volume)
LOG_DIR = "./data"
OUTPUT_DIR = "./output"
#OUTPUT_DIR = os.path.join(os.path.curdir,"output")
# FILENAME_OUTPUT= 'accessi.csv'
# FILE_OUTPUT = os.path.join(OUTPUT_DIR,FILENAME_OUTPUT)
CHART_FILE = os.path.join(OUTPUT_DIR, "chart.png")
TIME_READ = 60

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

print("Avvio Consumer...")
date_format = '%Y-%m-%d %H:%M:%S'
data_accessi=[]

try:
    while True:

        #legge i file
        lista_files = os.listdir(LOG_DIR)
        print(f'lista files:{lista_files}')
        for f in lista_files:
            f1=os.path.join(LOG_DIR,f)
            with open(f1,'r') as filereader:
                data=filereader.readline()
            data_accessi.append(data)
        data_accessi_new=[(d.split(',')) for d in data_accessi]
        timestamps = [datetime.strptime(d[0], date_format) for d in data_accessi_new]
        counts = [int(d[1]) for d in data_accessi_new]

        data_pairs=sorted(zip(timestamps,counts))
        ordered_timestamps, counts = zip(*data_pairs)

        print(data_accessi_new)
        print(timestamps)
        print(counts)
        #Generazione del grafico
        plt.figure(figsize=(10, 5))
        plt.plot(ordered_timestamps, counts, marker='o', linestyle='-', color='b')
        plt.title('Traffico di Rete Rilevato')
        plt.xlabel('Orario')
        plt.ylabel('Numero di Pacchetti')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
                
        plt.savefig(CHART_FILE)
        plt.close()
        print(f"Grafico aggiornato: {CHART_FILE}")
  




            
        # Breve pausa per evitare loop infiniti in caso di errore immediato
        time.sleep(TIME_READ)

except KeyboardInterrupt:
    print("Arresto in corso...")