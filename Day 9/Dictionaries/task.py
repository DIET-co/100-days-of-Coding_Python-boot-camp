programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}


for key, value in programming_dictionary.items():
    print(key, value)

print("_-"*25)

for key in programming_dictionary:
    print(key)

for key in programming_dictionary:
    print(programming_dictionary[key])
