def combine(d1, d2):
    d3 = {}

    for key, value in d1.items():
        if value in d2.keys():
            d3[key] = d2[value]
            # d3[key] = d2.get(value)
    return d3