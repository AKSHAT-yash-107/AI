def to_bin(n):
    if n == 0:
        return ""
    return to_bin(n//2) + str(n%2)

print(to_bin(100))
