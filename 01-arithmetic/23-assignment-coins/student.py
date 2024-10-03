# write your code here
def coins(amount):
    coins_of_five = amount // 5
    if amount % 5 == 0:
        return coins_of_five
    else:
        coins_of_two = (amount - (coins_of_five * 5)) // 2
        if amount % 5 % 2 == 0:
            return coins_of_five + coins_of_two
        else:
            coins_of_one = amount - (coins_of_five * 5) - (coins_of_two * 2)


    return coins_of_five + coins_of_two + coins_of_one


