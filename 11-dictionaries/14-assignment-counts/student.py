def count(xs):
    items = set(xs)
    result = {}
    count = 0

    for target in items:
        for value in xs:
            if target == value:
                count += 1
        result[target] = count
        count = 0

    return result

