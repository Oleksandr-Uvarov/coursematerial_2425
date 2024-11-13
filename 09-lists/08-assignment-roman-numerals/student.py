def to_roman(x):
    year = ""

    thousands = 0
    hundreds = 0
    tens = 0
    ones = 0

    if len(str(x)) == 4:
        thousands = int(str(x)[0])
        hundreds = int(str(x)[1])
        tens = int(str(x)[2])
        ones = int(str(x)[3])
    elif len(str(x)) == 3:
        hundreds = int(str(x)[0])
        tens = int(str(x)[1])
        ones = int(str(x)[2])
    elif len(str(x)) == 2:
        tens = int(str(x)[0])
        ones = int(str(x)[1])
    else:
        ones = int(str(x)[0])




    # I 1
    # V 5 
    # X 10 
    # L 50
    # C 100
    # D 500
    # M 1000

    year += thousands * "M"
    
    if hundreds == 9:
        year += "CM"
    elif hundreds == 4:
        year += "CD"
    elif hundreds >= 5:
        year += "D" + ((hundreds-5) * "C")
    else:
        year += hundreds * "C"
    

    if tens == 9:
        year += "XC"
    elif tens == 4:
        year += "XL"
    elif tens >= 5:
        year += "L" + ((tens-5) * "X")
    else:
        year += tens * "X"

    if ones == 9:
        year += "IX"
    elif ones == 4:
        year += "IV"
    elif ones >= 5:
        year += "V" + ((ones-5) * "I")
    else:
        year += ones * "I"

    
        
    
    return year

def from_roman(string):
    year = 0

    if "CM" in string:
        year += 900
        index = string.find("CM")
        string = string[:index] + string[index+2:]

    if "CD" in string:
        year += 400
        index = string.find("CD")
        string = string[:index] + string[index+2:]

    if "XC" in string:
        year += 90
        index = string.find("XC")
        string = string[:index] + string[index+2:]

    if "XL" in string:
        year += 40
        index = string.find("XL")
        string = string[:index] + string[index+2:]


    if "IX" in string:
        year += 9
        index = string.find("IX")
        string = string[:index] + string[index+2:]


    if "IV" in string:
        year += 4
        index = string.find("IV")
        string = string[:index] + string[index+2:]



    for char in string:
        if char == "M":
            year += 1000
    for char in string:
        if char == "D":
            year += 500
    for char in string:
        if char == "C":
            year += 100
    for char in string:
        if char == "L":
            year += 50
    for char in string:
        if char == "X":
            year += 10
    for char in string:
        if char == "V":
            year += 5
    for char in string:
        if char == "I":
            year += 1


    return year






# string = "helloIIIIfwefew"
# if "IIII" in string:
#     index = string.find("IIII")
#     string = string[:index] + "IV" + string[index+len("IIII"):]


# integer = 42
# print(str(integer)[0])
# # print(string)









    # thousands = (x // 1000) * "M"
    # x -= 1000 * (x // 1000)

    # five_hundreds = (x // 500) * "D"
    # x -= 500 * (x // 500)

    # hundreds = (x // 100) * "C"
    # x -= 100 * (x // 100)

    # fifties = (x // 50) * "L"
    # x -= 50 * (x // 50)

    # tens = (x // 10) * "X"
    # x -= 10 * (x // 10)

    # fives = (x // 5) * "V"
    # x -= 5 * (x // 5)

    # ones = x * "I"


    # year = thousands + five_hundreds + hundreds + fifties + tens + fives + ones

    # year = year.replace("IIII", "IV")
    # year = year.replace("VIIII", "IX")
    # year = year.replace("XXXX", "XL")
    # year = year.replace("LXXXX", "XC")
    # year = year.replace("CCCC", "CD")
    # year = year.replace("DCCCC", "CM")

    # value = "DCCCC"
    # if value in year:
    #     index = year.find(value)
    #     year = year[:index] + "CM" + string[index+len(value)]

    # value = "CCCC"
    # if value in year:
    #     index = year.find(value)
    #     year = year[:index] + "CD" + string[index+len(value)]

    # value = "LXXXX"
    # if value in year:
    #     index = year.find(value)
    #     year = year[:index] + "XC" + string[index+len(value)]

    # value = "XXXX"
    # if value in year:
    #     index = year.find(value)
    #     year = year[:index] + "XL" + string[index+len(value)]

    # value = "VIIII"
    # if value in year:
    #     index = year.find(value)
    #     year = year[:index] + "IX" + string[index+len(value)]

    # value = "IIII"
    # if value in year:
    #     index = year.find(value)
    #     year = year[:index] + "IV" + string[index+len(value)]