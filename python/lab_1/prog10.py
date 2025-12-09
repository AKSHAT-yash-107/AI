def prime_factors(n):
    factors = []

    # check for factor 2
    if n % 2 == 0:
        factors.append(2)
        while n % 2 == 0:
            n //= 2

    # check for odd factors
    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            while n % i == 0:
                n //= i
        i += 2

    # if remaining n > 2, it is prime
    if n > 2:
        factors.append(n)

    return factors


x = int(input("Enter a number: "))
result = prime_factors(x)

print("Distinct Prime Factors:", *result)
