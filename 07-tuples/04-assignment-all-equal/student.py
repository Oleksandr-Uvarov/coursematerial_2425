# write your code here
def all_equal(xs):
    if len(xs) == 0:
        return True
    
    first = xs[0]
    for element in xs:
        if element == first:
            continue
        else:
            return False
    return True