# Problem Link: https://www.hackerrank.com/challenges/string-construction/problem


def stringConstruction(string):
    newString = ''
    cost = 0
    for char in string:
        if char not in newString:
            newString += char
            cost += 1
    return cost


string1 = 'abcabc'
string2 = 'abcd'
string3 = 'abab'
stringConstruction(string1)
stringConstruction(string2)
stringConstruction(string3)
