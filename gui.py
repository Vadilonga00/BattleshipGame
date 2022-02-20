import sys
import tkinter as tk

import Utils
import game
import game_board
import inputs
import ship_types

FONT = ("Calibri", 12)


class GuiApp(tk.Tk):

    def __init__(self, args, ships):
        tk.Tk.__init__(self)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = Player1Page(container, self, args, ships)
        self.frames[Player1Page] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Player1Page)

    def show_frame(self, controller):
        frame = self.frames[controller]
        frame.tkraise()


class Player1Page(tk.Frame):

    def __init__(self, parent, controller, args, ships):
        tk.Frame.__init__(self, parent)
        for i in range(1, args.rows + 1):
            for j in range(1, args.columns + 1):
                text = f'({i} - {j})'
                L = tk.Label(self, text=text, bg='grey')
                L.grid(row=i, column=j)
                for ship in ships:
                    if ship_types.Ship.check_hit(ship, i, j):
                        L.bind('<Button-1>',
                               lambda e, row_guess=i, col_guess=j: self.on_hit(ships, row_guess, col_guess, e))
                        break
                    else:
                        L.bind('<Button-1>', lambda e, row_guess=i, col_guess=j: self.on_miss(row_guess, col_guess, e))

    def on_hit(self, ship_list, row_guess, col_guess, event):
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

    def on_miss(self, row_guess, col_guess, event):
        color = "blue"
        event.widget.config(bg=color)
        board[row_guess - 1][col_guess - 1] = color
        print("\nMiss!!")


if __name__ == '__main__':
    args = inputs.initialize_parser()
    type_list = Utils.create_ship_type_list(args)
    board, ships = game_board.create_board(args, type_list)
    app = GuiApp(args, ships)
    app.mainloop()
