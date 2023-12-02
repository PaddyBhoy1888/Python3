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

# nums.sort(reverse=True)
# This will sort the list in decending order starting with the larges number
# print(nums)
# Prints the nums list to confirm changes

# Global sort function to print out sort changes without changing the list
print(sorted(nums, reverse=True))
# Here we print using the sorted function to sort the nums list using the 'revers=True' function.
# This is to again sort the list without changing the original list.
print(nums)
# Prints the nums list to confirm changes

# Make copy & sort

# The three methods below can be used to make a copy of a list.
numscopy = nums.copy()
# Method 1
mynums = list(nums)
# Method 2
mycopy = nums[:]
# Method 3

print(numscopy)
# Prints the numscopy list to confirm changes
print(mynums)
# Prints the mynums list to confirm changes
print(mycopy)
# Prints the mycopy list to confirm changes

mycopy.sort()
# Sorts the mycopy list in ascending order.
print(mycopy)
# Prints the mycopy list to confirm changes

# Check the type of list to det the data class
print(type(nums))

mylist = list([1, "Neil", True])
# A method to create a list using the list constructor
print(mylist)
# Prints the mylist to confirm chages

# TUPELS

# Tupels are like lists except that they can not be changes and neithier can the order be changed.

mytuple = tuple(('Dave', 42, True))
# Creates a tuple using the tuple constructor
anothertuple = (1, 2, 3, 9, 2, 2, 5, 1)
# Creates a tuple without a constructor.

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

# How to copy a tuple

newlist = list(mytuple)
# Creates a new list using the list constructor for the variables in mytuple.

newlist.append('Neil')
# Here we can append the variable 'Neil' to the newlist

newtuple = tuple(newlist)
# We can then make the newlist into a tuple
print(newtuple)
# print the newtuple to to confirm the changes

# Unpacking a tuple

(*one, two, hey) = anothertuple
# Assigns the variables in the anothertuple to the one, two, hey variables.
# Note that assigning the * puts all inbetween variables to that set.
print(one)
print(two)
print(hey)

print(anothertuple.count(2))
# Allows the methos of counting how many '2' there are inside the anothertuple.
