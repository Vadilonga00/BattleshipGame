
# SHIP BATTLE
Program that implements the game of the sea battle in the user vs user version. Project for the programming exam at Università Campus Bio-Medico di Roma.


# Index

- [How to get started](#how-to-get-started)

# How to get started

## To execute
To execute the script you can:

-Insert the rows and columns fields that indicate the number of rows and columns the board has. If not indicated they are equal to 9
   
   
    Example of execution commands: python3 main.py -r 6 -c 6
    
    
    In this way you will play with a 6x6 board.
    
    
-Choose the number of each type of ship to play with. If not indicated it shall be equal to one for each type of ship


    Example of execution commands: python3 main.py -s1 1 -s2 2 -s3 3 -s4 4
    
    
    In this way you will play with 1 carrier 2 battleships 3 submarines 4 destroyers
    
    
-Choose the game variant you want to play: 0 if after hitting is my turn again, 1 otherwise. if not indicated you will play with the variant 0
    
    
    Example of execution commands: python3 main.py -o 1
    
    
    In this way after shooting the turn will be automatically passed to my opponent
    
    
-Choose if you want to play with graphical interface (1) or not (0). If not indicated you will play without
    
    
    Example of execution commands: python3 main.py -g 1
    
    
    In this way you will play with graphical interface
    
# Authors
Code written by:

Capurro Llado Massimo, Carpineti Francesco, Vadilonga Francesca

