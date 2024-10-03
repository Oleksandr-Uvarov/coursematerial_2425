# write your code here
def leftover_candy(candy_count, child_count):
    if candy_count < child_count:
        return candy_count
    
    leftover_amount = candy_count % child_count

    return leftover_amount