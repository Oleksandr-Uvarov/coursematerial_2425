def rpg2(n_sides, goal):
    count = 0
    total_number = n_sides * n_sides

    for dice_one in range(1, n_sides+1):
        for dice_two in range(1, n_sides+1):
            if dice_one + dice_two >= goal:
                count+=1
    return (count / total_number) * 100

def rpg3(n_sides, goal):
    count = 0
    total_number = n_sides * n_sides * n_sides
    for dice_one in range(1, n_sides+1):
        for dice_two in range(1, n_sides+1):
            for dice_three in range(1, n_sides+1):
                if dice_one + dice_two + dice_three >= goal:
                    count+=1


    return (count / total_number) * 100







        