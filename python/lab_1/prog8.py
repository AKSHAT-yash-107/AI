def fun(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s

x = int(input("Enter number: "))
s = fun(x)

print("Perfect" if fun(x)== x else "Not Perfect")
