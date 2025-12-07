def hcf(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a*b) // hcf(a, b)

a = int(input("A: "))
b = int(input("B: "))

print("HCF =", hcf(a, b))
print("LCM =", lcm(a, b))
