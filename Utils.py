# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 23:05:52 2022

@author: carpy
"""
import inputs


class Ship:
    def __init__(self, size, orientation, start_row, start_col):
        if size <= 5 and size >= 1:
            self.size = size
        else: raise ValueError("Value must be an integer between 1 and 5")

        if orientation == 'horizontal' or orientation == 'vertical':
            self.orientation = orientation
        else:
            raise ValueError("Value must be 'horizontal' or 'vertical'.")
            

def create_board(args):
    board = [[0] * args.columns for x in range(args.rows)]
    counter = 0
    ships_array=[]
    while counter < args.ships:    
        start_row = int(input('Insert row:'))
        start_col = int(input('Insert column:'))
        orientation = input('Insert orientation:')
        size = int(input('Insert size:'))
        ship = Ship(size, orientation,start_row,start_col)
        ships_array.append(ship)
        counter += 1
    print('passa computer al giocatore successivo e premi invio')
    

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
        
def print_board(board,args):
  print("\n  " + " ".join(str(x) for x in range(1, args.columns + 1)))
  for r in range(args.rows):
    print(str(r + 1) + " " + " ".join(str(c) for c in board[r]))
  print()
