# main.py
# call the functions from other .py files

# required modules and files
import os
from Context import *
from Menu import *

# starting game status
game_status = "PLAY"

# clear the terminal
os.system('cls||clear')

# main game loop
while game_status != "EXIT":
    context("START_ROOM")
    menu("START_ROOM")
    game_status = "EXIT"

# press anykey
input()

# end of code
