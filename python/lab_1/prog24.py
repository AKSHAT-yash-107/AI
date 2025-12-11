def base_to_decimal(number, base):
    number = number.upper()
    value = 0
    power = 0

    for digit in number[::-1]:
        if digit.isdigit():
            num = int(digit)
        else:
            num = ord(digit) - 55  

        value += num * (base ** power)
        power += 1

    return value

num = input("Enter number: ")
base = int(input("Enter base: "))
print("Decimal =", base_to_decimal(num, base))
