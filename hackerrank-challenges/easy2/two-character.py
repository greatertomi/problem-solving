# Problem Link: https://www.hackerrank.com/challenges/two-characters/problem


def uniqueCharacter(string):
    uniqueStr = ''
    uniqueArr = []
    for char in string:
        if char not in uniqueStr:
            uniqueStr += char
    for i in range(len(uniqueStr)):
        for k in range(i+1, len(uniqueStr)):
            newString = ''
            newString += uniqueStr[i]
            newString += uniqueStr[k]
            uniqueArr.append(newString)
    return uniqueArr


def checkForAlternating(string):
    if string[0] == string[1]:
        return False
    char1 = string[0]
    char2 = string[1]
    for i in range(len(string)):
        if i % 2 == 0 and string[i] != char1:
            return False
        if i % 2 == 1 and string[i] != char2:
            return False
    return True


def twoCharacters(string):
    uniques = uniqueCharacter(string)
    possibleAlternates = []
    for unq in uniques:
        tempAlt = ''
        for char in string:
            if char == unq[0] or char == unq[1]:
                tempAlt += char
        if checkForAlternating(tempAlt):
            possibleAlternates.append(tempAlt)
    if len(possibleAlternates) == 0:
        return 0
    return max(possibleAlternates, key=len)


string1 = 'beabeefeab'
string2 = 'abaacdabd'
string3 = 'asdcbsdcagfsdbgdfanfghbsfdab'
string4 = 'asvkugfiugsalddlasguifgukvsa'
print(twoCharacters(string4))
