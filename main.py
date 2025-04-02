import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Option 1: Easy

# Empty password string
password = ""

# Generating random letters
for letter in range(1, nr_letters+1):
    password += random.choice(letters)

# Generating random symbols
for symbol in range(1, nr_symbols+1):
    password += random.choice(symbols)

# Generating random numbers
for number in range(1, nr_numbers+1):
    password += random.choice(numbers)

print(f"Here's your password {password}.")

# Option 2: Difficult

# Converting the password string to a list
password_list = list(password)
print(password_list)

# Shuffling the password list
random.shuffle(password_list)

# Printing the final password
new_password = ""
for char in password_list:
    new_password += char

print(f"Your shuffled password is : {new_password}")
