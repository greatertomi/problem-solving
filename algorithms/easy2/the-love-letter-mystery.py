# Problem Link: https://www.hackerrank.com/challenges/the-love-letter-mystery/problem


def getLetterIndex(letter):
    alphaDict = {'a': 1, 'b': 2, 'c': 3, 'e': 5, 'd': 4, 'g': 7, 'f': 6,
                 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12, 'o': 15,
                 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20,
                 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}
    return alphaDict[letter]


def theLoveLetterMystery(string):
    total = 0
    for i in range(0, len(string)//2):
        count = abs(getLetterIndex(string[i]) - getLetterIndex(string[-(i+1)]))
        total += count
    print(total)


string1 = 'abc'
string2 = 'abcba'
string3 = 'abcd'
string4 = 'cba'
string5 = 'abcdefghijk'
theLoveLetterMystery(string1)
theLoveLetterMystery(string2)
theLoveLetterMystery(string3)
theLoveLetterMystery(string4)
