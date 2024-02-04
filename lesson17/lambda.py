# Two topics, Lambda fuctions & ??

# Lambda functions - A lambda function is a single expression that returns a value.

from functools import reduce
def squared(num): return num * num


# lambda num : num * num. VScode auto formats the lambda
print(squared(4))


def addTwo(num): return num + 2


# lambda num : num + 2. VScode auto formats the lambda
print(addTwo(12))


def sum_total(a, b): return a + b
# lambda a, b : a + b. VScode auto formats the lambda


print(sum_total(2, 3))

# When would you use a Lambda function.?
# They are often used inside another function, for a quick function.


def funcBuilder(x):
    return lambda num: num + x


add_ten = funcBuilder(10)
add_twenty = funcBuilder(20)

print(add_ten(7))
print(add_twenty(7))

# Higher order functions
# A higher order function is a function that take 1 or more function as an arguments or a function that returns a function as its result.

# MAP
numbers = [3, 7, 12, 18, 20, 21]  # Create a list
# Square the numbers in the list. Using the map function
squared_nums = map(lambda num: num * num, numbers)
print(list(squared_nums))  # Print out new list

# FILTER

# The lambda function returns a True or False if the numbers are odd.
odd_nums = filter(lambda num: num % 2 != 0, numbers)
# The filter function filters out the even numbers.
# Prints new list with only the odd numbers filtered from the list
print(list(odd_nums))

# REDUCE

numbers = [1, 2, 3, 4, 5, 1]

total = reduce(lambda acc, curr: acc + curr, numbers, 10)

print(total)

print(sum(numbers, 10))

# Second example of reduce
# List of names that are strings
names = ['Dave Gray', 'Sara Ito', 'John Jacob jingleheimerschmidt']

# Using the length function as names are strings to get total of characters.
char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)
