def is_prime(n: int) -> bool:
    """
    Determine if a given number is prime.
    
    Arguments:
    n (int): The number to check for primality.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
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