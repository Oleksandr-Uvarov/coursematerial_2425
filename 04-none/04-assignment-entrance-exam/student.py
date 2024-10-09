def entrance_exam(grade1, grade2, grade3, grade4, grade5):
    grades = [grade1, grade2, grade3, grade4, grade5]
    

    tests_taken = 0
    for grade in grades:
        if grade is not None:
            tests_taken += 1


    i = 0
    for grade in grades:
        if grade is None:
            grades[i] = 0
        i += 1

    if tests_taken < 4:
        return False
    elif sum(grades) / tests_taken >= 12:
        return True
    return False
