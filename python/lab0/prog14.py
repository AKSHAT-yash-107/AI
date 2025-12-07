n = int(input("Enter number: "))
rev = 0
original_n = n
while n > 0:
 
    digit = n % 10

    
    rev = (rev * 10) + digit

    
    n = n // 10

print(f"Original Number: {original_n}")
print(f"Reversed: {rev}")