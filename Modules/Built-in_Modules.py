# Importing built-in Python modules

import math
import random
import datetime
import os

# Using math module
print("Value of pi : ",math.pi)
print("Square root of 17 :",math.sqrt(17))

# Using random module
print("\nRandom number between 1 and 10:", random.randint(1, 17))

# Using datetime module
now = datetime.datetime.now()
print("\nCurrent date abd time : ",now)
print("Current date :",now.date())
print("Current time :",now.time())

# Using os module
print("\nCurrent working directory:", os.getcwd())
print("List of files in this folder:", os.listdir())

