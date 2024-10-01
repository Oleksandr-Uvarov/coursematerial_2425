# write your code here
from math import floor
def cake4(eggs, flour, butter, sugar, eggs_per_cake, flour_per_cake, butter_per_cake, sugar_per_cake):
    min_eggs_flour = min(floor(eggs/eggs_per_cake), floor(flour/flour_per_cake))
    min_butter_sugar = min(floor(sugar/sugar_per_cake), floor(butter/butter_per_cake))

    return min(min_eggs_flour, min_butter_sugar)