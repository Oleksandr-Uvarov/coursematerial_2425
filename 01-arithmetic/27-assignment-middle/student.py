# write your code here
def middle(a, b, c):
    a_or_b_min = min(a, b)
    b_or_c_min = min(b, c)

    abc_min = min(a_or_b_min, b_or_c_min)

    lowest_number = abc_min

    
    a_or_b_max = max(a, b)
    b_or_c_max = max(b, c)

    abc_max = max(a_or_b_max, b_or_c_max)

    
    









    return str(abc_min) + " " + str(abc_max)

    


    # put them in a sort of sorted list without using a list

    
        

print(middle(4, 4, 4))
print(middle(7, 4, 5))
print(middle(4, 5, 5))
print(middle(5, 6, 4))