# Problem Link: https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python


def countCharacter(string):
    stringDict = {}
    for char in string:
        if char in stringDict:
            stringDict[char] += 1
        else:
            stringDict[char] = 1
    return stringDict


print(countCharacter(''))
