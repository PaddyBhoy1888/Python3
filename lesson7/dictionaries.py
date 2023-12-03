# Dictionaries are used to store values that are in key value pairs

band = {
    "vocals": "Plant",
    "guitar": "Page"
}
# Method 1 for creating dictonaries

band2 = dict(vocals="Plants", guitar="Page")
# Method 2 for creating dictonaries

print(band)
# prints method 1 for band
print(band2)
# prints method 2 for band2

print(type(band))
# Checks the type class of the dictionary band
print(len(band))
# Checks the length of the dictionary band

print(type(band2))
# Checks the type class of the dictionary band2
print(len(band2))
# Checks the length of the dictionary band2


# Access items in a dictionary

print(band["vocals"])
# Method 1 - refer to the dictionary and refernce the key to get the value associated with that key
print(band.get("guitar"))
# Method 2 - refer to the dictionary and refernce the key to get the value associated with that key

# LIST ALL KEYS

print(band.keys())
# This will print the list of Keys

# LIST ALL VALUES
print(band.values())
# This will print the list of Keys

# LIST OF KEY/VALUE PAIRS AS TUPLES

print(band.items())
# prints out the keys and values of each pair as a tuple

# VERIFY A KEY EXISTS

print("guitar" in band)
# This will check if the key "guitar" in dictionary band exists and return a boolean True or False
print("triangle" in band)
# This will check if the key "triangle" in dictionary band exists and return a boolean True or False

# CHANGE VALUES

band["vocals"] = "coverdale"
# Updates the value in vocals from plant to coverdale
band.update({"bass": "JPJ"})
# Adds a new key/value pair to the dictionary
print(band)
# print the dictionary band to confirm changes

# REMOVE ITEMS
print(band.pop("bass"))
# Using the pop method this will remove the key/value pair "bass" and will only return the value "JPJ"
print(band)
# print the dictionary band to confirm changes

band["drums"] = "Bonham"
# Creates a new key/value pair dictionary
print(band)
# print the dictionary band to confirm changes

print(band.popitem())
# Removes the last key/value pair but returns a Tuple that has been removed.
print(band)
# print the dictionary band to confirm changes

# DELETE & CLEAR

band["drums"] = "bonham"
# Adds the key/value pair into the band dictionary
print(band)
# print the dictionary band to confirm changes
del band["drums"]
# Using the 'del' or delete function we can remove the key "drums" from the band dictionary
# This will also remove the value associsiated with the key.
# To delete the value we must specify the key as specifying the values returns a error
print(band)
# print the dictionary band to confirm changes

print(band2)
# print band2 so we can see what is in the dictionary before attempting to change
band2.clear()
# Clears all the key/value pairs from the dictionary
print(band2)
# print the dictionary band2 to confirm changes

del band2
# Using the 'del' function we can completely delete the dictionary band2.
# print(band2)
# Trying to print this dictionary after being deleted will return a 'not identified' error.


# COPY DICTIONARIES

# The first method below is not prefered as it is a refernce copy method and add/remove from one effects the other.
# band2 = band
# This method creates a refernce to band not a copy
# print("Bad copy!")
# This is a bad copy as if we add or remove from band2 it will also add and remove from band
# print(band2)
# print band2 to confirm changes
# print(band)
# print band to confirm changes

# band2["drums"] = "Dave"
# Adds a key/value pair to band2
# print(band2)
# print band2 to confirm changes
# print(band)
# print band to confirm changes
