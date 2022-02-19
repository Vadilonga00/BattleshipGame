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


def on_click(ship_list, row_guess, col_guess, event):
    player = 1
    color = None
    for i in ship_list:
        if ship_types.Ship.is_hit(i, row_guess, col_guess):
            color = "red"
            if ship_types.Ship.is_sunk(i):
                if game.is_win(ship_list):
                    print(f'\nPlayer {player} wins the game')
                    sys.exit()
                else:
                    print('\nHit and sunk a ship, shoot again!')
                    #Utils.game_variant(ship_list1, ship_list2, args, play_board1, play_board2, player)
            else:
                print('\nHit, shoot again!')
                #Utils.game_variant(ship_list1, ship_list2, args, play_board1, play_board2, player)
    if color != 'red':
        color = "blue"
        print('\nMiss, pass the computer to Player2')
    event.widget.config(bg=color)
    board[row_guess-1][col_guess-1] = color


def gui_board(args):
    for i in range(1, args.rows+1):
        for j in range(1, args.columns+1):
            text = f'({i} - {j})'
            L = tk.Label(root, text=text, bg='grey')
            L.grid(row=i, column=j)
            L.bind('<Button-1>', lambda e, row_guess=i, col_guess=j: on_click(ships, row_guess, col_guess, e))


gui_board(args)
root.mainloop()
