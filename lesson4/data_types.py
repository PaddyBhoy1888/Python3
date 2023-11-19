# String data type

# Literal assignment
# Lierally assign the value dave as a string to the variable first
import math
first = "Dave"
last = "Gray"

# print(type(first))                    #To comment out code not to be used select all and use Ctrl + /. You can use the same command to un comment out
# print(type(first) == str)
# print(isinstance(first, str))

# Constructor function
# pizza = str("Pepperoni")
# print(type(pizza))  # Ctrl + C to copy the print code above & Ctrl + V. Highlight the first 'first' & Ctrl + D to select the other instances to change 'first' to 'pepperoni'
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatination. Adding two strings together to form a larger string
fullname = first + " " + last
print(fullname)

fullname += " ! "   # The += takes the value for fullname and adds to it, in this instance !
print(fullname)

# Casting a number to a string. Take a number and change it to a string

# Here we see the value 1980 as a string not as a number which is needed to use concatination
decade = str(1980)
print(type(decade))
print(decade)

statement = " I Like rock Music from " + decade + "s"
print(statement)

# Multiple Lines
multiline = '''
Hey, how are you?

I was just checking in. 
                    All good?

'''
print(multiline)

# Escaping special characters

# \' helps to use a ' in a sentence. \t provides space between the sentence. \n adds a return line. \\ allows for 1 \.
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# String Methods. Methods are functions that are called on the string clas.

print(first)  # Prints the value assigened to the variable first
print(first.lower())  # Prints the value in all lower case
print(first.upper())  # Prints the value in all upper case
print(first)


# Turns everything into proper case and capitalising the first letter of every word
print(multiline.title())
print(multiline.replace("good", "ok"))  # Replaces good with ok
print(multiline)

# White space check
print(len(multiline))  # len is length and counts the characters. Original length
# Change the length using += to increase with white space
multiline += "                           "
# Adds length to the begining of muti line
multiline = "            " + multiline
print(len(multiline))

# Methods to remove white space
# Strip removes the white space. Add len to get length
print(len(multiline.strip()))
print(len(multiline.lstrip()))  # Only remove white space from the left side
print(len(multiline.rstrip()))  # Only remove white space from the riht side

print("")  # Allows for a blank space on the code read out so as to not have all code read out together. i.e. a space between

# Build a Menu

title = "menu".upper()  # Sets the string using upper case
# Print the title and use center method by passing in 20 characters with a value of =.
print(title.center(20, "="))
# This left justifies the text coffee with 16 charecters and fills the space with '.'. Then inside we can contcatinate with the string $1 and right justify it with 4 chracters, no space to fill so only one argument required.
print("coffee".ljust(16, ".") + "$1".rjust(4))
# Adding to the menu using different menu items
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

print("")

# string index values.
# note indexes start at zero so the number 1 is ctually the second letter
print(first[1])
# -1, gets the last letter.
print(first[-1])
# Creates a range [1:-1]. When you create a range you must consider that the last selected point on the range will not output so this needs to be considered.
print(first[1:-1])
# To get the full range leave the second value empty and start at 0.
print(first[0:])

# Some methods return boolean data
# Checks to see if the variable first starts with 'D'. Will return boolean True or False
print(first.startswith("D"))
print(first.endswith("Z"))  # Checks to see if ends with 'Z'. ""

# Bollean data type

# Must be proper case i.e. capital 'T' for true or 'F' for false to be correct boolean type
myvalue = True
# bool is a constructor function so can be set as a data type in a few ways
x = bool(False)  # Set the variable 'x' to equal a boolean 'False'
print(type(x))  # Check the type 'x'
# Check is the instance 'myvalue' a 'boolean type.
print(isinstance(myvalue, bool))

# Numeric data types
# Integer
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# float type has decimals

gpa = 3.28
y = float(1.14)
print(type(gpa))

# complex type
comp_value = 5 + 3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)


# built in numbers and functions

print(abs(gpa))
# absolute value of gpa
print(abs(gpa * -1))
# Multiple the absolute by -1

print(round(gpa))
# This would round the value to the nearest integer

print(round(gpa, 1))
# This would round to the nearest specified decimal place

print(math.pi)
# Print the value of Pi
print(math.sqrt(64))
# Print the square route of 64
print(math.ceil(gpa))
# Print the cling of gpa * Highest point
print(math.floor(gpa))
# print the floor of gpa * Lowest point, rounding down to int


# Casting a string to a number

zipcode = "10001"
print(zipcode)
zip_value = int(zipcode)
print(type(zip_value))
print(zip_value)
#
