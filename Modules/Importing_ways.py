# First way
import MyMath
print("Square of a number using module :",MyMath.sqr(17))

# Second way
from MyMath import sqr
print("Square of a number using module :",sqr(17))

# Third way
import MyMath as get
print("Square of a number using module :",get.sqr(17))

