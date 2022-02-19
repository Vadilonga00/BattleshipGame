import tkinter as tk

import Utils
import game_board
import inputs
import ship_types

args = inputs.initialize_parser()
root = tk.Tk()
root.title('PlayBoard')

play_board = board = [['-'] * args.columns for x in range(args.rows)]
board[0][0] = 1


def on_click(row_guess, col_guess, event):
    if board[row_guess-1][col_guess-1] == 1:
        color = "red"
    else:
        color = "blue"
    event.widget.config(bg=color)
    board[row_guess-2][col_guess-2] = color


def gui_board(args):
    for i in range(1, args.rows+1):
        for j in range(1, args.columns+1):
            text = f'({i} - {j})'
            L = tk.Label(root, text=text, bg='grey')
            L.grid(row=i, column=j)
            L.bind('<Button-1>', lambda e, row_guess=i, col_guess=j: on_click(row_guess, col_guess, e))


gui_board(args)
root.mainloop()
