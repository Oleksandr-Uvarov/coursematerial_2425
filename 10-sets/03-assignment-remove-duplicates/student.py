def remove_duplicates(xs):
    lst = []
    set_xs = set()
    for item in xs:
        if item not in set_xs:
            set_xs.add(item)
            lst.append(item)
    return lst