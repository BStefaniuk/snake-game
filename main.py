import os
from tkinter import Tk
from snake_project.ui.console_ui import SnakeGameGUI
from snake_project.database.models import save_data
from snake_project.database.models import load_data_from_file

if __name__ == "__main__":
    try:
        choice = input("Czy chcesz wczytać dane z pliku? (T/N)").strip().lower()
        if choice == "t":
            filename = input("Podaj sciezke do pliku json").strip()
            if not os.path.isfile(filename):
                print(f"Plik '{filename}' nie istnieje, nie wczytano")
            else:
                #wczytanie danych
                load_data_from_file(filename)
        else:
            print("Pominieto wczytywannie z pliku")
        root = Tk()
        root.title("Snake Game")
        game = SnakeGameGUI(root)
        root.mainloop()
    finally:
        save_data() #zapis danych 
