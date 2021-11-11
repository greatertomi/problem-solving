# Problem Link: https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec
import math
from functools import reduce
import operator


def persistence(num):
    count = 0
    while num > 10:
        num = math.prod([int(x) for x in str(num)])
        count += 1
    return count

def persistence2(num):
    count = 0
    while num >= 10:
        num = reduce(operator.mul, [int(x) for x in str(num)], 1)
        count += 1
    return count


value1 = 39
value2 = 999
value3 = 25
print(persistence2(value1))
print(persistence2(value2))
print(persistence2(value3))
