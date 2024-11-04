def valid_parentheses(string):
    count_left = 0
    count_right = 0
    for char in string:
        if count_right > count_left:
            return False
        if char == "(":
            count_left += 1
        if char == ")":
            count_right += 1
    
    if count_left != count_right:
        return False
    return True