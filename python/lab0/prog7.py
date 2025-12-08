import math

print("1. Area of Circle\n2. Area of Rectangle\n3. Area of Triangle")
ch = int(input("Enter choice: "))

if ch == 1:
    r = float(input("Radius: "))
    print("Area =", math.pi * r * r)

elif ch == 2:
    l = float(input("Length: "))
    b = float(input("Breadth: "))
    print("Area =", l * b)

elif ch == 3:
    b = float(input("Base: "))
    h = float(input("Height: "))
    print("Area =", 0.5 * b * h)

else:
    print("Invalid")
