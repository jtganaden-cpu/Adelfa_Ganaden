# SG 7 - Validating Data Input and Verifying Output

# 1) Payment Method Checker - Acceptable Value
payment = ["cash", "gcash", "card"] # Only acceptable values
method = input("Enter payment method: ").lower() # Input

if method in payment: # Validate
    print("Valid payment method") # Output
else:
    print("Invalid payment method") # Output

# 2) Grade Checker - Range Validation
print("")
grade = int(input("Enter your grade: ")) # Input

if 0 <= grade <= 100: # Validate
    print("Valid grade") # Output

else:
    print("Invalid grade. Grade must be between 0 and 100.") # Output

# 3) Student ID Checker - Pattern Validation
import re # To make re.fullmatch() work

print("")
student_id = input("Enter Student ID: ") # Input

pattern = r"\d{4}-\d{4}" # Pattern to follow

if re.fullmatch(pattern, student_id): # Validate
    print("Valid Student ID") # Output
else:
    print("Invalid Student ID") # Output

# 4) PIN Validator - Combination: Length + Content Validation
print("")
pin = input("Enter 6-Digit PIN: ") # Input

if len(pin) == 6 and pin.isdigit(): # Validation for length and content
    print("Valid PIN") # Output
else:
    print("Invalid PIN. Enter exactly 6 digits.") # Output

# 5) Student Score Entry - Combination: Data Type + Range Validation
try: # Validation for data type
    print("")
    score = int(input("Enter examination score: ")) # Input
    if 0 <= score <= 100: # Validation for range
        print("Valid score.") # Output

except ValueError: # Validation for data type
    print("Invalid input. Please enter a number.") # Output

