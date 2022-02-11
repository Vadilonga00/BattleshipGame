import warnings
import ship_types


def check_orientation(orientation):
    if orientation == 'horizontal' or orientation == 'vertical':
        return True
    else:
        return False


def check_start_point(args, start_row, start_col):
    if start_row <= args.rows and start_col <= args.columns:
        return True
    else:
        return False


def create_ship_type_list(args):
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


def create_board(args, type_list):
    board = [[0] * args.columns for x in range(args.rows)]
    ship_list = []
    for i in type_list:
        successful_insertion = False

        while not successful_insertion:
            start_row = int(input(f'\nInsert row. Integer from 1 to {args.rows}: '))
            start_col = int(input(f'\nInsert column. Integer from 1 to {args.columns}: '))
            if not check_start_point(args, start_row, start_col):
                print('\nError! The given starting point is not valid. Try again')
                continue

            orientation = input('\nInsert orientation. Must be horizontal or vertical: ')
            if not check_orientation(orientation):
                print(
                    '\nError! The given orientation is not valid. Try again making sure you spell correctly your choice')
                continue

            if orientation == 'horizontal':
                error = check_horizontal_ship_positioning(args, board, start_row, start_col, i)
                if not error:
                    successful_insertion = True
            else:
                error = check_vertical_ship_positioning(args, board, start_row, start_col, i)
                if not error:
                    successful_insertion = True
            print_board(board, args)
        #Todo: successfully added ships must be added to the list of ships
        # if i == 5:
        #     ship = ship_types.Carrier(orientation, start_row, start_col)
        # elif i == 4:
        #     ship = ship_types.Battleship(orientation, start_row, start_col)
        # elif i == 3:
        #     ship = ship_types.Submarine(orientation, start_row, start_col)
        # elif i == 2:
        #     ship = ship_types.Destroyer(orientation, start_row, start_col)
        # ship_list.append(ship)


def gameplay(args, ship_list):
    board = [[0] * args.columns for x in range(args.rows)]
    for turn in range(args.turns):
        print_board(board, args)
        print("Turn:", turn + 1, "of", args.turns)
        print("Ships left:", len(ship_list))

        row_guess = int(input("guess_row:\n"))
        if row_guess > args.rows:
            print(f'That is not in the boundaries of the ocean! Try a coordinate between 1 and {args.rows}')

        col_guess = int(input("guess_colum:\n"))
        if col_guess > args.columns:
            print(f'That is not in the boundaries of the ocean! Try a coordinate between 1 and {args.columns}')


def print_board(game_board, args):
    print("\n  " + " ".join(str(x) for x in range(1, args.columns + 1)))
    for r in range(args.rows):
        print(str(r + 1) + " " + " ".join(str(c) for c in game_board[r]))
    print()


def check_horizontal_ship_positioning(args, board, start_row, start_col, size):
    error = True
    if start_col + size - 1 <= args.columns:
        for i in range(start_col - 1, start_col + size - 1):
            if board[start_row - 1][i] == 1:
                warnings.warn("Error! There is already another ship here")
            if start_row == 1:
                if board[start_row][i] == 1:
                    warnings.warn("Error! You are adjacent to another ship")
            if start_row == args.rows:
                if board[start_row - 2][i] == 1:
                    warnings.warn("Error! You are adjacent to another ship")
            if start_row > 1 and start_row < args.rows:
                if board[start_row][i] == 1 or board[start_row - 2][i] == 1:
                    warnings.warn("Error! You are adjacent to another ship")
            if start_col != 1:
                if board[start_row - 1][start_col - 2] == 1:
                    warnings.warn("Error! You are adjacent to another ship")
            if start_col + size - 2 != args.columns - 1:
                if board[start_row - 1][start_col + size - 1] == 1:
                    warnings.warn("Error! You are adjacent to another ship")
            board[start_row - 1][i] = 1
        error = False
    else:
        warnings.warn('Error! Ship is out of board')
    return error

#Todo: fix bugs in check
def check_vertical_ship_positioning(args, board, start_row, start_col, size):
    error = True
    if start_row + size - 1 <= args.rows:
        for i in range(start_row - 1, start_row + size - 1):
            if board[i][start_col - 1] == 1:
                warnings.warn("Error! There is already another ship here")
            if start_col == 1:
                if board[i][start_col] == 1:
                    warnings.warn("Error! You are adjacent to another ship")
            if start_row == args.rows:
                if board[i][start_col - 2] == 1:
                    warnings.warn("Error! You are adjacent to another ship")
            if start_col > 1 and start_col < args.columns:
                if board[i][start_col] == 1 or board[i][start_col - 2] == 1:
                    warnings.warn("Error! You are adjacent to another ship")
            if start_row != 1:
                if board[start_row - 2][start_col - 1] == 1:
                    warnings.warn("Error! You are adjacent to another ship")
            if start_row + size - 2 != args.rows - 1:
                if board[start_row + size - 1][start_col - 1] == 1:
                    warnings.warn("Error! You are adjacent to another ship")
            board[i][start_col - 1] = 1
        error = False
    else:
        warnings.warn('Error! Ship is out of board')
    return error
