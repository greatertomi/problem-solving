# Problem Link: https://www.hackerrank.com/challenges/grading/problem


def gradeCalculator(grade):
    if grade < 38:
        return grade
    extra = 5 - (grade % 5)
    if extra < 3:
        return grade + extra
    return grade


def gradingStudents(grades):
    result = []
    for i in grades:
        result.append(gradeCalculator(i))
    return result


nums = [84, 29, 73, 67, 38, 33]
print(gradingStudents(nums))
