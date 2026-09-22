# Username Validator Program

# Prompt user for username
username = input("Enter username: ")

# Check if the username length is between 5 and 10 characters
# AND check if it contains only letters and numbers 
if 5 <= len(username) <= 10 and username.isalnum():
# If both conditions are met, the username is valid
    print("Valid username.")

else:
# If either condition fails, the username is invalid
    print("Invalid username.")
