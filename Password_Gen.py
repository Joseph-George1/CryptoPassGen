import random 
import time
import os

# List of characters to use for generating passwords
special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\', ';', ':', '\'', '"', ',', '.', '/', '<', '>', '?', '`', '~']
al_lis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 
'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
'U', 'V', 'W', 'X', 'Y', 'Z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Combine alphabets, numbers, and special characters
all_chars = al_lis + special_chars

# Asking the user for the password length
length = int(input("What is the password length you want?: "))
i = random.choices(all_chars, k = length)

# Check if the file exists, if not create it and write "Passwords History"
if not os.path.exists("passwords.txt"):
    with open("passwords.txt", 'w') as file:
        file.write("Passwords History")

# Hide the passwords.txt file
os.system("attrib +h passwords.txt")

# Open the passwords file in append mode
with open('passwords.txt', "a+") as file:
    # Read the file to check if it has a password or not
    test_string = file.read()
    if test_string.strip() != "":
        file.write("\n")  # Write a new line if the file is not empty

    # Write the generated password to the file
    file.write(''.join(i))
    file.write("\n \n")  # Add a newline after writing the password

# Printing the password to the terminal so the user can see & copy it
print("Generated Password:", ''.join(i))

# Wait for 15 seconds before exiting
time.sleep(15)
