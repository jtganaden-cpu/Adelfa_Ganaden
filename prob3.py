# 3. School Grade Level Validator

# Data Type Validator
try:
    grd_lvl = int(input("Enter your grade level: ")) # Input
    if 7 <= grd_lvl <= 12: # Range Validator (accepted values only from grade 7 to 12).
        print("Valid grade level.") # Line 7, 10, and 13 are all possible outputs that depend on the user's input.

    else:
        print("Invalid grade level.")

except ValueError:
    print("Invalid grade level. Please enter a whole number.")

# Author: Jeyah Mae T. Ganaden
# Section: Adelfa