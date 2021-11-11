# Problem Link: https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python


def countBit(num):
    binary = [x for x in bin(num)]
    return len(list(filter(lambda x: x == '1', binary)))


value1 = 1234
print(countBit(value1))
