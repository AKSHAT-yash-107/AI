def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def prime_series(n):
    count = 0
    num = 3
    while count < n:
        if is_prime(num):
            print(num, end=" ")
            count += 1
        num += 1

n = int(input("Enter n: "))
prime_series(n)
