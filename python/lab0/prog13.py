n = int(input("Enter number: "))
s = 0

for i in range(1, n):
    if n % i == 0:
        s += i

print("Perfect" if s == n else "Not Perfect")
