# write your code here
def all_different(xs):
    for index in range (0, len(xs)):
        for index_two in range (1, len(xs)):
            if xs[index] == xs[index_two] and index != index_two:
                return False
    return True
