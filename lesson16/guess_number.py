# This is a challange project where we create a new game of guess the number.

# GAME REQUIERMENTS

# The game should be able to be launched on the terminal and accept the name argument
# The computer will randomly select 1, 2 or 3
# The computer will promt the player "Player, guess which number I'm thinking of... 1, 2, or 3."

# The player will guess between the numbers 1, 2 or 3.
# The player will only be able to input the three choices ONLY, error return if not chosen.

# The output should show results of both computer & player choices, who wins, count the games played, winning percentage, play again Y or Q, thanks for playing,  game should be personalised.
# To play type the following into the terminal: -
# py guess_number.py -n [INSERT NAME] *Make sure in the corect directory


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
            return play_gn()

        player = int(playerchoice)
        # As the above input would be a string we use the cast playerchoice from a string to an integer so that the code below can read if the players choice is between 1 - 3

        computerchoice = random.choice("123")
        # Computer to choose a random choice between one of the characters in the string.

        computer = int(computerchoice)
        # Here we change the computers choice from one of the random string values to an integer.

        print(f"\n{name}, you chose {playerchoice}.")
        # Print statement to display the players choice
        print(f"\nI was thinking of the number {computerchoice}.\n")
        # Print statement to display the computers choice.

        # define function 'decide_winner' with input parameters 'player' & 'computer'
        def decide_winner(player, computer):
            # We refer this function to the nonlocal variables listed below which are defined in the function gn local scope above.
            nonlocal player_wins
            nonlocal python_wins
            nonlocal name

            # Using an if & else statement we can state that if the player guesses the same as the computer then the player wins. Else any other outcome the computer wins.
            if player == computer:
                player_wins += 1

                # If player wins increment the value by 1
                # Return statement to say that the player wins.
                return f"🥳{name}, you Win!"

            else:
                python_wins += 1  # If computer wins increment the value by 1
                # Return statement to say that the computer has won
                return f"Sorry, {name}. Better luck next time.😢"
                # A new variable to call the nested function 'decide_winner' refering to the parameters above inside the function.

        game_result = decide_winner(player, computer)

        print(game_result)  # Print the output of 'game result'

    # Creating a way for the code to keep count of how many times it has been played.
    # We refer this variable to the nonlocal variables listed below which are defined in the function gn local scope above.
        nonlocal game_count  # Refering to the nonlocal variable
        game_count += 1  # Adding 1 everytime the game is played
        # Print out a statment that counts by converting the game_count to a string
        print(f"\nGame count: {game_count}")
        # print out the winning count.
        print(f"\n{name}'s wins: {player_wins}")
        # print out the winning count.
        print(f"\npython_wins: {python_wins}")
        # Print out the winning percentage for player where percentage is calculated by (player_wins/game_count) at 2 decimal places
        print(f"\nYour winning percentage: {player_wins/game_count:.2%}")
        # Print out the winning percentage for computer where percentage is calculated by (python_wins/game_count) at 2 decimal places
        print(f"\nPython winning percentage: {python_wins/game_count:.2%}")
        # Print out play again statement.
        print(f"\nPlay again, {name}?")

        # To play again we provide a while loop that must be True.
        while True:
            # For the loop to continue the 'playagain' variable is created to allow the player to input a choice of Y or Q.
            playagain = input("\nY for yes or \nQ to Quit \n")
            # If the player inputs a lower case we provide the .lower function so that python can understand the palyers input.
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break
            # An if else statement is created so that unless the player choses one of the two inputs the question will be re asked until it receives the correct input.

        if playagain.lower() == "y":
            # Create a if statement so if the player uses lower case choice the game still understands the input and if y chosen then we wish to replay game
            return play_gn()  # if the player choses y then game will restart and play again by calling the play_gn function
        else:  # else statement to begin the stop process
            print("\n🥳🎉\n")
            print("Thank you for playing!\n")
            # This will exit the game and return to the terminal config
            sys.exit(f"Bye {name}! 👋")

    # This is added to return the function
    return play_gn

    # We create a modules with args so that we can use the terminal to play the game and call the files


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

    guess_number = gn(args.name)
    guess_number()
