def series(n):
    if n == 0:
        return 0
    return n + series(n-1)

print(series(77))
