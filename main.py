#variables
row_size = 10  # number of rows
col_size = 10 # number of columns
max_turns=60
#initialize a board
ship_list = []
board = [[0] * col_size for x in range(row_size)]
#board_display = [["O"] * col_size for x in range(row_size)] in case of string

def print_board(board_array):
  print("\n  " + " ".join(str(x) for x in range(1, col_size + 1)))
  for r in range(row_size):
    print(str(r + 1) + " " + " ".join(str(c) for c in board_array[r]))
  print()



for turn in range(max_turns):
  print_board(board)
  print("Turn:", turn + 1, "of", max_turns)
  print("Ships left:", len(ship_list))
  print()

  input("guess_row:\n")

  input("guess_colum:\n")

