# Problem Link: https://www.codewars.com/kata/618688793385370019f494ae
import math


def distanceBetweenTwoPoints(pointA, pointB):
    valueA = (pointB[1] - pointA[1]) ** 2
    valueB = (pointB[0] - pointA[0]) ** 2
    return math.sqrt(valueA + valueB)


def isSquare(points):
    if len(points) < 4:
        return False

    result1 = distanceBetweenTwoPoints(points[0], points[1])
    result2 = distanceBetweenTwoPoints(points[1], points[2])
    result3 = distanceBetweenTwoPoints(points[2], points[3])
    result4 = distanceBetweenTwoPoints(points[3], points[0])
    print(result1, result2, result3, result4)
    if result1 == result2 == result3 == result4 == 0:
        return False
    return result1 == result2 == result3 == result4


value1 = ((1, 1), (3, 3), (1, 3), (3, 1))
value2 = ((0, 0), (0, 2), (2, 0), (2, 1))
value3 = ((0, 2), (0, -2), (1, 0), (-1, 0))
value4 = ((2, 6), (5, 1), (0, -2), (-3, 3))
value5 = ((0, 0), (0, 0), (0, 0), (0, 0))
value6 = ((1, 1), (3, 3), (1, 3), (3, 1))
value7 = [(0, 0), (0, 0), (2, 0), (2, 0)]
# print(isSquare(value1))
# print(isSquare(value2))
# print(isSquare(value3))
print(isSquare(value7))
