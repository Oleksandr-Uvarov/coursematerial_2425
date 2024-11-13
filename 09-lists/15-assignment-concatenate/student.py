def concatenate(xs, ys):
    if len(ys) == 0:
        return xs
        
    for element in ys:
        xs.append(element)

