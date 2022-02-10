# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:05:52 2022

@author: carpy
"""


class Ship:
    def __init__(self, size, orientation, start_row, start_col):
        if size >= 1 and size <= 5:
            self.size = size
        else: raise ValueError("Value must be an integer between 1 and 5")

        if orientation == 'horizontal' or orientation == 'vertical':
            self.orientation = orientation
        else:
            raise ValueError("Value must be 'horizontal' or 'vertical'.")

            

def create_board(args):
    board = [[0] * args.columns for x in range(args.rows)]
    counter = 0
    ships_array = []
    while counter < args.ships:    
        start_row = int(input('Insert row:'))
        start_col = int(input('Insert column:'))
        orientation = input('Insert orientation:')
        size = int(input('Insert size:'))
        ship = Ship(size, orientation, start_row, start_col)
        if (start_row in range(args.rows+1) and start_col in range(args.columns+1)):
            if orientation == 'horizontal':
                horizontal_ship_restraints(args, board, start_row, start_col, orientation, size)
                counter += 1
            if orientation == 'vertical':
                vertical_ship_restraints(args, board, start_row, start_col, orientation, size)
                counter += 1
        else:
            raise ValueError('Error! Start point is out of board')
        ships_array.append(ship)
        print_board(board,args)
    print('Pass the computer to the next player')
    

def gameplay(args,ship_list):
    board = [[0] * args.columns for x in range(args.rows)]
    for turn in range(args.turns):
        print_board(board,args)
        print("Turn:", turn + 1, "of", args.turns)
        print("Ships left:", len(ship_list))

        row_guess = int(input("guess_row:\n"))
        if row_guess > args.rows:
            print(f'That is not in the boundaries of the ocean! Try a coordinate between 1 and {args.rows}')

        col_guess = int(input("guess_colum:\n"))
        if col_guess > args.columns:
            print(f'That is not in the boundaries of the ocean! Try a coordinate between 1 and {args.columns}')
        
def print_board(game_board,args):
  print("\n  " + " ".join(str(x) for x in range(1, args.columns + 1)))
  for r in range(args.rows):
    print(str(r + 1) + " " + " ".join(str(c) for c in game_board[r]))
  print()

def horizontal_ship_restraints(args, board, start_row, start_col, orientation, size):
    if start_col + size - 1 <= args.columns:
        for i in range(start_col - 1, start_col + size - 1):
            if board[start_row - 1][i] == 1:
                raise ValueError("Error! There is already another ship here")
            if start_row == 1:
                if board[start_row][i] == 1:
                    raise ValueError("Error! You are adjacent to another ship")
            if start_row == args.rows:
                if board[start_row-2][i] == 1:
                    raise ValueError("Error! You are adjacent to another ship")
            if start_row > 1 and start_row < args.rows:
                if board[start_row][i] == 1 or board[start_row - 2][i] == 1:
                    raise ValueError("Error! You are adjacent to another ship")
            if start_col != 1:
                if board[start_row - 1][start_col - 2] == 1:
                    raise ValueError("Error! You are adjacent to another ship")
            if start_col + size - 2 != args.columns - 1:
                if board[start_row - 1][start_col + size - 1] == 1:
                    raise ValueError("Error! You are adjacent to another ship")
            board[start_row - 1][i] = 1
    else:
        raise ValueError('Error! Ship is out of board')

def vertical_ship_restraints(args, board, start_row, start_col, orientation, size):
    if start_row + size - 1 <= args.rows:
        for i in range(start_row - 1, start_row + size - 1):
            if board[i][start_col - 1] == 1:
                raise ValueError("Error! There is already another ship here")
            if start_col == 1:
                if board[i][start_col] == 1:
                    raise ValueError("Error! You are adjacent to another ship")
            if start_row == args.rows:
                if board[i][start_col-2] == 1:
                    raise ValueError("Error! You are adjacent to another ship")
            if start_col > 1 and start_col < args.columns:
                if board[i][start_col] == 1 or board[i][start_col-2] == 1:
                    raise ValueError("Error! You are adjacent to another ship")
            if start_row != 1:
                if board[start_row - 2][start_col - 1] == 1:
                    raise ValueError("Error! You are adjacent to another ship")
            if start_row + size - 2 != args.rows - 1:
                if board[start_row + size - 1][start_col - 1] == 1:
                    raise ValueError("Error! You are adjacent to another ship")
            board[i][start_col - 1] = 1
    else:
        raise ValueError('Error! Ship is out of board')