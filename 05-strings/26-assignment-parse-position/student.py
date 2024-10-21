def parse_position_x(string):
    comma_index = string.find(",")

    number = string[1:comma_index]

    return float(number)
    
def parse_position_y(string):
    comma_index = string.find(",")

    number = string[comma_index+2:len(string)-1]

    return float(number)

string = "(12.453, 9.120)"

print(parse_position_x(string))
print(parse_position_y(string))
