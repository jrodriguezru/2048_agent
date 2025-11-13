import tkinter as tk
from tkinter import Frame, Label

class GameUI(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title('2048')
        self.grid()
        self.cells = []
        self.create_widgets()

    def create_widgets(self):
        """
        The `create_widgets` function initializes the UI, creating a grid layout with cells and a score
        label in a Python GUI application.
        """
        self.main_grid = Frame(
            self, bg='#92877d', bd=3, width=400, height=400
        )
        self.main_grid.grid(pady=(80, 0))

        for i in range(4):
            row = []
            for j in range(4):
                cell = Frame(
                    self.main_grid, bg='#9e948a', width=100, height=100
                )
                cell.grid(row=i, column=j, padx=5, pady=5)
                t = Label(
                    master=cell, text='', bg='#9e948a',
                    justify='center', font=('Helvetica', 32, 'bold'),
                    width=4, height=2
                )
                t.grid()
                row.append(t)
            self.cells.append(row)

        self.score_label = Label(
            self, text="Score: 0", font=("Helvetica", 16)
        )
        self.score_label.place(x=20, y=10)

    def update_board(self, board: list[list[int]], score: int):
        """
        The `update_board` function updates the graphical representation of a game board with cell
        colors, text colors, and score information.
        
        :param board: The `board` parameter in the `update_board` method represents the current state of
        the game board in a 2048 game. It is a 2D list where each element represents the value of a cell
        on the board. The method iterates over this board to update its graphical representation.
        :param score: The `score` parameter in the `update_board` function represents the current score
        in the game. This score is used to update the score label displayed on the game board interface.
        """
        cell_colors = {
            0: "#9e948a", 2: "#eee4da", 4: "#ede0c8", 8: "#f2b179",
            16: "#f59563", 32: "#f67c5f", 64: "#f65e3b", 128: "#edcf72",
            256: "#edcc61", 512: "#edc850", 1024: "#edc53f", 2048: "#edc22e"
        }
        text_colors = {
            0: "#9e948a", 2: "#776e65", 4: "#776e65", 8: "#f9f6f2",
            16: "#f9f6f2", 32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2",
            256: "#f9f6f2", 512: "#f9f6f2", 1024: "#f9f6f2", 2048: "#f9f6f2"
        }

        for i in range(4):
            for j in range(4):
                value = board[i][j]
                text = str(value) if value != 0 else ""
                bg_color = cell_colors.get(value, "#3c3a32")
                fg_color = text_colors.get(value, "#f9f6f2")
                
                self.cells[i][j].config(text=text, bg=bg_color, fg=fg_color)
                self.cells[i][j].master.config(bg=bg_color)
        
        self.score_label.config(text=f"Score: {score}")
        self.master.update_idletasks()

def start_ui():
    root = tk.Tk()
    app = GameUI(master=root)
    return root, app
