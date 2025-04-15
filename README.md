# s27929-s28751-python-game
Projekt nr 1 - Gra "Snake" wykonana w języku python

---
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

1. Zalecane jest zainstalowanie wszystkich wymaganych bibliotek z pliku `requirements.txt`:
```bash
pip install -r requirements.txt
```

2. Uruchom testy w katalogu głównym projektu:
```bash
python -m pytest
```

## ☁️ Jak uruchomić projekt z bazą danych?

1. W katalogu głównym projektu utwórz plik ```.env``` na wzór ```.env.example```.

2. Uzupełnij dane logowania do MongoDB Atlas w ```.env```:
```
MONGO_URI=mongodb+srv://<username>:<password>@<host>/?retryWrites=true&w=majority
```
---