# write your code here
def matches_pattern(pattern, string):
    if len(pattern) > len(string) or len(pattern) < len(string):
        return False
    

    code = {}

    for i in range(0, len(pattern)):
        if pattern[i] in code.keys():
            if code[pattern[i]] != string[i]:
                return False
        else: 
            code[pattern[i]] = string[i]

    if len(set(code.values())) < len(list(code.values())):
        return False

    

    return True


print(matches_pattern("AB", "XX"))
print(matches_pattern("XXXYYY", "AAAAAA"))