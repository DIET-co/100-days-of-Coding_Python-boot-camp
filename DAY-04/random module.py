import random


for n in range(0, 5):
    random_int = random.randint(1, 10)
    print(random_int)

random_heads_or_tails = random.randint(0, 1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("tails") 


import random
import string

# Lists for letters, numbers, and symbols
letters = []
numbers = []
symbols = []

# Fill the lists with random characters
for _ in range(100):  # Adjust the range for desired number of elements
    letters.append(random.choice(string.ascii_letters))  # Random letter (upper or lower case)
    numbers.append(random.choice(string.digits))         # Random digit (0-9)
    symbols.append(random.choice(string.punctuation))    # Random symbol (e.g., @, #, $)

# Print the lists
print("Letters:", letters)
print("Numbers:", numbers)
print("Symbols:", symbols)
