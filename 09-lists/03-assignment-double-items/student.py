def double_items(ns):
    for i in range (0, len(ns)):
        ns[i] *= 2
    return ns


print(double_items([0, 1, 2, 3]))