# write your code here
def tip_calculator():
    total_price = int(input("Enter total price: "))
    tip = input("Enter int percentage (default is 20): ")
    if tip == "":
        tip = 20
    else:
        tip = int(tip)
    print("You have to pay " + str(round(total_price + (total_price / 100 * tip))))