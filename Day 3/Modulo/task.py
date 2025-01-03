def isPrime(n):
    if n <= 1:
        return False

    # Check divisibility from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def isoddEven(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

if __name__ == "__main__":
  number = int(input("Enter a number: "))
  isoddEven(number)
  if(isPrime(number)):
    print("prime")
  else:
    print("not prime")