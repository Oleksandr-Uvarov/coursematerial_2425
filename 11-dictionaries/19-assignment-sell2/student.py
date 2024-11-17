def sell2(stock, model, size):
    if model not in stock:
        return False
    
    if size not in stock[model]:
        return False
    else:
        for shoe_size in stock[model]:
            if shoe_size == size:
                if stock[model][shoe_size] == 1:
                    del stock[model][shoe_size]
                    break
                else:
                    stock[model][shoe_size] -= 1
                    break

    if len(stock[model]) == 0:
        del stock[model]

    print(stock)
    return True
            














stock = {
    'New Balance 530': {44: 2, 45: 3, 47: 1},
    'Converse Chuck Taylor All Star 70 Hi': {39: 2, 40: 1, 43: 4, 44: 2},
    'Air Jordan 1 Retro': {46: 1},
    'Nike Air Max Tuned 1': {44: 2, 45: 1},
    'Adidas Superstar': {41: 2, 43: 2, 45: 1, 47: 3},
    'Vans Classic Slip-on Checkered': {43: 1}
}

print(sell2(stock, 'Vans Classic Slip-on Checkered', 43))
print(sell2(stock, 'Vans Classic Slip-on Checkered', 43))
