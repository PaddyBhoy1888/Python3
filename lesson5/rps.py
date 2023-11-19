# Rock, Paper, Scissors
#
# value = input('Please enter a value:\n')
# print(value)

import random  # random is a import module that randomises the computers choice
import sys  # sys is a import modeule that allows for a system control, in this case to exit the commands
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print("")
# Printing a blank string will allow for a new line between new games
playerchoice = input(
    "Enter...\n1 for Rock, \n2 for Paper, or\n3 for Scissors:\n\n")
# Create a player choice function where an input is required.
# A String is provided with the input to allow the user to determine 1 for Rock, 2 for Paper & 3 for Scissors

player = int(playerchoice)
# As the above input would be a string we use the cast playerchoice from a string to an integer so that the code below can read if the players choice is between 1 - 3

if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3.")
# Here using an if statement we can can confin the users choice to only allow for inputs 1 to 3 so that if the user inputs a higher number we promt them to choose again. Using the sys.exit import we can exit the game back to the start rather than continuing with unwanted inputs.


computerchoice = random.choice("123")
# Computer to choose a random choice between one of the characters in the string.

computer = int(computerchoice)
# Here we change the computers choice from one of the random string values to an integer.

print("")
# Print blank line for space

print("You Chose " + str(RPS(player)).replace('RPS.', '') + ".")
#  Concatinate the players choice
print("Python Chose " + str(RPS(computer)).replace('RPS.', '') + ".")
# Concatinate the computer choice. Concatination. Adding two strings together to form a larger string
print("")

if player == 1 and computer == 3:
    print("🐱‍🏍You Win!")
elif player == 2 and computer == 1:
    print("🐱‍🏍You Win!")
elif player == 3 and computer == 2:
    print("🐱‍🏍You Win!")
elif player == computer:
    print("😒Tie Game!")
else:
    print("🤦‍♀️Python Wins")

#
