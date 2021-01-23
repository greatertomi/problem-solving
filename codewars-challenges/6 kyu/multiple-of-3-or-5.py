# Problem Link: https://www.codewars.com/kata/514b92a657cdc65150000006/train/python


def countMultiple(num):
    total = 0
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total


print(countMultiple(10))
