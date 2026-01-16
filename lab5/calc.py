import math
from sympy import symbols, diff, integrate

x = symbols('x')

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def power(a, b):
    return a ** b

def factorial(n):
    if n < 0:
        return "Error: Factorial of negative number"
    return math.factorial(n)

def square_root(n):
    return math.sqrt(n)

def cube_root(n):
    return n ** (1/3)

def derivative(expr):
    return diff(expr, x)

def integration(expr):
    return integrate(expr, x)


while True:
    print("\n--- CALCULATOR MENU ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Factorial")
    print("7. Square Root")
    print("8. Cube Root")
    print("9. Derivative")
    print("10. Integration")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 0:
        print("Calculator Closed.")
        break

    elif choice in [1, 2, 3, 4, 5]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == 1:
            print("Result:", add(a, b))
        elif choice == 2:
            print("Result:", subtract(a, b))
        elif choice == 3:
            print("Result:", multiply(a, b))
        elif choice == 4:
            print("Result:", divide(a, b))
        elif choice == 5:
            print("Result:", power(a, b))

    elif choice == 6:
        n = int(input("Enter a number: "))
        print("Result:", factorial(n))

    elif choice == 7:
        n = float(input("Enter a number: "))
        print("Result:", square_root(n))

    elif choice == 8:
        n = float(input("Enter a number: "))
        print("Result:", cube_root(n))

    elif choice == 9:
        expr = input("Enter expression in x (example: x**2 + 3*x): ")
        print("Derivative:", derivative(expr))

    elif choice == 10:
        expr = input("Enter expression in x (example: x**2): ")
        print("Integration:", integration(expr))

    else:
        print("Invalid choice")
