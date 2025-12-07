m1 = int(input("Sub1: "))
m2 = int(input("Sub2: "))
m3 = int(input("Sub3: "))

total = m1 + m2 + m3
avg = total / 3

if avg >= 90:
    grade = "O"
elif avg >= 80:
    grade = "E"
elif avg >= 70:
    grade = "A"
elif avg >= 60:
    grade = "B"
else:
    grade = "F"

print("Total =", total)
print("Average =", avg)
print("Grade =", grade)
