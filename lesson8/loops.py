# When talking about loops there are two types a 'While Loop' & a ' for Loop'

# A while loop will execute a block of code when a condition is true.

value = 1  # Creates a variable with the value of '1'
# while value <= 10:  # This provides a while value of less than or equal to 10
#     print(value)
#     if value == 8:
#         break  # We can stop the loop using a if & break statement and determine if the value reaches
#         # the defined value the loop should stop
#     value += 1  # This will create an increament of 1 up o 10 and then stop.

# while value <= 10:  # This provides a while value of less than or equal to 10
#     value += 1  # This will create an increament of 1 up o 10 and then stop. The value is incremented
#     # before the if statement here as if not then the value would only increment the value defined below.
#     if value == 5:
#         continue  # We can continue the loop using a if & continue statement. This means the loop will continue
#     # beyond the stated value and skip it.
#     print(value)
# else:  # The addition of an else statement allows us to print the final value if the loop is allowed to complete.
#     # Note if break is used the else statement would not work.
#     # Print the value as a string using the 'str' as value is an integer.
#     print("Value is now equal to "+str(value))

# FOR LOOPS

# A for loop itirates over a sequence like lists, tuples, dic, sets or individual characters of a string.

# Creates a list 'names' with three string variables inside.
# names = ["Dave", "Sara", "John"]
# for x in names:  # Using a for loop we can make assign 'x' for the values in the list.
#     # Here we will print the 'x' which will be the result of the values asigned from the list.
#     print(x)

# for x in "Mississippi":  # We can use for loops to go through a string. Here we will
#     # Here we will print the string as its own letter of the string as the loop iterates
#     print(x)

# for x in names:  # Another for loop using the variable 'names'
#     if x == "Sara":  # We use the if statement for when x equals "Sara" to initiae a break function
#         break
# # We print the output of x. Note as the loop iterates it stops and will not display the value defined as it ==.
#     print(x)

# for x in names:  # Another for loop using the variable 'names'
#     if x == "Sara":  # We use the if statement for when x equals "Sara" to initiae a continue function
#         continue
# # We print the output of x. Note as the loop iterates it skips the defined value and continues the loop.
#     print(x)

# WE CAN USE FOR LOOPS IN RANGES

# for x in range(4):  # We create a range of '4' numbers, note range always starts a '0'
#     print(x)

# for x in range(2, 4):  # We create a range of numbers starting at '2' and ending at '4'. Doesn't use the number to be stopped on.
#     print(x)

# for x in range(5, 101, 5):  # We create a range of numbers starting at '5' and ending at '101'. In increaments of '5'
#     print(x)
# else:
#     # Else statement will print once 'For loop' has finished
#     print("Glad thats\'s over!")

names = ["Dave", "Sara", "John"]
actions = ["Codes", "Eats", "Sleeps"]

# Nested for loops i.e. loop within a loop

# for name in names:  # A for loop where the value defined as 'name' in the varible 'names'
#     for action in actions:  # A for loop inside the firts loop where value defined 'action' in variable 'actions'
#         print(name + " " + action + ".")
#         # When we print this the loop will apply each 'action' value to each 'name value in order.

for action in actions:  # A for loop where the value defined as 'action' in the varible 'actions'
    for name in names:  # A for loop inside the firts loop where value defined 'name' in variable 'names'
        print(name + " " + action + ".")
        # When we print this the loop will apply each 'name' value to each 'action' value in order.
