def gcd(a,b):
    while(b):
        a=b
        b=a%b
    return a 

x=int(input("enter number1 "))
y=int(input("enter number2 "))
print("gcd=",gcd(x,y))