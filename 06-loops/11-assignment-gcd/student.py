def gcd(x, y):
    if x < 0:
        x = -x
    if y < 0:
        y = -y

    divisor = min(x, y)
    while True:
        if divisor == 0:
            return 1
        
        if x % divisor == 0 and y % divisor == 0:
            break
        else:
            divisor -= 1

    return divisor

print(gcd(10, -15))
print(gcd(12, 16))
print(gcd(40, 20))
print(gcd(20, 25))
print(gcd(100, 100))
print(gcd(17, 31))
print(gcd(17*31*97, 17 * 37 * 97))
print(gcd(10**100, 10**100))
            # (12, 16, 4),
            # (40, 20, 20),
            # (20, 25, 5),
            # (100, 100, 100),
            # (17, 31, 1),
            # (17 * 31 * 97, 17 * 37 * 97, 17 * 97),
            # (10**100, 10**200, 10**100),
