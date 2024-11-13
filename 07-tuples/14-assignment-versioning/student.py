# write your code here
def increase_version(version, breaking_change, new_features):
    if breaking_change:
        return (version[0]+ 1, 0, 0)
    elif new_features:
        return(version[0], version[1]+1, 0)
    else:
        return(version[0], version[1], version[2] + 1)
    
def is_more_recent(v1, v2):
    if v1[0] > v2[0]:
        return True
    elif v1[0] == v2[0] and v1[1] > v2[1]:
        return True
    elif v1[0] == v2[0] and v1[1] == v2[1] and v1[2] > v2[2]:
        return True
    else:
        return False

def is_older(v1, v2):
    if v1[0] < v2[0]:
        return True
    elif v1[0] == v2[0] and v1[1] < v2[1]:
        return True
    elif v1[0] == v2[0] and v1[1] == v2[1] and v1[2] < v2[2]:
        return True
    else:
        return False