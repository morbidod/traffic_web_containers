# Usa un'immagine Python leggera
FROM python:3.11-slim

# Crea la directory per i log
WORKDIR /app
RUN mkdir -p /data

# Copia lo script
COPY app.py .

# Comando di avvio
CMD ["python", "app.py"]