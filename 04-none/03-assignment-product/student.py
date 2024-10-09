def product(x, y, z):
    # numbers = [x, y, z]

    # i = 0
    # for number in numbers:
    #     if number is None:
    #         numbers[i] = 1
    #     i += 1
    
    # return numbers[0] * numbers[1] * numbers[2] 

    if x is None:
        x = 1
    if y is None:
        y = 1
    if z is None:
        z = 1
    
    return x * y * z