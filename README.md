# s27929-s28751-python-game
Projekt nr 1 - Gra "Snake" wykonana w języku python w ramach przedmiotu PPY z graficznym interfejsem oraz integracją z bazą danych MongoDB Atlas.

---
## ▶️ Wymagania

- Python 3.10+ (testowane na 3.13.3)
- MongoDB Atlas (darmowe konto)

Zainstaluj wszystkie zależności:
```bash
pip install -r requirements.txt
```

## ▶️ Jak uruchomić grę?

1. Przejdź do katalogu z projektem:
```bash
cd s27929-s28751-python-game
```

2. Uruchom grę:
```bash
python main.py
```

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