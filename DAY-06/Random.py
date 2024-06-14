def is_prime(n: int) -> bool:
    
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

counter = 0
num = 2

while counter < 100:
    if is_prime(num):
        print(num)
        counter += 1
    num += 1