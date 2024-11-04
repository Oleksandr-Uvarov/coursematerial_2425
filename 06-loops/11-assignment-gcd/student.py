def gcd(x, y):
    if x < 0:
        x = -x
    if y < 0:
        y = -y

    divisor = max(x, y)

    while True:
        if divisor > x or divisor > y:
            divisor -= 1
            continue

        if divisor == 0:
            return 1
        
        if x % divisor == 0 and y % divisor == 0:
            break
        else:
            divisor -= 1

    return divisor

print(gcd(10, -15))