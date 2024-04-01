import os
# r = Read
# a = Append
# w = Write
# x = Create

# Read - error if it doesn't exit

# Specifies the 'f' as file that will use the open operation to open the .txt file. as standard the file will use the read operation unless otherwise specified.
f = open("names.txt")

# prints out the context of the file as part of the 'f' variable.
# print(f.read())

# prints out the context of the file as part of the 'f' variable with only 4 characters specified.
# print(f.read(4))

# reads the first line and prints out.
# print(f.readline())

# Using two in a row will read the second line as well.
# print(f.readline())

# Creates a for in, wher we specify each line to be read in the 'f' variable above.
for line in f:
    print(line)

f.close  # Closes the 'for' 'in'


# A try block below, to try open the file.
try:
    f = open("names.txt")
    print(f.read())
# An except block to give info about the file trying to be open.
except:
    print("The file you want does not exist")
# A finally block used to close the try.
finally:
    f.close()


# Append - Creates the file if it does not exist.

# By default the file will open in read so a new argument of "a" is required to append.
# f = open("names.txt", "a")
# We can write to this file using the 'f.write'.
# f.write("Neil\n")
# closes the operation
# f.close

# By default the file will open in read.
# f = open("names.txt")
# We can read to this file using the 'f.read'.
# print(f.read())
# closes the operation
# f.close


# Write (Overwrite)

# By default the file will open in read so a new argument of "w" is required to write.
f = open("context.txt", "w")
# We can write to the file using 'f.write'. This will overwrite all the contents of the file with what is being specified.
f.write("I deleted all the conext")
# Closes the operation.
f.close()

# By default the file will open in read.
f = open("context.txt")
# We can read to this file using the 'f.read'.
print(f.read())
# closes the operation
f.close


# Two ways to create a new file.

# Opens a file for writing, creates the file if it does not exist.

f = open("names_list.txt", "w")
f.close()

# Creates the specified file, but returns an error if the file exists.
if not os.path.exists("dave.txt"):
    f = open("dave.txt", "x")  # 'x' means create
    f.close()

# Delete a file

# Aavoid an error if does not exist.
if not os.path.exists("dave.txt"):
    os.remove("dave.txt")
else:
    print("The file you wish to delete does not exist")


# With has built-in implicit exception handling.

with open("more_name.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)
