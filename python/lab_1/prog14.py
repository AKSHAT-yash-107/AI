def sum_series(n):
    total = 0
    for i in range(1, n + 1):
        inner_sum = (i * (i + 1)) // 2
        total += inner_sum
    return total

n = int(input("Enter n: "))
print("Sum =", sum_series(n))
