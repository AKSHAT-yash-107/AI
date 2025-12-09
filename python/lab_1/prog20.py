def reverse_pyramid(n):
    for i in range(n, 0, -1):
        
        for j in range(1, i + 1):
            print(j, end=" ")

        for j in range(i - 1, 0, -1):
            print(j, end=" ")

        print()


num = int(input("Enter a number: "))
reverse_pyramid(num)
