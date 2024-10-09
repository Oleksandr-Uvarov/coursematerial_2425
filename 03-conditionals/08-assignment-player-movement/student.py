# write your code here
def player_movement(position, left_arrow, right_arrow, shift):
    position_change = 1
    if shift:
        position_change = 2

    if left_arrow:
        position -= position_change
    if right_arrow:
        position += position_change
    return position