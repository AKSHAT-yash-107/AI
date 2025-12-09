n = int(input("Enter rows: "))

for i in range(1, n + 1):
    start = 1 if i % 2 != 0 else 0
    for j in range(i):
        print(start, end=" ")
        start = 1 - start      # alternate 1 ↔ 0
    print()
