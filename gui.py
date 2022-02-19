import tkinter as tk

import Utils
import game_board
import inputs
import ship_types

args = inputs.initialize_parser()
root = tk.Tk()
root.title('PlayBoard')


type_list = Utils.create_ship_type_list(args)
board, ship_list1 = game_board.create_board(args, type_list)


def on_click(row_guess, col_guess, event):
    if board[row_guess-1][col_guess-1] == 1:
        color = "red"
    else:
        color = "blue"
    event.widget.config(bg=color)
    board[row_guess-1][col_guess-1] = color


def gui_board(args):
    for i in range(1, args.rows+1):
        for j in range(1, args.columns+1):
            text = f'({i} - {j})'
            L = tk.Label(root, text=text, bg='grey')
            L.grid(row=i, column=j)
            L.bind('<Button-1>', lambda e, row_guess=i, col_guess=j: on_click(row_guess, col_guess, e))


gui_board(args)
root.mainloop()
