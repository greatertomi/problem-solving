# Problem Link: https://www.codewars.com/kata/51b6249c4612257ac0000005


def romanNumeralDecoder(string):
    romanDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    i = 0
    while i < len(string):
        try:
            if romanDict[string[i]] < romanDict[string[i + 1]]:
                total += romanDict[string[i + 1]] - romanDict[string[i]]
                i += 2
            else:
                total += romanDict[string[i]]
                i += 1
        except IndexError:
            total += romanDict[string[i]]
            break
    return total


string1 = 'XXI'  # 21
string2 = 'I'  # 1
string3 = 'IV'  # 4
string4 = 'MMVIII'  # 2008
string5 = 'MDCLXVI'  # 1666

print(romanNumeralDecoder(string5))
