def remove_backspaces(string):
    index = 0
    for char in string:
        if char == "\\" and string[index+1] == "b":
            string = string[0:index-1] + string[index+2:]
        index += 1
    return string


print(remove_backspaces("abc\\b\\b"))