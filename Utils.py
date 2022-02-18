# This file contains a collection of utilities methods for the other files and classes


def check_orientation(orientation):
    """
         check if the orientation of the ship in the board is valid
         :return: a logical parameter that is true if the orientation
         is valid and false if not
         """
    if orientation == 'horizontal' or orientation == 'vertical':
        return True
    else:
        return False


def check_start_point(args, start_row, start_col):
    """
     check the starting point of the ship is valid
     :param start_row: the start point of the row
     :param start_col: the start point of the colum
     :return: a logical parameter that is true if the start row and start colum are
            included in the range
     """
    if start_row <= args.rows and start_col <= args.columns:
        return True
    else:
        return False


def create_ship_type_list(args):
    """
         create a list of ships types checking the inputs parameters
         :param args: the inputs given by the user
         :return: a list that contains an element for each ship based on his size
         """
    type_list = []
    counter = 0
    while counter < args.carriers:
        new = 5
        type_list.append(new)
        counter += 1
    while counter < args.carriers + args.battleships:
        new = 4
        type_list.append(new)
        counter += 1
    while counter < args.carriers + args.battleships + args.submarines:
        new = 3
        type_list.append(new)
        counter += 1
    while counter < args.carriers + args.battleships + args.submarines + args.destroyers:
        new = 2
        type_list.append(new)
        counter += 1
    return type_list


def choose_and_check_strike_point(args, play_board):
    """
    asks for a point to hit and checks the validity of the coordinates entered
    :param args: The inputs given by the user
    :param play_board:the game board
    :return: hit row and column
    """
    while True:
        try:
            row_guess = int(input("guess_row:\n"))
            col_guess = int(input("guess_column:\n"))
            if not(check_start_point(args, row_guess, col_guess)):
                print("The point is not inside the board, try again!")
            if not(play_board[row_guess-1][col_guess-1] == '-'):
                print("You’ve already hit this point, try again!")
            else:
                break
        except:
            print("Invalid input, please try again!")
    return row_guess, col_guess
