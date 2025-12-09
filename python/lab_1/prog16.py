def star_pyramid(n):
    for i in range(1, n + 1):
        # print spaces
        print(" " * (n - i), end="")
        # print stars with spaces
        print("* " * i)

n = int(input("Enter rows: "))
star_pyramid(n)
