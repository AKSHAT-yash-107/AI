def special_series(n):
    val = 1
    for i in range(1, n + 1):
        print(val, end=" ")
        val = val * 2 + (i - 1)

n = int(input("Enter n: "))
special_series(n)
