import math


def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def main():
    print("WELCOME TO DEVSTORIES PLAYGROUND")
    print("-------------------------")
    while True:
        try:
            num = int(input("Enter a number to check if it is prime: "))
            if is_prime(num):
                print(f"{num} is a prime number.")
                return False
            else:
                print(f"{num} is not a prime number.")
                return False
        except Exception as ex:
            print("Invalid input. Please try again!!!")
            continue


if __name__ == "__main__":
    main()