# write your code here
def middle(a, b, c):
 
    ab_max = max(a, b)
    bc_max = max(b, c)
    ac_max = max(a, c)

    return min(ab_max, bc_max, ac_max)

    


