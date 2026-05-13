# Network Monitoring Dashboard con Docker

Questo progetto implementa un'architettura a microservizi per il monitoraggio e la visualizzazione del traffico di rete (simulato o reale) tramite container Docker. Il sistema è composto da un **Producer** (generatore di dati), un **Consumer** (elaboratore statistico) e un **Web Server** (Nginx) per la visualizzazione dei risultati.

## 🏗️ Architettura del Sistema

Il progetto è diviso in tre componenti principali che comunicano tra loro attraverso volumi condivisi:

1.  **Producer**: Genera dati statistici (distribuzione normale con $\mu=50$ e $\sigma=10$) e li salva in file `.pcap` o log nella cartella condivisa `./data`.
2.  **Consumer**: Monitora la cartella `./data`, elabora i file in ordine cronologico e utilizza `matplotlib` per generare un grafico andamento temporale (`chart.png`) nella cartella `./output`.
3.  **Nginx**: Funge da interfaccia utente, servendo una pagina HTML statica e rendendo accessibile il grafico generato dal Consumer tramite un volume montato.

## 📁 Struttura delle Cartelle

```text
MyDocker/
├── consumer/          # Dockerfile e script Python (Analisi e Grafici)
├── producer/          # Dockerfile e script Python (Sniffing/Generazione)
├── nginx/             # Dockerfile e configurazione Web Server
│   └── static-html-directory/ # File HTML/CSS per la dashboard
├── data/              # Volume condiviso per i dati grezzi (ignorato da git)
├── output/            # Volume condiviso per i risultati (grafici)
└── README.md
