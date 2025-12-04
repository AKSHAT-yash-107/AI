
arr=[]
x=int(input("enter array size="))
sum=0
for i in range(x):
    num =int(input("enter numbr for:"))
    arr.append(num)
    sum+=num

print("sum = ",sum, "avg=",sum/x)
