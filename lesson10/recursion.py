# Recursion is when a function calls itself.

def add_one(num):  # define a function with one number

    if (num >= 9):  # If statement to check if num is greater than or equal to 9
        return num + 1  # Return which will end the function and return num + 1 when value is greater than 9

    total = num + 1  # create a new variable = num + 1
    print(total)

    return add_one(total)
# This is the recursive reaturn as the return will continue to call the function
# until the vaule is greater than the defined value in the if statement i.e. '9' in this case.


# To get the file to first call the 'add_one' function.
mynewtotal = add_one(0)
print(mynewtotal)
