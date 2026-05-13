# Usa un'immagine Python leggera
FROM python:3.11-slim
RUN pip install matplotlib scapy

WORKDIR /app
RUN mkdir -p /data /output

COPY app-c.py .

CMD ["python", "app-c.py"]
