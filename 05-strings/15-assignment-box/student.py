# write your code here
def box(string):
    length = len(string)

    first_line = f"+{(length+2)*"-"}+"
    second_line = f"| {string} |"
    third_line = f"+{(length+2)*"-"}+"

    return f"{first_line}\n{second_line}\n{third_line}"


print(box("x"))
print(box("xfwerfwefwe"))
print(box("x421421"))