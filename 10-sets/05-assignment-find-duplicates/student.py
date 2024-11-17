def find_duplicates(xs):
    xs_set = set()
    xs_set_duplicates = set()
    for item in xs:
        if item not in xs_set:
            xs_set.add(item)
        else:
            xs_set_duplicates.add(item)

    lst = list(xs_set_duplicates)
    return lst