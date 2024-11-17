from math import floor

def cake(stock, recipe_ingredients):
    number_of_cakes = []


    for key, value in recipe_ingredients.items():
        if key in stock:
            number_of_cakes.append(floor(stock[key] / value))
        else:
            return 0

    return min(number_of_cakes)


