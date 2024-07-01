
import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.board = [""] * 9
        self.current_joueur = "X"
        self.buttons = [tk.Button(root, text="", font="Arial 20", width=5, height=2, command=lambda i=i: self.on_click(i)) for i in range(9)]
        for i, button in enumerate(self.buttons):
            button.grid(row=i//3, column=i%3)
    
    def on_click(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_joueur
            self.buttons[index].config(text=self.current_joueur)
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_joueur} Vous avez gagné!")
                self.reset_board()
            elif "" not in self.board:
                messagebox.showinfo("Tic Tac Toe", "Vous avez échoué!")
                self.reset_board()
            else:
                self.current_joueur = "O" if self.current_joueur == "X" else "X"
    
    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], 
            [0, 3, 6], [1, 4, 7], [2, 5, 8], 
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] and self.board[combo[0]] != "":
                return True
        return False
    
    def reset_board(self):
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="")
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()