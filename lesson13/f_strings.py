# F_strings can be a better way to create multiple values in one string

# Both values below are global values
person = "Dave"  # Variable called 'person' with the value "Dave". Noting dave is a string
coins = 3  # Variable called coins with the value 3. Noting 3 is an integer.

# CONCATINATING STRINGS

# Using concatination we add all the values to gether to get one complete sentence as a string. Noting coins is integer and needs to be converted to a string value.
print("\n" + person + " has " + str(coins) + " coins left.")

# PREVIOUS %s FORMATTING

# This method uses the'%s' as an insert point for the defined values of the % variable at the end of the message variable.
message = "\n%s has %s coins left." % (person, coins)
print(message)

# PREVIOUS STRING.FORMAT() METHOD

message = "\n{} has {} coins left.".format(person, coins)
print(message)

message = "\n{1} has {0} coins left.".format(coins, person)
print(message)

message = "\n{person} has {coins} coins left.".format(
    coins=coins, person=person)
print(message)

# DICTIONARY METHOD
# Create a dictionary with key/value pairs
player = {'person': 'Dave', 'coins': 3}
message = "\n{person} has {coins} coins left.".format(
    **player)
print(message)


# F-STRING! THIS IS THE WAY

# This method requires the f at the start and to insert the values we want inside {}. The values are defined in the global scope
message = f"\n{person} has {coins} coins left."
print(message)

# We can even use equations inside the {} instead of specified values
message = f"\n{person} has {2*5} coins left."
print(message)

# We can even use formatting inside the {} instead of specified values
message = f"\n{person.lower()} has {2*5} coins left."
print(message)

# We can also use the dictionary defined values
message = f"\n{player['person']} has {2*5} coins left."
print(message)

# ANOTHER METHOD IS TO PASS FORMATTINFG OPTIONS

num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")

# WE CAN ALSO MAKE A LOOP

for num in range(1, 11):
    print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")

for num in range(1, 11):
    print(f"{num} divided by 4.52 is {num / 4.52:.2%}")
