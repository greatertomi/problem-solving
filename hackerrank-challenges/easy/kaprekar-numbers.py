# Problem Link: https://www.hackerrank.com/challenges/kaprekar-numbers/problem
import math
import re


def checkKaprekarStatus(num):
    squareNum = str(num ** 2)
    movNum = int(len(squareNum) / 2)
    numsArr = [squareNum[:movNum], squareNum[movNum:]]

    if num != 1 and not bool(re.match('^(?!0*$).*$', numsArr[1])):
        return False

    if numsArr[1] == '':
        numsArr[1] = 0
    elif numsArr[0] == '':
        numsArr[0] = 0

    return int(numsArr[0]) + int(numsArr[1]) == num


def kaprekarNumbers(p, q):
    nums = []
    for num in range(p, q + 1):
        if checkKaprekarStatus(num):
            nums.append(num)
    if len(nums) == 0:
        print('INVALID RANGE')
    else:
        print(*nums, end=' ')


kaprekarNumbers(400, 700)
# print(checkKaprekarStatus(1))
