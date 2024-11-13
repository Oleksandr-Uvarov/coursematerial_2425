from collections import namedtuple
Color = namedtuple("Color", ["r", "g", "b"])

color = Color(50, 90, 150)

def valid_color(color):
    for value in color:
        if value > 255 or value < 0:
            return False
    return True

def clamp_color(color):
    red = color.r
    green = color.g
    blue = color.b

    if red < 0:
        red = 0
    elif red > 255:
        red = 255

    if green < 0:
        green =  0
    elif green > 255:
        green = 255

    if blue < 0:
        blue = 0
    elif blue > 255:
        blue = 255

    return Color(red, green, blue)
