# Basis-Image mit Python und apt-get
FROM python:3.11-slim

# Installiere benötigte Bibliotheken und Abhängigkeiten
RUN apt-get update && apt-get install -y \
    python3-dev \
    libsdl-image1.2-dev \
    libsdl-mixer1.2-dev \
    libsdl-ttf2.0-dev \
    libsdl1.2-dev \
    libsmpeg-dev \
    libportmidi-dev \
    libavformat-dev \
    libswscale-dev \
    libjpeg-dev \
    libfreetype6-dev \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere alle Dateien ins Image
COPY . /app

# Installiere pygame
RUN pip install pygame

# Starte das Spiel über xvfb
CMD ["xvfb-run", "python", "python.py"]
