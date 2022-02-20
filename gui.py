import sys
import tkinter as tk

import Utils
import game_board
import inputs
import ship_types
import game

args = inputs.initialize_parser()
root = tk.Tk()
root.title('PlayBoard')

type_list = Utils.create_ship_type_list(args)
board, ships = game_board.create_board(args, type_list)


def on_hit(ship_list, row_guess, col_guess, event):
    player = 1
    color = "red"
    for i in ship_list:
        if ship_types.Ship.is_hit(i, row_guess, col_guess):
            if ship_types.Ship.is_sunk(i):
                if game.is_win(ship_list):
                    print(f'\nPlayer {player} wins the game!!')
                    sys.exit()
                else:
                    print('\nHit and sunk a ship!!')
            else:
                print('\nHit!')
    event.widget.config(bg=color)
    board[row_guess - 1][col_guess - 1] = color


def on_miss(row_guess, col_guess, event):
    color = "blue"
    event.widget.config(bg=color)
    board[row_guess - 1][col_guess - 1] = color
    print("\nMiss!!")


def gui_board(args):
    for i in range(1, args.rows + 1):
        for j in range(1, args.columns + 1):
            text = f'({i} - {j})'
            L = tk.Label(root, text=text, bg='grey')
            L.grid(row=i, column=j)
            for ship in ships:
                if ship_types.Ship.check_hit(ship, i, j):
                    L.bind('<Button-1>', lambda e, row_guess=i, col_guess=j: on_hit(ships, row_guess, col_guess, e))
                else:
                    L.bind('<Button-1>', lambda e, row_guess=i, col_guess=j: on_miss(row_guess, col_guess, e))


gui_board(args)
root.mainloop()
