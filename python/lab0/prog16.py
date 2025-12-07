n = int(input("Enter the number of rows (n): "))

for i in range(1, n + 1):

    if i % 2 != 0:
       
        row_output = ""
        for j in range(1, i + 1):
            row_output += str(j) + " "
        
    else:
       
        row_output = ""
        for j in range(i, 0, -1):  
            row_output += str(j) + " "

  
    print(row_output.strip())