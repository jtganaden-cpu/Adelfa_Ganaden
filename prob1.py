# User Age Validator
# Author: Princess Sofia H. Macala
# Section: 8-Adelfa
# Date: September 22, 2026

# This program determines if the user's age is within the range and is in the correct data type.

# We use try and except ValueError to only get an input with a valid data type
try:
    # Ask for the user's age
    age = int(input("Enter your age: "))

    # Check if the user's age is between 12 and 18, if not, then display Invalid age
    if 12<=age<=18:
        print("Valid age.")
    else:
        print("Invalid age.")
except ValueError:
    print("Invalid input. Please enter a whole number")
