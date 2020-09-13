# Problem Link: https://www.hackerrank.com/challenges/bigger-is-greater/problem
from itertools import permutations


def wordValuer(word):
    alphaDict = {'a': 1, 'b': 2, 'c': 3, 'e': 5, 'd': 4, 'g': 7, 'f': 6,
                 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12, 'o': 15,
                 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20,
                 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}
    total = 0
    for i in word:
        total += alphaDict[i]
    return total


def biggerIsGreater(word):
    permList = list(permutations(word))
    wordPerms = []
    wordValue = []
    for perm in permList:
        currentWord = ''.join(perm)
        wordPerms.append(currentWord)
        wordValue.append(wordValuer(currentWord))
    print(wordPerms)
    print(wordValue)


str1 = 'ab'
str2 = 'bb'
str3 = 'hefg'
str4 = 'dhck'
str5 = 'dkhc'

biggerIsGreater('abcd')
