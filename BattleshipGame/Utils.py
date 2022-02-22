def check_orientation(orientation):
    """
    Check if the orientation of the ship in the board is valid
    :param: orientation: The input orientation given by the user
    :return: a logical parameter that is true if the orientation
         is valid and false if not
    """
    if orientation == 'horizontal' or orientation == 'vertical':
        return True
    else:
        return False


def check_start_point(rows, cols, start_row, start_col):
    """
     Check the starting point of the ship is valid
     :param rows: The input given by the user for the number of rows of the board
     :param cols: The input given by the user for the number of columns of the board
     :param start_row: the start point of the row
     :param start_col: the start point of the colum
     :return: a logical parameter that is true if the start row and start colum are
            included in the range
     """
    if start_row <= rows and start_col <= cols:
        return True
    else:
        return False


def create_ship_type_list(carriers, battleships, submarines, destroyers):
    """
    Create a list of ships types checking the inputs parameters
    :param carriers: The input given by the user for the number of carriers
    :param battleships: The input given by the user for the number of battleships
    :param submarines: The input given by the user for the number of submarines
    :param destroyers: The input given by the user for the number of destroyers
    :return: a list that contains an element for each ship based on his size
    """
    type_list = []
    counter = 0
    while counter < carriers:
        new = 5
        type_list.append(new)
        counter += 1
    while counter < carriers + battleships:
        new = 4
        type_list.append(new)
        counter += 1
    while counter < carriers + battleships + submarines:
        new = 3
        type_list.append(new)
        counter += 1
    while counter < carriers + battleships + submarines + destroyers:
        new = 2
        type_list.append(new)
        counter += 1
    return type_list


def choose_and_check_strike_point(rows, cols, play_board):
    """
    Asks for a point to hit and checks the validity of the coordinates entered
    :param rows: The input given by the user for the number of rows of the board
    :param cols: The input given by the user for the number of columns of the board
    :param play_board:the game board
    :return: hit row and column
    """
    error = True
    while error:
        try:
            row_guess = int(input("guess_row:\n"))
            col_guess = int(input("guess_column:\n"))
            if not (check_start_point(rows, cols, row_guess, col_guess)):
                print("\u001b[31mThe point is not inside the board, try again!\033[0m")
            elif not (play_board[row_guess - 1][col_guess - 1] == '-'):
                print("\u001b[31mYou’ve already hit this point, try again!\033[0m")
            else:
                error = False
        except ValueError:
            print("\u001b[31mInvalid input, please try again!\033[0m")
    return row_guess, col_guess


def user_message(i):
    """
    This method is used to print a message during ship positioning
    :param i: An integer that represents the size of the ship to be positioned
    :return: None
    """
    if i == 5:
        print(f'\nGive me the coordinates and orientation of the carrier that is 5 squares long!')
    elif i == 4:
        print(f'\nGive me the coordinates and orientation of the battleship that is 4 squares long!')
    elif i == 3:
        print(f'\nGive me the coordinates and orientation of the submarine that is 3 squares long!')
    elif i == 2:
        print(f'\nGive me the coordinates and orientation of the destroyer that is 2 squares long!')
