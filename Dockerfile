# 1. Pobranie oficjalnego obrazu Pythona, lekka wersja bez dodatkow
FROM python:3.11-slim

# 2. Instalacja dodatkowych pakietow systemowych potrzebnych do działania Tkintera i bazy MongoDB
RUN apt-get update && apt-get install -y tk && rm -rf /var/lib/apt/lists/*

# 3. Utworzenie folderu roboczego w konteneze gdzie beda pliki aplikacji
WORKDIR /app

# 4. Skopiowanie wszystkich plikow z folderu do kontenera
COPY . .

# 5. Instalacja zaleznosci Pythona ( pakiety z requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt

# 6. Flask jako backend (ustawienie srodowiska)
ENV FLASK_APP=api.py
ENV FLASK_RUN_HOST=0.0.0.0

# 7. Otworz port 5000, aplikacja dziala na tym porcie
EXPOSE 5000

# 8. Uruchom aplikacje, ostateczna komenda. Uruchomienie serwera Flask
CMD ["flask", "run"]
