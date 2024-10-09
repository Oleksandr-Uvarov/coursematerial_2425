# write your code here
def total_cost(amount):
    if amount < 100:
        return amount + 10
    if amount >= 200:
        return amount * 0.95
    return amount