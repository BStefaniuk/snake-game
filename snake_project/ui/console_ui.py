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

        self.canvas = tk.Canvas(root, width = self.canvas_size, height=self.canvas_size, bg="pink")
        self.canvas.pack()

        self.root.bind("<Key>", self.handle_key)
        self.update_ui()


    def handle_key(self, event):
        key_map = {"Up": "up", "Down": "down", "Left": "left", "Right": "right"}
        if event.keysym in key_map:
            self.status["direction"] = key.map[event.keysym]
            self.status = update_game_status(self.status)

            if self.status["game_over"]:
                self.canvas.create_text(200, 200, text="GAME OVER", fill="red", font=("Arial", 24))
            else:
                self.update_ui()


    def update_ui(self):
        self.canvas.delete("all")
        for x in range(self.board_size[0]):
            for y in range(self.board_size[1]):
                self.canvas.create_rectangle(
                    x * self.cell_size, y * self.cell_size, 
                    (x + 1) * self.cell_size, (y + 1) * self.cell_size,
                    outline = "gray"
                )

        for segemnt in self.status["snake_position"]:
            x, y = segemnt
            self.canvas.create_rectangle(
                x * self.cell_size, y * self.cell_size,
                (x+1) * self.cell_size, (y+1) * self.cell_size,
                fill="green"
            )