# Interfejs użytkownika

import tkinter as tk
from game_engine.engine import init_game_status, update_game_status

class SnakeGameGUI:

    def __init__(self, root):
        self.root = root
        self.canvas_size = 400
        self.cell_size = 20
        self.board_size = (20, 20)
        self.status = init_game_status(self.board_size)

        self.canvas = tk.Canvas(root, width = self.canvas_size, height=self.canvas_size, bg="white")
        self.canvas.pack()

        self.root.bind("<Key>", self.handle_key)
        self.update_ui()


    def handle_key(self, event):
        key_map = {"Up": "up", "Down": "down", "Left": "left", "Right": "right"}
        if event.keysym in key_map:
            self.status["direction"] = key.map[event.keysym]
            self.status = update_game_status(self.status)