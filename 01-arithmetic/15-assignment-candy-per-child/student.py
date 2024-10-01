# write your code here
def candy_per_child(candy_count, child_count):
    if (candy_count % child_count == 0):
        return candy_count / child_count
    else:
        return (candy_count - (candy_count % child_count)) / child_count

