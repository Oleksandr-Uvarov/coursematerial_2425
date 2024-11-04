def invest(amount, rate, goal):
    number = amount
    years = 0
    
    while number < goal:
        years += 1
        number = number * (rate+100)/100
        # number += number * (rate/100)

    return years

