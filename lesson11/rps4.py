# Rock, Paper, Scissors Update 29.12.23 lesson 11 with global & local scope

# Rock, Paper, Scissors
#
# value = input('Please enter a value:\n')
# print(value)

import random  # random is a import module that randomises the computers choice
import sys  # sys is a import modeule that allows for a system control, in this case to exit the commands
from enum import Enum

# New Lesson11 29.12.23

game_count = 0  # Global scope variable


# New addition 29.12.23

def play_rps():  # Here we have defined the function play_rps
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

    print("You Chose " + str(RPS(player)).replace('RPS.', '').title() + ".")
    #  Concatinate the players choice
    print("Python Chose " + str(RPS(computer)).replace('RPS.', '').title() + ".")
    # Concatinate the computer choice. Concatination. Adding two strings together to form a larger string

    # New lesson11 29.12.23 - create the player, computer choice into a nested function
    def decide_winner(player, computer):
        if player == 1 and computer == 3:
            return "🐱‍🏍You Win!"
        elif player == 2 and computer == 1:
            return "🐱‍🏍You Win!"
        elif player == 3 and computer == 2:
            return "🐱‍🏍You Win!"
        elif player == computer:
            return "😒Tie Game!"
        else:
            return "🤦‍♀️Python Wins"

    # A new variable to call the nested function 'decide_winner' refering to the parameters above inside the function.
    game_result = decide_winner(player, computer)

    print(game_result)

# New lesson11 29.12.23 - Creating a way for the code to keep count of how many times it has been played.
    global game_count  # Refering to the global variable
    game_count += 1  # Adding 1 everytime the game is played
    # Print out a statment that counts by converting the game_count to a string
    print("\n Game count: " + str(game_count))

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


play_rps()  # Thisline is the call for the function
