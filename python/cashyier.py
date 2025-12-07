

a = int(input("Enter amount in hundreds: ")) 

amount = a * 100  

hundreds = amount // 100
remaining = amount % 100

fifties = remaining // 50
remaining = remaining % 50

tens = remaining // 10

print("\n--- Cashier Note Calculation ---")
print("100 Rs notes =", hundreds)
print("50 Rs notes  =", fifties)
print("10 Rs notes  =", tens)



basic = float(input("\nEnter Ramesh's Basic Salary: "))

da = 0.40 * basic     
hra = 0.20 * basic    

gross_salary = basic + da + hra

print("\n--- Gross Salary Calculation ---")
print("Basic Salary      =", basic)
print("Dearness Allowance (40%) =", da)
print("House Rent Allowance (20%) =", hra)
print("Gross Salary      =", gross_salary)
