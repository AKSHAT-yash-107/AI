def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

def is_strong(n):
    s = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        s += factorial(digit)
        temp //= 10
    return s == n

x = int(input("Enter number: "))
print("Strong Number" if is_strong(x) else "Not Strong")
