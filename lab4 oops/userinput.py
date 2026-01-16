try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if b == 0:
        raise ZeroDivisionError("Second number cannot be zero")

    result = a / b
    print("Result:", result)

except ZeroDivisionError as e:
    print("Exception:", e)
5
