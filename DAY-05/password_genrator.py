import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password_list = []

# Append random letters to the password list
for _ in range(nr_letters):
    password_list.append(random.choice(letters))

# Append random symbols to the password list
for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

# Append random numbers to the password list
for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

# Shuffle the password list to randomize the characters
random.shuffle(password_list)

# Convert the password list to a string
password = ''.join(password_list)

print(f"Your generated password is: {password}")
