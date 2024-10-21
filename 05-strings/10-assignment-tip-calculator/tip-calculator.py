# write your code here
def main():
    total_price = int(input("Enter total price: "))
    tip = input("Enter int percentage (default is 20): ")
    if tip == "":
        tip = 20
    else:
        tip = int(tip)
    print("You have to pay" + str(total_price + (total_price / 100 * tip)))


if __name__ == "__main__":
    main()