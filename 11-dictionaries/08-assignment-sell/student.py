def sell(stock, model):
    if stock[model] == 1:
        del stock[model]
    else:
        stock[model] -= 1