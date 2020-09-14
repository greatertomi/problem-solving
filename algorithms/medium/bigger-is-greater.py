# Problem Link: https://www.hackerrank.com/challenges/bigger-is-greater/problem
from itertools import permutations


def biggerIsGreater(word):
    permList = list(permutations(word))
    wordPerms = []
    for perm in permList:
        currentWord = ''.join(perm)
        wordPerms.append(currentWord)
    wordPerms = list(set(wordPerms))
    wordPerms.sort()
    try:
        biggerWord = wordPerms[wordPerms.index(word) + 1]
    except IndexError:
        biggerWord = 'no answer'

    return biggerWord


str1 = 'a'
str2 = 'bb'
str3 = 'hefg'
str4 = 'dhck'
str5 = 'dkhc'

print(biggerIsGreater(str5))
