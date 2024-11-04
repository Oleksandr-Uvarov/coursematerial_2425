# write your code here
def sum_input():
    number = -1
    sum = 0
    while number != 0:
        number = int(input("Enter integer: "))
        sum += number
    print(f"The sum equals {sum}.")