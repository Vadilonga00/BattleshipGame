import sys
import tkinter as tk
import tkinter.messagebox
import Utils
import game
import game_board
import inputs
import ship_types

FONT = ("Calibri", 10)


class GuiApp(tk.Tk):

    def __init__(self, args, ships):
        tk.Tk.__init__(self)
        tk.messagebox.showinfo('BATTLESHIPS GAME', 'Player 1 will start the game!! Click Ok to continue')

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Player1Page, Player2Page):
            frame = F(container, self, args, ships)
            self.frames[F] = frame
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
                L = tk.Label(self, text=text, bg='grey', font=FONT)
                L.grid(row=i, column=j)
                for ship in ships:
                    if ship_types.Ship.check_hit(ship, i, j):
                        L.bind('<Button-1>', lambda e, row_guess=i, col_guess=j: on_hit(args.option, ships, row_guess, col_guess, e, controller, 1))
                        break
                    else:
                        L.bind('<Button-1>', lambda e, row_guess=i, col_guess=j: on_miss(row_guess, col_guess, e, controller, 1))


class Player2Page(tk.Frame):

    def __init__(self, parent, controller, args, ships):
        tk.Frame.__init__(self, parent)
        for i in range(1, args.rows + 1):
            for j in range(1, args.columns + 1):
                text = f'({i} - {j})'
                L = tk.Label(self, text=text, bg='grey', font=FONT)
                L.grid(row=i, column=j)
                for ship in ships:
                    if ship_types.Ship.check_hit(ship, i, j):
                        L.bind('<Button-1>', lambda e, row_guess=i, col_guess=j: on_hit(args.option, ships, row_guess, col_guess, e, controller, 2))
                        break
                    else:
                        L.bind('<Button-1>', lambda e, row_guess=i, col_guess=j: on_miss(row_guess, col_guess, e, controller, 2))


def on_hit(option, ship_list, row_guess, col_guess, event, controller, player):
    color = "red"
    event.widget.config(bg=color)
    board[row_guess - 1][col_guess - 1] = color
    for i in ship_list:
        if ship_types.Ship.is_hit(i, row_guess, col_guess):
            if ship_types.Ship.is_sunk(i):
                if game.is_win(ship_list):
                    tk.messagebox.showinfo('YOU WIN!!', f'Player {player} wins the game! Click OK to terminate program')
                    sys.exit()
                else:
                    tk.messagebox.showinfo('HIT AND SUNK!!', f'You just sunk an enemy {i.__class__.__name__}!!')
                    if option == 1:
                        switch_frame(player, controller)

            else:
                tk.messagebox.showinfo('HIT!!', f'You just hit an enemy ship!!')
                if option == 1:
                    switch_frame(player, controller)


def on_miss(row_guess, col_guess, event, controller, player):
    color = "blue"
    event.widget.config(bg=color)
    board[row_guess - 1][col_guess - 1] = color
    switch_frame(player, controller)


def switch_frame(player, controller):
    if player == 1:
        controller.show_frame(Player2Page)
        tk.messagebox.showinfo('PLAYER 2 TURN', 'Pass the computer to Player 2')
    else:
        controller.show_frame(Player1Page)
        tk.messagebox.showinfo('PLAYER 1 TURN', 'Pass the computer to Player 1')


if __name__ == '__main__':
    args = inputs.initialize_parser()
    type_list = Utils.create_ship_type_list(args)
    board, ships = game_board.create_board(args, type_list)
    app = GuiApp(args, ships)
    app.mainloop()
