# Finding the Hypotenuse of a Right Triangle Using the Math Library

import math

#Input
a = float(input("Enter length for side a: "))
b = float(input("Enter length for side b: "))

#Processing
c = math.sqrt(pow(a, 2) + pow(b, 2))

#Output
print(f"The hypotenuse is {c:.2f}")