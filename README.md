# s27929-s28751-python-game
Projekt nr 1 - Gra "Snake" wykonana w języku python


---

## 🧪 Jak uruchomić testy?

1. Upewnij się, że masz zainstalowane **pytest**:
    ```
    pip install pytest
    ```

2. Uruchom testy w katalogu głównym projektu:
    ```
    python -m pytest
    ```

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

---

## 👥 Skład zespołu

- s27929 – odpowiedzialny za **logikę gry (silnik)**, testy jednostkowe
- s28751 – odpowiedzialny za **interfejs użytkownika (GUI)** w Tkinterze

---

## ✅ Funkcjonalności silnika

- Przemieszczanie węża (w układzie kartezjańskim)
- Kolizja z samym sobą
- Przenikanie przez ściany (wrap)
- Zbieranie owoców i zwiększanie prędkości
- System punktacji i żyć
- Zakończenie gry (game over)

---

## 📌 Uwaga

> Silnik gry (engine.py) nie zawiera żadnych odwołań do I/O (brak `print`, `input`, `tkinter` itp.) – jego funkcje są testowalne i całkowicie niezależne od GUI.

---
