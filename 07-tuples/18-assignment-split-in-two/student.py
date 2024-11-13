# write your code here
def split_in_two(xs):
    length = len(xs)
    if length % 2 == 0:
        return (xs[0:int(length/2)], xs[int(length/2):])
    else:
        return (xs[0:int(length/2 + 1)], xs[int(length/2) + 1:])
    

print(split_in_two((1, 2, 3, 4)))
print(split_in_two((1, 2, 3, 4, 5)))