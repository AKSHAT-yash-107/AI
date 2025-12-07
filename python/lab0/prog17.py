def calculate_average(a, b, c):
    total_sum = a + b + c
    average = total_sum / 3
    return average

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

result = calculate_average(num1, num2, num3)

print(f"The average is: {result}")