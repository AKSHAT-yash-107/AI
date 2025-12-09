n = int(input("Enter rows: "))

for i in range(1, n + 1):
    if i % 2 != 0:      # odd → ascending
        for j in range(1, i + 1):
            print(j, end=" ")
    else:               # even → descending
        for j in range(i, 0, -1):
            print(j, end=" ")
    print()
