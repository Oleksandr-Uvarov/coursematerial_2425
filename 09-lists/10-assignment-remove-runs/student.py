def remove_runs(ns):
    if len(ns) == 0 or len(ns) == 1:
        return ns
    
    if len(ns) == 2 and ns[0] == ns[1]:
        return ns[:1]
    length = len(ns) - 1
    
    stop = False
    while stop == False:
        # deleting loop
        for i in range(0, length):
            if ns[i] == ns[i+1]:
                ns.pop(i+1)
                length -= 1
                break
        
        # checking loop
        for i in range(0, length):
            if ns[i] == ns[i+1]:
                break
            if i == length - 1 and (ns[i] != ns[i+1]):
                stop = True


    return ns

    
    
print(remove_runs([1, 2]))
print(remove_runs([1, 2, 3, 3, 3, 4, 5, 6, 6, 7, 7, 7, 7, 1, 1, 9]))
print(remove_runs([5, 2, 2, 3, 3, 4, 4, 2, 2, 5, 5, 5, 2, 2, 2, 2]))
print(remove_runs([1, 2, 2, 2, 3, 2, 2]))


