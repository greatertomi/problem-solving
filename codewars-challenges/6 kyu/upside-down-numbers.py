# Problem Link: https://www.codewars.com/kata/59f7597716049833200001eb/train/python


def isStrobogrammatic(number):
    number = str(number)
    valid_nums = ['0', '1', '8']
    checker = ['6', '9']
    countValid = 0
    countChecker = 0
    invalid = False
    for val in number:
        if val in valid_nums:
            countValid += 1
        elif val in checker:
            countChecker += 1
        else:
            return False

    if countValid > 0:
        if countChecker == 0 and len(number) == 1:
            return True
        else:
            if number == number[0] * len(number):
                return True
            else:
                return False
    else:
        if len(number) > 1:
            convertedNum = str(number).replace('9', '6')
            if convertedNum == convertedNum[::-1]:
                if number == number[0] * len(number):
                    return False
                else:
                    return True
            else:
                return False
        return False


def checkUpsideDown(start, end):
    count = 0
    for i in range(start, end):
        if isStrobogrammatic(i):
            print(i)
            count += 1
    print(count)


# print(checkUpsideDown(100, 1000))
