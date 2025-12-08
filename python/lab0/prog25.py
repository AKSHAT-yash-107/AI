def sq(n):
    if n == 1:
        return 1
    return n*n + sq(n-1)

print(sq(9))
