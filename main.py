import inputs

args = inputs.initialize_parser()

# Variables
row_size = args.rows
col_size = args.columns
max_turns = args.turns

# Initialize the board
ship_list = []
board = [[0] * col_size for x in range(row_size)]


# board_display = [["O"] * col_size for x in range(row_size)] # for strings case


def print_board(board_array):
    print("\n  " + " ".join(str(x) for x in range(1, col_size + 1)))
    for r in range(row_size):
        print(str(r + 1) + " " + " ".join(str(c) for c in board_array[r]))
    print()


for turn in range(max_turns):
    print_board(board)
    print("Turn:", turn + 1, "of", max_turns)
    print("Ships left:", len(ship_list))

    row_guess = int(input("guess_row:\n"))
    if row_guess > row_size:
        print(f'That is not in the boundaries of the ocean! Try a coordinate between 1 and {row_size}')

    col_guess = int(input("guess_colum:\n"))
    if col_guess > col_size:
        print(f'That is not in the boundaries of the ocean! Try a coordinate between 1 and {col_size}')
