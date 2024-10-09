# write your code here
def higher_card(card1, card2):
    if card2 == 1:
        return False
    elif card1 == 1:
        return True
    elif card1 > card2:
        return True
    return False