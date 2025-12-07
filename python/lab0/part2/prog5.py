n = int(input("Enter 3-digit number: "))
original_n = n  


last_digit = original_n % 10

first_digit = original_n

while first_digit >= 10:
    first_digit = first_digit // 10


print(f"Original Number: {original_n}")
print(f"First D: {first_digit}")
print(f"Last Digit: {last_digit}")

if first_digit == last_digit:
    print("**Palindrome**")
else:
    print("**Not Palindrome**")