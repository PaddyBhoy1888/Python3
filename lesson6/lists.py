users = ['Dave', 'John', 'Sara']
# List of users

data = ['Dave', 42, True]
# A list of valid data

emptylist = []
# A list can be empty with no variables


# LISTS
print("Dave" in users)
# Here we can check if Dave is in the list of users and print an output which will return a Boolean response

print("Dave" in data)
# Here we can check if Dave is in the list of data and print an output which will return a Boolean response

print("Dave" in emptylist)
# Here we can check if Dave is in the list of emptylist and print an output which will return a Boolean response


# LIST POSITIONS
print(users[0])
# Prints the first input of the users, list given that the list always starts from the 0 position
print(users[1])
# Prints the second input of the users, list given that the list always starts from the 0 position

print(users[-2])
# Prints the second last input of the users, list given that the end of a list always starts from the -1 position
print(users[-1])
# Prints the last input of the users, list given that the end of a list always starts from the -1 position

# WORKING OUT POSITIONS USING VARIABLES IN LISTS
print(users.index('Sara'))
# To work out the position of the variable inside a list we can use the '.index'
print(users.index('Dave'))
# To work out the position of the variable inside a list we can use the .index
# print(users.index('Paddy'))
# To work out the position of the variable inside a list we can use the .index. Here we can even ask for a variable
# that is not in the list and python will return with the variable is not in the list.

# RANGES
# What if we want a range of values. We can use the [0:1]
print(users[0:2])
# This will check and print from the first position 0 to position 2. Note 2 will NOT print as the range is up and
# to the point of the range
print(users[1:])
# This will print from position 1 until end of list as no defined end point.
print(users[-3:-1])
# This will print from -3 to -1. This is similiar to the first range exapmle in that it starts from
# -3 i.e. 3 from last & prints up to but not including the last.

# LENGTH OF A LIST
print(len(emptylist))
# The 'len' function allows for the length of the list to be known.

# ADD TO AN EXISTING LIST
users.append('Paddy')
# Using the '.append' function we can add to an existing list called users.
print(users)
# prints the list to confirm user has been added.

# ADD TWO LISTS TOGETHER
users += ['Jason']
# The '+=' function allows the existing users list to be added to a new list created ['Jason']. Make sure []
# or it will add all letters as a list.
print(users)
# prints the list to confirm lists have been added together into one list and contains all users.

# EXTENDING A LIST
users.extend(['Robert', 'Jimmy'])
# Using the '.extend' function we can extend an existing list with a new list.
print(users)
# prints the list to confirm lists have been added together into one list and contains all users.
