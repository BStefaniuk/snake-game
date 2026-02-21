# Snake game

**Projekt nr 1 – Candy Snake**  
Wykonany w języku Python w ramach przedmiotu **PPY**, z graficznym interfejsem frontendowym (HTML + CSS + JS) oraz integracją z bazą danych **MongoDB Atlas**.

Gra działa przez przeglądarkę, komunikuje się z backendem (Flask) i zapisuje dane użytkowników do chmurowej bazy danych.

Prezentacja 
[CandySnake.pdf](https://github.com/user-attachments/files/20573059/CandySnake.pdf)
[CandySnake.pptx](https://github.com/user-attachments/files/20573064/CandySnake.pptx)

## ⚙️ Wymagania

- Python 3.10+ (testowane na 3.13.3)
- MongoDB Atlas (darmowe konto)
- Przeglądarka

Zainstaluj wszystkie zależności:
```bash
pip install -r requirements.txt
```

## ▶️ Jak uruchomić grę?

1. Przejdź do katalogu z projektem:
```bash
cd s27929-s28751-python-game
```

2. Skonfiguruj połączenie z bazą(niżej instrukcja)

3. Uruchom backend API:
```bash
python api.py
```
Serwer wystartuje na: ```http://127.0.0.1:5000```

4. Uruchom grę (frontend)
Otwórz plik ```ui/index.html``` w przeglądarce

## 🧪 Jak uruchomić testy?

Uruchom testy w katalogu głównym projektu:
```bash
python -m pytest
```

## ☁️ Jak skonfigurować DB(data base)?

1. Utwórz darmowe konto na [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)

2. Utwórz nowy klaster i użytkownika z hasłem

3. Skopiuj connection string z zakładki "Connect"

4. W katalogu głównym projektu utwórz plik ```.env``` na wzór ```.env.example```.

5. Uzupełnij dane logowania do MongoDB Atlas w ```.env```:
```
MONGO_URI=mongodb+srv://<username>:<password>@<host>/?retryWrites=true&w=majority
```

6. Pamiętaj, aby dodać swój adres IP w sekcji **Network Access** w MongoDB Atlas. W innym przypadku połączenie nie zadziała!
---

## 🐳 Jak uruchomić projekt w Dockerze?

1. Upewnij się, że masz plik ```.env``` z danymi dostępu do MongoDB Atlas

2. Zbuduj obraz Dockera: 
```bash
docker build -t candy-snake .
```

3. Uruchom kontener z przekazaniem pliku ```.env```:
```bash
docker run -p 5000:5000 --env-file .env candy-snake
```

4. Otwórz w przeglądarce plik ```ui/index.html```
