def prime(n):
    flag=True
    if n<2:
        flag=False
    else:
        for i in range (2, int(n**0.5)+1):
            if n % i ==0:
                flag=False
                break
    print("Prime" if flag else "Not Prime")

x=int(input("enter number "))
prime(x)