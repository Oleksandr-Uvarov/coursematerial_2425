def inverse_lookup(dictionary, value):
    if dictionary is None:
        return None
    
    keys = []

    for key in dictionary.keys():
        if dictionary.get(key) == value:
            keys.append(key)


    return keys