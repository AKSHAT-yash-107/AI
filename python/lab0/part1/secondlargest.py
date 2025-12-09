x=int(input("enter number"))
y=int(input("enter number"))
z=int(input("enter number"))
if (x > y and x < z) or (x > z and x < y):
    second = x
elif (y > x and y < z) or (y > z and y < x):
    second = y
else:
    second = z

print("Second largest =", second)