# write your code here
def split_name(name):
    for index in range(0, len(name)):
        if name[index] == " ":
            tuple_name = (name[:index], name[index+1:])
            return tuple_name
    
