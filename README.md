
# SHIP BATTLE
Program that implements the game of the sea battle in the user vs user version. Project for the programming exam at Università Campus Bio-Medico di Roma.


# Index

- [How to get started](#how-to-get-started)

# How to get started

## Game guide

The program allows two players to play the "naval battle" according to the usual rules.

To configure your own playing field, which consists of a matrix within the which to place a predetermined number of ships of different lengths, the following rules apply:
- the length of the ship corresponds to a number integer of squares of the matrix
- each ship can be arranged horizontally or vertically, entirely within the playing board
- two ships cannot be adjacent, it must always be there at least one square away from one ship to any other.
 
 The game has two modes of alternation of the turn of game between players:
- systematic alternation (one shot each)
- in the event of a hit, the player is entitled to another hit.

The size of the playing field, the number of vessels of each type and the mode of alternation are parameters by which the application must be initially configured and are the same for both players (refer to ##To execute).

Each player, according to the alternation of game turns, will be asked to communicate the coordinates of his shot and the application will provide the result: missed / hit / sunk, until the end of the game and the proclamation of the winner when all of a player's ships are been sunk.

## To execute
To execute the script you can:

-Insert the rows(-r) and columns(-c) fields that indicate the number of rows and columns the board has. If not indicated they are equal to 9
   
   
    Example of execution commands: python3 main.py -r 6 -c 6
    
    
    In this way you will play with a 6x6 board.
    
    
-Choose the number of each type of ship to play with. If not indicated it shall be equal to one for each type of ship


    Example of execution commands: python3 main.py -s1 1 -s2 2 -s3 3 -s4 4
    
    
    In this way you will play with 1 carrier(-s1) 2 battleships(-s2) 3 submarines(-s3) 4 destroyers(-s4)
    
    
-Choose the game variant you want to play: 0 if after hitting is my turn again, 1 otherwise. if not indicated you will play with the variant 0
    
    
    Example of execution commands: python3 main.py -o 1
    
    
    In this way after shooting the turn will be automatically passed to my opponent
    
    
-Choose if you want to play with graphical interface (1) or not (0). If not indicated you will play without
    
    
    Example of execution commands: python3 main.py -g 1
    
    
    In this way you will play with graphical interface
    
# Authors
Code written by:

Capurro Llado Massimo, Carpineti Francesco, Vadilonga Francesca

