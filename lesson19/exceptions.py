# Exceptions

# Exceptions are raised errors that are produce when python does not fully compute what is being asked or variables are missing

class JustNotCoolError(Exception):
    pass


x = 2

try:  # This will 'try' to catch any errors
    raise JustNotCoolError("This is not cool man")
    # raise Exception("I'm a custom Exception")
    # print(x/0)
    # if not type(x) is str:
    #    raise TypeError("only strings are allowed")
# except:  # This will except/catch all the errors python gives and with the print statement below we can provide our own text output
#    print('There is an error')
except NameError:  # This will except only the 'Name' error python gives and with the print statement below we can provide our own text output
    print('Name Error means something is probarly not defined')

except ZeroDivisionError:  # This will catch Zero division error's
    print('Please do not divide by zero.')

except Exception as error:  # This will catch
    print(error)
else:  # This will output if there are no errors
    print('No errors!')
finally:  # This will print with or without an error
    print("I'm going to print with or without an error")
