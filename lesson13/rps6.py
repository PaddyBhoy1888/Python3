# Rock, Paper, Scissors Update 1.1.24 lesson 13 with f-strings

# Rock, Paper, Scissors
#
# value = input('Please enter a value:\n')
# print(value)

import random  # random is a import module that randomises the computers choice
import sys  # sys is a import modeule that allows for a system control, in this case to exit the commands
from enum import Enum

# New Lesson11 31.12.23. Change global variable to nested local inside function below


def rps():
    game_count = 0  # Local scope variable
    player_wins = 0  # New variable to count how many times the player wins
    python_wins = 0  # New variable to count how many times the python wins

    # New addition 29.12.23

    def play_rps():  # Here we have defined the function play_rps
        # New addition 31.12.23 nonlocal variables for player & python game count
        nonlocal player_wins
        nonlocal python_wins

        # Indent all code to be inside the function
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

    # New addition 29.12.23 is to remove the while loop and playagain variable.

        playerchoice = input(
            "Enter...\n1 for Rock, \n2 for Paper, or\n3 for Scissors:\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print("You must enter 1, 2, or 3.")
            return play_rps()
        # Create a player choice function where an input is required.
        # A String is provided with the input to allow the user to determine 1 for Rock, 2 for Paper & 3 for Scissors

        player = int(playerchoice)
        # As the above input would be a string we use the cast playerchoice from a string to an integer so that the code below can read if the players choice is between 1 - 3

        computerchoice = random.choice("123")
        # Computer to choose a random choice between one of the characters in the string.

        computer = int(computerchoice)
        # Here we change the computers choice from one of the random string values to an integer.

# New modification with f-string lesson 13 1.1.24

        print(f"You Chose {str(RPS(player)).replace('RPS.', '').title()}.")
        #  Concatinate the players choice
        print(
            f"Python Chose {str(RPS(computer)).replace('RPS.', '').title()}.\n")
        # Concatinate the computer choice. Concatination. Adding two strings together to form a larger string

        # New lesson11 29.12.23 - create the player, computer choice into a nested function
        def decide_winner(player, computer):
            # New addition lesson12 31.12.23 - nonlocal values for player & python wins added.
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1  # New addition lesson12 31.12.23 - count the player wins in increments of 1
                return "🐱‍🏍You Win!"
            elif player == 2 and computer == 1:
                player_wins += 1  # New addition lesson12 31.12.23 - count the player wins in increments of 1
                return "🐱‍🏍You Win!"
            elif player == 3 and computer == 2:
                player_wins += 1  # New addition lesson12 31.12.23 - count the player wins in increments of 1
                return "🐱‍🏍You Win!"
            elif player == computer:
                return "😒Tie Game!"
            else:
                python_wins += 1  # New addition lesson12 31.12.23 - count the python wins in increments of 1
                return "🤦‍♀️Python Wins"

        # A new variable to call the nested function 'decide_winner' refering to the parameters above inside the function.
        game_result = decide_winner(player, computer)

        print(game_result)

    # New lesson11 29.12.23 - Creating a way for the code to keep count of how many times it has been played.
    # Updated lesson12 31.12.23 - Removal of global to nonlocal
        nonlocal game_count  # Refering to the nonlocal variable
        game_count += 1  # Adding 1 everytime the game is played
        # Print out a statment that counts by converting the game_count to a string
        # Lesson13 1.1.24 - f-strings
        print(f"\n Game count: {str(game_count)}")
        # Addition lesson12 31.12.23 - print out the winning count.
        print(f"\n player_wins: {str(player_wins)}")
        # Addition lesson12 31.12.23 - print out the winning count.
        print(f"\n python_wins: {str(python_wins)}")

        print("\nPlay again?")

        while True:
            # New addition 27.12.23
            playagain = input("\n Y for yes or \n Q to Quit \n")
        # Provide the player a method to input if they wish to continue to play.
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":  # Create a if statement so if the player uses lower case choice the game still understands the input
            return play_rps()  # if the player choses y then game will continue
        else:  # else statement to begin the stop process
            print("\n🥳🎉\n")
            print("Thank you for playing!\n")
            # This will exit the game and return to the terminal config
            sys.exit("Bye! 👋")

    # New addition lesson12 31.12.23 - This needs to be added to return the function
    return play_rps


play = rps()  # This new variable 'play' is created to call for the function

# This line will call the 'play' variable which now cotains the function 'rps' to start the game code.
play()
