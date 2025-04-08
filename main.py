from tkinter import Tk
from snake_project.ui.console_ui import SnakeGameGUI

if __name__ == "__main__":
    root = Tk()
    root.title("Snake Game – wersja testowa")
    game = SnakeGameGUI(root)
    root.mainloop()
