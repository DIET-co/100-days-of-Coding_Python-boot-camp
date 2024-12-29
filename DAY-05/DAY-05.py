import string
import random
# Create lists for letters, numbers, and symbols
letters = list(string.ascii_letters)  # All uppercase and lowercase letters
numbers = list(string.digits)        # Digits 0-9
symbols = list(string.punctuation)   # Common symbols (e.g., @, #, $, etc.)

print("Welcome to the pypassword Generator!")
nr_letters = random.randint(3, 10)
nr_symbols = random.randint(3, 8)
nr_numbers = int(input(f"how many numbers would u like?\n"))


def easy():
    password = "" 
    for char in range(0, nr_letters ):
     password += random.choice(letters)

    for char in range(0, nr_symbols ):
     password += random.choice(symbols)

    for char in range(0, nr_numbers ):
     password += random.choice(numbers)

    return(password) 

def hard():
  password_list = []
  for char in range(0, nr_letters ):
     password_list.append(random.choice(letters))
  for char in range(0, nr_symbols ):
     password_list.append(random.choice(symbols))
  for char in range(0, nr_numbers ):
     password_list.append(random.choice(numbers))
   
  random.shuffle(password_list)
  password = ""
  for char in password_list:
    password +=char  
  return(password)  

print("-------"*10)

print("easy password gen:",easy())
print("hard password gen:",hard())















 
  

