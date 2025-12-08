import math

def stats(a, b, c, d, e):
    nums = [a, b, c, d, e]
    s = sum(nums)
    avg = s / 5
    variance = sum((x - avg)**2 for x in nums) / 5
    sd = math.sqrt(variance)
    return s, avg, sd

print(stats(10, 60,70, 40, 50))
