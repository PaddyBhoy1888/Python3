# This is a challange project where we create a new game of guess the number.

# GAME REQUIERMENTS

# The game should be able to be launched on the terminal and accept the name argument
# The computer will randomly select 1, 2 or 3
# The computer will promt the player "Player, guess which number I'm thinking of... 1, 2, or 3."

# The player will guess between the numbers 1, 2 or 3.
# The player will only be able to input the three choices ONLY, error return if not chosen.

# The output should show results of both computer & player choices, who wins, count the games played, winning percentage, play again Y or Q, thanks for playing,  game should be personalised.
#


import random
# random is a import module that randomises the computers choice
import sys
# sys is a import module that allows for a system control, in this case to exit the commands
from enum import Enum
# enumerations are created either by using class syntax, or by using function-call syntax.


# Here we define the function gn with an input arguments name='playerOne'

def gn(name='playerOne'):
    game_count = 0  # Local scope variable to count games played
    player_wins = 0  # variable to count how many times the player wins
    python_wins = 0  # New variable to count how many times the python wins

    def play_gn():  # Here we have defined the function play_gn
        # We refer this function to the nonlocal variables listed below which are defined in the function gn local scope above.
        nonlocal player_wins
        nonlocal python_wins
        nonlocal name

        # We create a playerchoice variable which requiers the player to input a value. We also provide the statement where the computer defines the choices to be guessed that are between 1, 2 or 3.
        playerchoice = input(
            f"\n{name}, guess which number I'm thinking of... 1, 2, or 3.\n\n"
        )

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_rps()
        # Create a player choice function where an input is required.
        # A String is provided with the input to allow the user to determine 1 for Rock, 2 for Paper & 3 for Scissors
