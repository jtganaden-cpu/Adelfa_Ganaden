# Finding the Hypotenuse of a Right Triangle Using the Math Library

import math # To make the actual formulas work like square root and power

# User enters the 2 lengths of their right triangle (Input Stage)
a = float(input("Enter length for side a: "))
b = float(input("Enter length for side b: "))

# Formula of finding the hypotenuse of the right triangle (Processing Stage)
c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))

# Showing the actual hypotenuse to the user (Output Stage)
print(f"The hypotenuse is {c:.2f}")