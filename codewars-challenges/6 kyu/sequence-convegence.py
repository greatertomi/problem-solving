# Problem Link: https://www.codewars.com/kata/59971e64bfccc70748000068
from functools import reduce


def generateSequence(num):
    array = [num]
    for i in range(2000):
        currentNum = array[-1]
        if currentNum < 10:
            array.append(2 * currentNum)
        else:
            digits = [int(x) for x in str(currentNum) if x != '0']
            total = reduce(lambda x, y: x * y, digits)
            array.append(currentNum + total)
    return array


def sequenceConvergence(num):
    base_series = generateSequence(1)
    test_series = generateSequence(num)
    point = 0
    for i in range(len(test_series)):
        if test_series[i] in base_series:
            point = i
            break
    return len(test_series[:point])


# generateSequence(3)
print(sequenceConvergence(5000))
