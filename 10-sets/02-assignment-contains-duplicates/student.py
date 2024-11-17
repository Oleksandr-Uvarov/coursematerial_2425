def contains_duplicates(xs):
    xs_set = set()
    for item in xs:
        if item not in xs_set:
            xs_set.add(item)
        else:
            return True
    return False