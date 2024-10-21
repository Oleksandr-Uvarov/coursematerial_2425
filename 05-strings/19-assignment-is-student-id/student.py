# write your code here
def is_student_id(string):
    if len(string) != 8:
        return False
    
    if not (string[0].lower() == "r" or string[0].lower() == "s"):
        return False
    
    for char in string[1:]:
        if char not in "0123456789":
            return False
        
    return True