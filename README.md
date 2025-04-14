# s27929-s28751-python-game
Projekt nr 1 - Gra "Snake" wykonana w języku python

---
## ▶️ Jak uruchomić grę?

1. Przejdź do katalogu z projektem:
    ```
    cd s27929-s28751-python-game
    ```

2. Uruchom grę:
    ```
    python main.py
    ```
    
## 🧪 Jak uruchomić testy?

1. Upewnij się, że masz zainstalowane **pytest**:
    ```
    pip install pytest
    ```

2. Uruchom testy w katalogu głównym projektu:
    ```
    python -m pytest
    ```

## ☁️ Jak uruchomić projekt z bazą danych?

1. Utwórz plik ```.env``` na wzór ```.env.example```.

2. Uzupełnij dane logowania do MongoDB Atlas w ```.env```:
    ```

    MONGO_URI=mongodb+srv://<username>:<password>@<host>/?retryWrites=true&w=majority
    ```

3. Upewnij się, że masz zainstalowane:
    ```

    pip install pymongo python-dotenv
    ```
---