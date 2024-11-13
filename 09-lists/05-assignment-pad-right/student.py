def pad_right(xs, length, padding):
    length_xs = len(xs)

    if length_xs >= length: 
        return xs
    else:
        times_to_add_padding = length - length_xs
        for i in range (0, times_to_add_padding):
            xs.append(padding)
    return xs