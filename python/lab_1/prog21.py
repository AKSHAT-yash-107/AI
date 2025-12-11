def triangle(n):
    for i in range(n + 1):
        c = 1
        for j in range(i + 1):
            print(c, end=" ")
            c = c * (i - j) // (j + 1)
        print()

num = int(input("Enter a number: "))
triangle(num)
