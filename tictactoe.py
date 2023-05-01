#tictactoe.py
import tkinter as tk

root = tk.Tk()
root.resizable(False, False)
root.title("Tic Tac Toe")

tk.Label(root, text="Tic Tac Toe", font=('Ariel',25)).pack()

play_area = tk.Frame(root, width=300, height=300, bg='white')

XO_points = []

class XOPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = None
        self.button = tk.Button(play_area, text="", width=10, height=5)
        self.button.grid(row=x, column=y)
    def reset(self):
        self.button.configure(text="", bg="white")
        self.value = None

for x in range(1, 4):
    for y in range(1, 4):
        XOPoint(x, y)

play_area.pack(padx=10, pady=10)

root.mainloop()
