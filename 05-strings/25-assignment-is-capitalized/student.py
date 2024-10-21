# write your code here
def is_capitalized(string):
    if string == "":
        return False
    
    capitalized_string = string[0].upper() + string[1:].lower()

    return capitalized_string == string

print(is_capitalized("AbcdeF"))