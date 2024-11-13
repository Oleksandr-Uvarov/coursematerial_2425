# write your code here
def domino_chain(dominos):
    for index in range (0, len(dominos) - 1):
        if dominos[index][1] != dominos[index+1][0]:
            return False
    return True
