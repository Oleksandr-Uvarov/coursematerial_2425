# write your code here
def cake3(eggs, flour, butter, sugar):
    min_eggs_flour = min(eggs/5, flour/250)
    min_butter_sugar = min(butter/200, sugar/250)

    return min(min_eggs_flour, min_butter_sugar)