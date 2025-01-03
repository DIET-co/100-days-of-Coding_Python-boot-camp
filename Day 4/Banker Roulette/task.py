import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

for _ in range(10):
    choice = random.choice(friends)

    print("The person playing the bill:", choice)