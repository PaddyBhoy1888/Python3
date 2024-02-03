# A new arcade 3

# GAME REQUIERMENTS

# To play type the following into the terminal: -
# py arcade.py -n ["INSERT NAME"] *Make sure in the corect directory

# The game should be able to be launched on the terminal and accept the name argument

# The computer should welcome the player ( "NAME", welcome to the Arcade! )
# The computer should prompt the player with: -
# ( Please choose a game: 1 = RPS, 2 = Guess My Number or press "X" to exit the Arcade)

# The computer should launch the RPS game if the player chooses 1
# If the game is quit the computer should promt the player with: -
# (Welcome back to the arcade menu) & should repeat the choose game options

# The computer should launch the guess my number if the player chooses 2
# If the game is quit the computer should promt the player with: -
# (Welcome back to the arcade menu) & should repeat the choose game options

# If the player enters a number out with the 1, 2 or X then they should be promted with the correct values:-
# ("NAME", Please enter 1, 2 or X)

# When the player chooses X the computer should prompt: -
# ( See you next time!, Bye "NAME")

import sys
# sys is a import module that allows for a system control, in this case to exit the commands
from rps import rps
# From the rps file we will import the game rps
from guess_number import guess_number
# From the guess_number file we will import the the game guess_number

# Defin function 'play_game', which as default will set the name to = PlayerOne


def play_game(name='PlayerOne'):
    welcome_back = False
    # The welcome_back is set to equal False so that we can set values to a True.

    # A while loop that will provide the player with a welcome back message with their defined name
    while True:
        if welcome_back == True:
            print(f"\n{name}, welcome back to the Arcade menu.")

    playerchoice = input(
        "\nPlease choose a game:\n1 = Rock Paper Scissors\n2 = Guess My Number\n\nOr press \"X\" to exit the Arcade\n\n")

    if playerchoice not in ["1", "2", "x"]:
        print(f"\n{name}, please enter 1, 2, or x.")
        return play_game(name)

    welcome_back = True
