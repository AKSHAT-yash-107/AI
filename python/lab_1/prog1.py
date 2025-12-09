
def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f


x=int(input("ENTER number "))
print("factorial of ", x ,"is " ,fact(x) )

