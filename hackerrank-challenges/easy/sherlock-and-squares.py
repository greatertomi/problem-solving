# Problem Link: https://www.hackerrank.com/challenges/sherlock-and-squares/problem
import math


def is_square(num):
    return num == int(math.sqrt(num))**2


def squares(a, b):
    sqrtA = math.ceil(math.sqrt(a))
    sqrtB = math.floor(math.sqrt(b))

    return sqrtB - sqrtA + 1


print(squares(17, 24))
# print(is_square(34))
