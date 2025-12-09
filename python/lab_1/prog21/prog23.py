def decimal_to_base(n, b):
    digits = ""

    while n > 0:
        rem = n % b
        digits = str(rem) + digits
        n //= b

    return digits

num = int(input("Enter decimal number: "))
base = int(input("Enter base: "))

print("Result =", decimal_to_base(num, base))
