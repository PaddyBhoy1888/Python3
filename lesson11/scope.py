# There are different type of scope, here we will look at the global scope

# Define the variable name with value of "Dave". This variable is inside the global scope as can be used or called from anywhere in the code and not defined as part of any specific function etc.
name = "Dave"
count = 1  # Global variable

# # Defining a function called greeting which will accept name parameter.
# def greeting(name):
#     # The 'name' value here is in the local scope but can refer to the global scope as well. to stop this we specify the value inside the call function as "John"
#     colour = "blue"
#     # The print colour only works here in the local sope as it not defined in the global scope like 'name'
#     print(colour)
#     print(name)


# We can define a new function and within that function call another function as the function as a whole is within the global scope.
def another():
    colour = "blue"
    # Refers to the global value defined in global scope, not a new variable inside function.
    global count
    count += 1
    print(count)

    # Nested function as function within function. As to not pollute the global scope.
    def greeting(name):
        nonlocal colour
        colour = "red"
        print(colour)
        print(name)

    greeting("Dave")


another()
