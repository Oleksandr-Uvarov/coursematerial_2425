def remove_backspaces(string):
    # if string != "" and string[0] == "\\" and string[1] == "b":
    if string != "" and string[0] == "\b":
        return ""
    
    while "\x08" in string:
        for index in range(0, len(string)):
            if string[index] == "\x08":
                string = string[:index-1] + string[index+1:]
                break
    return string





# print(remove_backspaces("abc\\b\\b"))
# print(remove_backspaces("13\\b2356\\b\\b45677\\b8990\\b\\b0"))


print(remove_backspaces("\b"))

# print(remove_backspaces(""))
# print(remove_backspaces("a"))
# print(remove_backspaces("\\b"))
# print(remove_backspaces("a\\b"))
# print(remove_backspaces("abc"))
# print(remove_backspaces("abc\\b"))
# print(remove_backspaces("a\\bb\\bc\\b"))
# print(remove_backspaces("aa\\bb\\bc\\b"))
# print(remove_backspaces("a\\bb\\bc\\bc"))
# print(remove_backspaces("aa\\bb\\bc\\bc"))
# print(remove_backspaces("aa\\bb\\bc\\bbc"))
# print(remove_backspaces("\\b"))


# print((len("abc\\b\\b")))
# print("a\b")
# print("Hello\b World")


