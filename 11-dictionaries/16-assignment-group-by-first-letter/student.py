def group_by_first_letter(strings):
    letters = []

    grouped_names = {}


    for string in strings:
        if string[0].upper() not in letters:
            letters.append(string[0].upper())


    for letter in letters:
        names = []
        for string in strings:
            if string[0].upper() == letter:
                names.append(string)
        grouped_names[letter] = names


    return grouped_names