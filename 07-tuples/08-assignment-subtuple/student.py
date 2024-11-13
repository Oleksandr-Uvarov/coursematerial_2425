# write your code here
def subtuple(xs, ys):
    if len(ys) == 0:
        return True
    if len(xs) == 0 and len(ys) != 0:
        return False
    
    first = ys[0]
    length = len(ys)

    if first in xs:
        first_xs = xs.index(first)
        
        i = 0
        for item in ys:
            if item == xs[first_xs+i]:
                i += 1
                continue
            return False
    return True



    #     subtuple = xs[xs.index(first):length]
    #     if subtuple == ys:
    #         return True
    # return False




print(subtuple((1, 2, 3), (1, 2)))