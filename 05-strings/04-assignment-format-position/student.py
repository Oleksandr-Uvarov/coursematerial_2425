from math import floor
# write your code here
def format_position(x, y):

    return f"({round(x, 3):.3f}, {round(y, 3):.3f})"
    
#     x_int = int(x)
#     y_int = int(y)

#     x_dot_index = find_dot_index(x)
#     y_dot_index = find_dot_index(y)
#     print(x_dot_index)

#     numbers_after_dot_x = str(x)[x_dot_index+1:x_dot_index+4]
#     numbers_after_dot_y = str(y)[y_dot_index+1:y_dot_index+4]

#     if x_dot_index == -1:
#         numbers_after_dot_x = 0

#     if y_dot_index == -1:
#         numbers_after_dot_y = 0

#     return f"({x_int}.{numbers_after_dot_x:03}, {y_int}.{numbers_after_dot_y:03})"


# def find_dot_index(number):
#     number_str = str(number)
#     dot_index = number_str.find(".")

#     return dot_index


# print(format_position(2.000, 3.000))
# print(format_position(2.200, 3.300))
# print(format_position(2.254, 3.323))
# print(format_position(2.287, 3.312))

# print(format_position(2.28, 3.392))
# print(format_position(2.207, 3.35))

# print(format_position(-87.100, 545.785))
# print(format_position(-88.1, 545.784))
print(format_position(2, 3))


print(round(3.1, 3))
