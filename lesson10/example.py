# while loops and how they evaluate the TRUE or FALSE condition

value = "y"

count = 0

while value:  # Implies the value exists or is true
    count += 1
    print(count)
    if (count == 5):
        break
    else:
        value = 0
        continue
