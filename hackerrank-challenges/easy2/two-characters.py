# Problem Link: https://www.hackerrank.com/challenges/two-characters/problem
# Todo


def uniqueCharacters(string):
    newString = ''
    newStringArr = []
    for char in string:
        if char not in newString:
            newString += char
    for i in range(len(newString)):
        for j in range(i+1, len(newString)):
            newStringArr.append([newString[i], newString[j]])
    return newStringArr


def possibleAlternates(string, arr):
    alternates = []
    for i in arr:
        for char in string:
            pass


def twoCharacter(string):
    pass


string1 = 'abaacdabd'
string2 = 'beabeefeab'
print(uniqueCharacters(string1))
