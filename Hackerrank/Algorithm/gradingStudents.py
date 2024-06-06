
def gradingStudents(grades):
    result = []
    for grade in grades:
        if grade < 38 or grade % 5 < 3:
            result.append(grade)
        else:
            result.append(grade + (5 - grade % 5))
    return result
