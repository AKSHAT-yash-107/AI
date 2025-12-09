def fun(n):
    rev=0
    while(n>0):
        d=n%10
        rev=rev*10+d
        n=n//10
    return rev

x=int(input("enter number "))
print("reversed=",fun(x))
