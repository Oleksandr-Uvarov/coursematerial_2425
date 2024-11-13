def compact(xs):
    new_list = []
    for value in xs:
        if value is not None:
            new_list.append(value)

    return new_list


def compact_in_place(xs):
    while None in xs:
        xs.remove(None)


lst = [None, None]

print(compact(lst))

compact_in_place(lst)

print(lst)