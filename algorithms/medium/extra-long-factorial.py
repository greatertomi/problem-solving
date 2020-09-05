# Problem Link: https://www.hackerrank.com/challenges/extra-long-factorials/problem


def factorial(num):
    fact = 1
    for i in range(num, 0, -1):
        fact *= i
    return fact


print(factorial(0))
