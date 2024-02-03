# Rock, Paper, Scissors Update 1.1.24 lesson 15 with modules & comand line arguments

# Rock, Paper, Scissors
#
# value = input('Please enter a value:\n')
# print(value)

import random  # random is a import module that randomises the computers choice
import sys  # sys is a import modeule that allows for a system control, in this case to exit the commands
from enum import Enum

# New Lesson11 31.12.23. Change global variable to nested local inside function below

# New lesson15 1.1.24 - define the name='playerOne'


def rps(name='playerOne'):
    game_count = 0  # Local scope variable
    player_wins = 0  # New variable to count how many times the player wins
    python_wins = 0  # New variable to count how many times the python wins

    # New addition 29.12.23

    def play_rps():  # Here we have defined the function play_rps
        # New addition 31.12.23 nonlocal variables for player & python game count
        # New addition lesson15 1.1.24 - nonlocal name
        nonlocal player_wins
        nonlocal python_wins
        nonlocal name

        # Indent all code to be inside the function
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

    # New addition 29.12.23 is to remove the while loop and playagain variable.

        playerchoice = input(
            f"\n{name}, please enter...\n1 for Rock, \n2 for Paper, or\n3 for Scissors:\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
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
# New modification with f-string lesson 15 1.1.24 - name args

        print(f"{name}, you Chose {str(RPS(player)).replace('RPS.', '').title()}.")
        #  Concatinate the players choice
        print(
            f"Python Chose {str(RPS(computer)).replace('RPS.', '').title()}.\n")
        # Concatinate the computer choice. Concatination. Adding two strings together to form a larger string

        # New lesson11 29.12.23 - create the player, computer choice into a nested function
        def decide_winner(player, computer):
            # New addition lesson12 31.12.23 - nonlocal values for player & python wins added.
            # New addition lesson15 1.1.24 - nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            nonlocal name

            if player == 1 and computer == 3:
                player_wins += 1  # New addition lesson12 31.12.23 - count the player wins in increments of 1
                return f"🐱‍🏍{name}, you Win!"
            elif player == 2 and computer == 1:
                player_wins += 1  # New addition lesson12 31.12.23 - count the player wins in increments of 1
                return f"🐱‍🏍{name}, you Win!"
            elif player == 3 and computer == 2:
                player_wins += 1  # New addition lesson12 31.12.23 - count the player wins in increments of 1
                return f"🐱‍🏍{name}, you Win!"
            elif player == computer:
                return "😒Tie Game!"
            else:
                python_wins += 1  # New addition lesson12 31.12.23 - count the python wins in increments of 1
                return f"🤦‍♀️Python Wins!\nSorry, {name}.."

        # A new variable to call the nested function 'decide_winner' refering to the parameters above inside the function.
        game_result = decide_winner(player, computer)

        print(game_result)

    # New lesson11 29.12.23 - Creating a way for the code to keep count of how many times it has been played.
    # Updated lesson12 31.12.23 - Removal of global to nonlocal
        nonlocal game_count  # Refering to the nonlocal variable
        game_count += 1  # Adding 1 everytime the game is played
        # Print out a statment that counts by converting the game_count to a string
        # Lesson13 1.1.24 - f-strings
        print(f"\n Game count: {game_count}")
        # Addition lesson12 31.12.23 - print out the winning count.
        print(f"\n {name}'s wins: {player_wins}")
        # Addition lesson12 31.12.23 - print out the winning count.
        print(f"\n python_wins: {python_wins}")

        print(f"\nPlay again, {name}?")

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
            if __name__ == "__main__":
                sys.exit(f"Bye {name}! 👋")
            else:
                return

    # New addition lesson12 31.12.23 - This needs to be added to return the function
    return play_rps


# New addition lesson15 1.1.24 - modules & args

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalised game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()
