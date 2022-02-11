# This file contains the logic and methods for the game execution
import game_board


# This method is a first implementation of a game turn
def gameplay(args, ship_list):
    board = [[0] * args.columns for x in range(args.rows)]
    for turn in range(args.turns):
        game_board.print_board(board, args)
        print("Turn:", turn + 1, "of", args.turns)
        print("Ships left:", len(ship_list))

        row_guess = int(input("guess_row:\n"))
        if row_guess > args.rows:
            print(f'That is not in the boundaries of the ocean! Try a coordinate between 1 and {args.rows}')

        col_guess = int(input("guess_colum:\n"))
        if col_guess > args.columns:
            print(f'That is not in the boundaries of the ocean! Try a coordinate between 1 and {args.columns}')
