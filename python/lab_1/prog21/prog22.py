def string_pattern(s):
    n = len(s)
    rev = s[::-1]

    
    for i in range(n):
        left = s[:n - i]
        right = rev[:n - i]
        print(left + " " * (2 * i) + right)

   
    for i in range(n - 2, -1, -1):
        left = s[:n - i]
        right = rev[:n - i]
        print(left + " " * (2 * i) + right)



text = input("Enter string: ")
string_pattern(text)
