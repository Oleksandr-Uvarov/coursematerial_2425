# write your code here
def increasing(ns):
    for index in range (0, len(ns) - 1):
        if ns[index+1] >= ns[index]:
            continue
        return False
    return True