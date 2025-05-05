from tkinter import Tk
from snake_project.ui.console_ui import SnakeGameGUI
from snake_project.database.models import save_data

if __name__ == "__main__":
    try:
        root = Tk()
        root.title("Snake Game – wersja testowa")
        game = SnakeGameGUI(root)
        root.mainloop()
    finally:
        save_data() #zapis danych 
