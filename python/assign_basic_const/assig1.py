#Create an array that is having user defined inputs and with the help of for loop, fetch all the prime numbers and print the numbers.
# Create an empty list
arr = []

# Take number of elements from user
n = int(input("Enter how many numbers: "))

# Take user inputs
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    arr.append(val)

print("Prime numbers are:")

# Function to check prime
for num in arr:
    if num > 1:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
