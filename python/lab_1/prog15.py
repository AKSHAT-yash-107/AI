def star_pattern(n):
    for i in range(1, n + 1):
        print("* " * i)

n = int(input("Enter rows: "))
star_pattern(n)
