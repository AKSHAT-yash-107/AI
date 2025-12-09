def fun(n):
    sum=0
    while(n):
        sum+=n%10
        n//=10
    return sum

x=int(input("enter number "))
print("the sum of digits=",fun(x))