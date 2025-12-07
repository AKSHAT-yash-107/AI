seconds = int(input("Enter  seconds: "))

hours = seconds // 3600
rem = seconds % 3600

minutes = rem// 60
seconds_left = rem % 60

print(f"{seconds} second = {hours} Hour, {minutes} Minute and {seconds_left} Second.")
