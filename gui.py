import sys
import tkinter as tk
import tkinter.messagebox
import game
import ship_types
from sys import platform

FONT = ("Calibri", 10)

if platform == "darwin":
    ICON = "img/battleship.icns"
elif platform == "win32":
    ICON = "img/battleship.ico"

# Icon created by: https://www.flaticon.com/free-icons/warship


class GuiApp(tk.Tk):
    """
        This is the base application class. Uses Tkinter to execute a GUI for the game. Its role is to create, start,
        and run the 2 Frames (one for each player) needed for the GUI implementation of the game. All it's done in
        the __init__ method.
    """
    def __init__(self, args, ships1, ships2, board1, board2):

        # Initialize the Tkinter GUI
        tk.Tk.__init__(self)

        # Change icon and title
        tk.Tk.iconbitmap(self, ICON)  # Using the icon
        tk.Tk.title(self, "BATTLESHIP GAME!!")

        # This command will be run all over the frames. It allows the creation of different types of pop-ups
        tk.messagebox.showinfo('BATTLESHIPS GAME', 'Player 1 will start the game!! Click Ok to continue')

        # The container will contain all the frames, stacked on top of each other
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Create the desired frames and put them into the container
        self.frames = {}
        for F in (Player1Page, Player2Page):
            if F is Player1Page:
                frame = F(container, self, args, ships2, board2)
            else:
                frame = F(container, self, args, ships1, board1)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # As player 1 starts, show its frame
        self.show_frame(Player1Page)

    def show_frame(self, controller):
        """
        This method puts one frame on top of the others
        :param controller: The controller
        :return: None
        """
        frame = self.frames[controller]
        frame.tkraise()


class Player1Page(tk.Frame):
    """
        This class represents player1's Frame. As we are using Tkinter, inherit from the Tkinter Frame module.
    """
    def __init__(self, parent, controller, args, ships, board):
        # Initialize the frame
        tk.Frame.__init__(self, parent)

        # Create a grid of labels for every row and column of the board, set text to the label and bind a button
        # depending on which coordinates of the grid are occupied by a ship. If there is a ship, the bound button,
        # upon click, will trigger a method (on_hit), if not, another method will be triggered instead (on_miss)
        for i in range(1, args.rows + 1):
            for j in range(1, args.columns + 1):
                text = f'({i} - {j})'
                l = tk.Label(self, text=text, bg='grey', font=FONT)
                l.grid(row=i, column=j)
                for ship in ships:
                    if ship_types.Ship.check_hit(ship, i, j):
                        l.bind('<Button-1>', lambda e, row_guess=i, col_guess=j:
                               on_hit(board, args.option, ships, row_guess, col_guess, e, controller, 1))
                        break
                    else:
                        l.bind('<Button-1>', lambda e, row_guess=i, col_guess=j:
                               on_miss(board, row_guess, col_guess, e, controller, 1))


class Player2Page(tk.Frame):
    """
        This class represents player2's Frame. As we are using Tkinter, inherit from the Tkinter Frame module.
    """
    def __init__(self, parent, controller, args, ships, board):
        # Initialize the frame
        tk.Frame.__init__(self, parent)

        # TODO: try to create a method
        for i in range(1, args.rows + 1):
            for j in range(1, args.columns + 1):
                text = f'({i} - {j})'
                l = tk.Label(self, text=text, bg='grey', font=FONT)
                l.grid(row=i, column=j)
                for ship in ships:
                    if ship_types.Ship.check_hit(ship, i, j):
                        l.bind('<Button-1>',
                               lambda e, row_guess=i, col_guess=j: on_hit(board, args.option, ships, row_guess,
                                                                          col_guess, e, controller, 2))
                        break
                    else:
                        l.bind('<Button-1>',
                               lambda e, row_guess=i, col_guess=j: on_miss(board, row_guess, col_guess, e, controller,
                                                                           2))


def on_hit(board, option, ship_list, row_guess, col_guess, event, controller, player):
    """
    This method executes only when a button with a ship is clicked. It generates a pop-up of the situation and colors
    the coordinate (the label). If the option is to shoot again after a hit then player frame unchanged. Otherwise,
    after the pop-up generation, changes the player frame as the turn changed hands
    :param board: The player Board
    :param option: The option given by the user at the start of the program
    :param ship_list: The player Ship list
    :param row_guess: The row coordinate of the click
    :param col_guess: The column coordinate of the click
    :param event: The event that triggered the method (the click)
    :param controller: The controller, used to switch frame when needed
    :param player: The player shooting
    :return: None
    """
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


def on_miss(board, row_guess, col_guess, event, controller, player):
    """
    This method executes only when a button without a ship is clicked. It colors the coordinate (label) and generates
    a pop-up message that communicates to change turns. Finally, it changes the player frame
    :param board: The player Board
    :param row_guess: The row coordinate of the click
    :param col_guess: The column coordinate of the click
    :param event: The event that triggered the method (the click)
    :param controller: The controller, used to switch frame when needed
    :param player: The player shooting
    :return: None
    """
    color = "blue"
    event.widget.config(bg=color)
    board[row_guess - 1][col_guess - 1] = color
    tk.messagebox.showinfo('MISS!!', 'You hit water. Better luck next time')
    switch_frame(player, controller)


def switch_frame(player, controller):
    """
    Support method to ease readability. It generates the right pop-up for the player change and actually changes the
    frame
    :param player: The player who shot last
    :param controller: The controller
    :return: None
    """
    if player == 1:
        controller.show_frame(Player2Page)
        tk.messagebox.showinfo('PLAYER 2 TURN', 'Pass the computer to Player 2')
    else:
        controller.show_frame(Player1Page)
        tk.messagebox.showinfo('PLAYER 1 TURN', 'Pass the computer to Player 1')
