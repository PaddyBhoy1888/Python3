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

users.insert(0, 'Bob')
# Inster the variable 'Bob' into the users list at the 0 position i.e. first
print(users)
# Prints the list users to confirm changes

users[2:2] = ['Eddie', 'Alex']
# Another method to insert names with brackets to insert two variable in the second position and stop at second.
print(users)
# Prints the list users to confirm changes

users[1:3] = ['Robert', 'JPJ']
# The range specified determines if a variable is replaced.
# using 1:3 we replace the position 1 & 2 but stop at position 3.
print(users)
# Prints the list users to confirm changes

# Remove a user

users.remove('Bob')
# Remove the variable 'Bob' from the users list
print(users)
# Prints the list users to confirm changes

print(users.pop())
# This is the 'pop' method that returns the last variable in the list then removes it from the list.
print(users)
# Prints the list users to confirm changes

# Delete a user or item

del users[0]
# This is the delete function that allows deleting from a list. Here we delete the list variable at 0 position.
print(users)
# Prints the list users to confirm changes

# del data
# This deletes the whole list and when printed then python will not find it.
print(data)
# Prints the list data to confirm changes

# Instead of deleting the full list we can use the clear method
data.clear()
# This will clear all the variables in the list. but list will still exist
print(data)
# Prints the list data to confirm changes

# Sort lists

users[1:2] = ['dave']
# Replacing the position 1 with the variable name 'dave' as lower case to see how this impacts the sort method.
users.sort()
# This will sort the variables in the users list by alphabetical order.
# If the variable starts with a lower case it will auto go to the end.
print(users)
# Prints the list users to confirm changes

users.sort(key=str.lower)
# This will allow us to sort the names including lower case. As all the name variables are string the key=str
# allows the strings to be all considered as lower case and then sorted in order.
print(users)

# Numbers

nums = [4, 42, 78, 1, 5]
# Creates a list of numbers
print(nums)
# Prints the nums list to confirm changes

nums.reverse()
# Allows to sort a list in the reverse order starting with the last first etc.
print(nums)
# Prints the nums list to confirm changes
