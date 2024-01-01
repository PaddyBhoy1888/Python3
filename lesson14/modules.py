# Modules can be considered small code libraries that are based on key features

import sys
import random as rdm  # This is a built in module, here we extract rdm only

from math import pi  # This is a built in module, here we extract pi from the module only
from enum import Enum  # This is a built in module, here we extract Enum only

import kansas


print(pi)

# for item in dir(rdm):
#    print(item)

print(kansas.capital)
kansas.randomfunfact()

print(__name__)
print(kansas.__name__)

# rock_paper_scissors()
