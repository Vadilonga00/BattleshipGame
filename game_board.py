import ship_types
import Utils


def create_board(args, type_list):
    """
        create the board of the game with each ship
        :param args: the inputs given by the user
        :param type_list: a list that contains the numbers of ships for each type
        :return: a game board and a list of each ship with its length,
        orientation, start row, start colum and coordinates
        """
    board = [[0] * args.columns for x in range(args.rows)]
    ship_list = []
    for i in type_list:
        Utils.user_message(i)
        successful_insertion = False

        while not successful_insertion:
            try:
                start_row = int(input(f'\nInsert row. An integer from 1 to {args.rows}: '))
                start_col = int(input(f'\nInsert column. An integer from 1 to {args.columns}: '))
            except ValueError:
                print(f'\u001b[31m\nInvalid row and/or column, please try again!\033[0m')
                continue
            if not Utils.check_start_point(args, start_row, start_col):
                print('\u001b[31m\nError! The given starting point is not valid. Try again\033[0m')
                continue

            orientation = input('\nInsert orientation. Must be horizontal or vertical: \033[0m')
            if not Utils.check_orientation(orientation):
                print(
                    '\u001b[31m\nError! The given orientation is not valid. Try again making sure you spell correctly your choice\033[0m')
                continue

            if orientation == 'horizontal':
                error, coordinates = check_horizontal_ship_positioning(args, board, start_row, start_col, i)
                if not error:
                    successful_insertion = True
            else:
                error, coordinates = check_vertical_ship_positioning(args, board, start_row, start_col, i)
                if not error:
                    successful_insertion = True
            print_board(board, args)

        if i == 5:
            ship = ship_types.Carrier(orientation, start_row, start_col, coordinates)
        elif i == 4:
            ship = ship_types.Battleship(orientation, start_row, start_col, coordinates)
        elif i == 3:
            ship = ship_types.Submarine(orientation, start_row, start_col, coordinates)
        elif i == 2:
            ship = ship_types.Destroyer(orientation, start_row, start_col, coordinates)
        ship_list.append(ship)
    return board, ship_list


def print_board(game_board, args):
    """
    print a game board with inputs parameters
   :param game_board: the game board
   :param args: the inputs given by the user
   :return: the graphics of the board in the current state
    """
    print("\n  " + " ".join(str(x) for x in range(1, args.columns + 1)))
    for r in range(args.rows):
        print(str(r + 1) + " " + " ".join(str(c) for c in game_board[r]))
    print()


def check_horizontal_ship_positioning(args, board, start_row, start_col, size):
    """
                check the horizontal position of the ship in the board
                and return a message of warning if the position in not valid
                :param args: The inputs given by the user
                :param board: the game board
                :param start_row: the start point of the row
                :param start_col: the start point of the colum
                :param size: the size of the ship
                :return: a logical parameter that is True is there is an error and false
                if not, and the coordinate of the ship (None if there is an error)
                """
    error = False
    if start_col + size - 1 <= args.columns: #Check that the ship is on the board
        i = start_col - 1
        while i < start_col + size - 1 and not error:
            if board[start_row - 1][i] == 1: #Check that i do not position over another ship
                print("\u001b[31m\n\nError! There is already another ship here\033[0m")
                error = True
                continue
            if start_row == 1:
                if board[start_row][i] == 1: #If i'm on the first row, check not to have an adjacent ship in the second row
                    print("\u001b[31m\n\nError! You are adjacent to another ship\033[0m")
                    error = True
                    continue
            if start_row == args.rows: #If I am on the last row, check not to have an adjacent ship in the penultimate row
                if board[start_row - 2][i] == 1:
                    print("\u001b[31m\n\nError! You are adjacent to another ship\033[0m")
                    error = True
                    continue
            if start_row > 1 and start_row < args.rows: #Check not to have an adjacent ship in the upper and lower row
                if board[start_row][i] == 1 or board[start_row - 2][i] == 1:
                    print("\u001b[31m\n\nError! You are adjacent to another ship\033[0m")
                    error = True
                    continue
            if start_col != 1:
                if board[start_row - 1][start_col - 2] == 1: #Check not to have an adjacent ship on the left
                    print("\u001b[31m\n\nError! You are adjacent to another ship\033[0m")
                    error = True
                    continue
            if start_col + size - 2 != args.columns - 1:
                if board[start_row - 1][start_col + size - 1] == 1: #Check not to have an adjacent ship on the right
                    print("\u001b[31m\n\nError! You are adjacent to another ship\033[0m")
                    error = True
                    continue
            i = i + 1
        if not error:
            coordinates = []
            for i in range(start_col - 1, start_col + size - 1):
                board[start_row - 1][i] = 1
                coordinates.append([start_row, i + 1])
            return error, coordinates
    else:
        error = True
        print("\u001b[31m\n\nError! Ship is out of board\033[0m")
    return error, None


def check_vertical_ship_positioning(args, board, start_row, start_col, size):
    """
            check the vertical position of the ship in the board
            and return a message of warning if the position in not valid
            :param args: The inputs given by the user, needed for the number of rows and columns of the board
            :param board: the game board
            :param start_row: the start point of the row
            :param start_col: the start point of the colum
            :param size: the size of the ship
            :return: a logical parameter that is True is there is an error and false
            if not, and the coordinate of the ship (None if there is an error)
            """
    error = False
    if start_row + size - 1 <= args.rows: #Check that the ship is on the board
        i = start_row - 1
        while i < start_row + size - 1 and not error:
            if board[i][start_col - 1] == 1: #Check that i do not position over another ship
                print("\u001b[31m\n\nError! There is already another ship here\033[0m")
                error = True
                continue
            if start_col == 1:
                if board[i][start_col] == 1: #If i'm on the first column, check not to have an adjacent ship in the second column
                    print("\u001b[31m\n\nError! You are adjacent to another ship\033[0m")
                    error = True
                    continue
            if start_col == args.columns:
                if board[i][start_col - 2] == 1: #If I am on the last column, check not to have an adjacent ship in the penultimate column
                    print("\u001b[31m\n\nError! You are adjacent to another ship\033[0m")
                    error = True
                    continue
            if start_col > 1 and start_col < args.columns: #Check not to have an adjacent ship in the left and right column
                if board[i][start_col] == 1 or board[i][start_col - 2] == 1:
                    print("\u001b[31m\n\nError! You are adjacent to another ship\033[0m")
                    error = True
                    continue
            if start_row != 1:
                if board[start_row - 2][start_col - 1] == 1: #Check not to have an adjacent ship above
                    print("\u001b[31m\n\nError! You are adjacent to another ship\033[0m")
                    error = True
                    continue
            if start_row + size - 2 != args.rows - 1:
                if board[start_row + size - 1][start_col - 1] == 1: #Check not to have an adjacent ship below
                    print("\u001b[31m\n\nError! You are adjacent to another ship\033[0m")
                    error = True
                    continue
            i = i + 1
        if not error:
            coordinates = []
            for i in range(start_row - 1, start_row + size - 1):
                board[i][start_col - 1] = 1
                coordinates.append([i + 1, start_col])
            return error, coordinates
    else:
        print("\u001b[31m\n\nError! Ship is out of board\033[0m")
        error = True
    return error, None
