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
