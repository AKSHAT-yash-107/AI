#print element after removing even number
n=int(input("ENTER n: "))
list =[]
result=[]
for i in range(n):
    num = int(input("enter  element :"))
    list.append(num)
print(list)
    
for i in list:
    if i % 2 !=0:
        result.append(i)
print(result)