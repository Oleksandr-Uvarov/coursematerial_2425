# write your code here
def empty_seats(used_seats):
    if len(used_seats) == 0:
        return 0
    if len(used_seats) == 1:
        return 0
    
    nr_empty_seats = 0
    for index in range(0, len(used_seats) - 1):
        nr_empty_seats += used_seats[index+1] - used_seats[index] - 1

    return nr_empty_seats

