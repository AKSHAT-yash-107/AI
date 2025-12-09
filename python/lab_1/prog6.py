def odd(n,p):
   
       for i in range(n, p + 1):
             if i % 2 != 0:
                print(i, end=" ")

def even(n,p):
 
    for i in range(n, p + 1):
     if i % 2 == 0:
        print(i, end=" ")

start = int(input("Enter start : "))
end = int(input("Enter end : "))
print("odd=")
odd(start,end)
print()
print("even=")
even(start,end)



