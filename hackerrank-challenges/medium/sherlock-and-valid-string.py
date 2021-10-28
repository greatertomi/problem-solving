# Problem Link: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem


def isValid(string):
    strMap = {}
    for char in string:
        if char in strMap:
            strMap[char] += 1
        else:
            strMap[char] = 1
    values = list(strMap.values())
    mostOccurring = max(set(values), key=values.count)
    others = [x for x in values if x != mostOccurring]
    if len(others) == 0:
        return 'YES'
    elif len(others) > 1:
        return 'NO'
    elif others[0] - mostOccurring > 1:
        return 'NO'
    else:
        return 'YES'


string1 = 'a'
string2 = 'aabbcd'
string3 = 'aabbccddeefghi'
string4 = 'abcdefghhgfedecba'

print(isValid(string1))
# print(isValid(string2))
# print(isValid(string3))
# print(isValid(string4))

