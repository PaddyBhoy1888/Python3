def hello_world():  # Using the 'def' key word we can define the function 'hello_world
    print("Hello World!")
# As the function is only defined above it needs to be called also or the running of the code will produce no output.
# Note case sensitive should not be caps, hifin etc


hello_world()  # This code will call the function and give the output.

# FUNCTIONS THAT CAN RECIEVE PARAMETERS


def sum(num1=0, num2=0):  # define sum function with placehold parameters =0
    # Checking to make sure values input are integers
    if (type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2


# Create a variable that calls the 'sum' function with two arguments
total = sum(4, 2)
print(total)

# FUNCTION WITH MULTIPLE ARGUMENTS

# Define the function using *args as the function may have an unknown amunt of arguments.


def multiple_items(*args):  # The '*' makes the args tuples to be owrked with
    print(args)
    print(type(args))   #


multiple_items("Dave", "John", "Sara")


# Two ** used before 'kwards'(Key word arguments).
def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))  # Identifies tha 'kwards' is a dictionary


# first & last as two word arguments.
mult_named_items(first="Dave", last="Gray")
