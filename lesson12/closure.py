# Closure is a function having access to the scope of its parent function after the parent function has returned.

# define a function called 'parent_function' that will recieve one parameter.
def parent_function(person):
    coins = 3  # Derfine a variable 'coins' that is equal to 3

    def play_game():  # Define a nested function called 'play_game' that has no parameters defined
        nonlocal coins  # The 'nonlocal' will allow the function to use the global scope and not local scope for the coins value
        coins -= 1  # Here we will reduce the value obtained from the global scope by -1 each time function is run

        if coins > 1:  # Logic with if statement, so if value is greater than 1 return statement below.
            # Remember that the coins is an integer and needs to be converted to a string using the 'str' constructor.
            print("\n" + person + "has" + str(coins) + "coins left.")

        # Logic with esleif statement, so if value is equal to 1 return statement below.
        elif coins == 1:
            print("\n" + person + "has" + str(coins) + "coin left.")

        else:  # Logic with else statement, so for every other value return statement below.
            print("\n" + person + "is out of coins.")

    return play_game  # returns the nested function inside the parent function


# Define 'tommy' variable and call parent function with input parameter "Tommy"
tommy = parent_function("Tommy")
# jenny = parent_function("Jenny", 5)

tommy()
# tommy()

# jenny()

# tommy()
