def binary_to_decimal(b):
    value = 0
    power = 0
    for digit in b[::-1]:
        value += int(digit) * (2 ** power)
        power += 1
    return value

def decimal_to_octal(n):
    result = ""
    while n > 0:
        result = str(n % 8) + result
        n //= 8
    return result or "0"

def decimal_to_hex(n):
    hex_digits = "0123456789ABCDEF"
    result = ""
    while n > 0:
        result = hex_digits[n % 16] + result
        n //= 16
    return result or "0"

binary = input("Enter binary number: ")
dec = binary_to_decimal(binary)

print("Octal:", decimal_to_octal(dec))
print("Hexadecimal:", decimal_to_hex(dec))
