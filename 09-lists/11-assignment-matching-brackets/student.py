def matching_brackets(string):
    count_left_round = 0
    count_left_curly = 0
    count_left_square = 0
    count_right_round = 0
    count_right_curly = 0
    count_right_square = 0
    
    for i in range(0, len(string) - 1):
        if string[i] == "(" and (string[i+1] == "}" or string[i+1] == "]"): 
            return False
        elif string[i] == "{" and (string[i+1] == ")" or string[i+1] == "]"): 
            return False
        elif string[i] == "[" and (string[i+1] == "}" or string[i+1] == ")"): 
            return False
        
    for char in string:
        if count_right_round > count_left_round or count_right_curly > count_left_curly or count_right_square > count_left_square:
            return False
        if char == "(":
            count_left_round += 1
        if char == "{":
            count_left_curly += 1
        if char == "[":
            count_left_square+= 1
        if char == ")":
            count_right_round += 1
        if char == "}":
            count_right_curly += 1
        if char == "]":
            count_right_square += 1

    
    if count_left_round != count_right_round or count_left_curly != count_right_curly or count_left_square != count_right_square:
        return False
    return True

print(matching_brackets("([)]"))

"([(]))"