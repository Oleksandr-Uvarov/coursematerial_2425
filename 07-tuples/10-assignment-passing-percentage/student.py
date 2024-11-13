# write your code here
def passing_percentage(grades):
    passing_grades = 0
    for grade in grades:
        if grade >= 10:
            passing_grades += 1

    return int(passing_grades / len(grades) * 100)