# write your code here
def thanos(queue_size, target_size):
    number = queue_size
    snaps = 0

    while number > target_size:
        number = number // 2
        snaps += 1
    return snaps
