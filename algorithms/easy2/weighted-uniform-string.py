# Problem Link: https://www.hackerrank.com/challenges/weighted-uniform-string/problem
from collections import Counter


def weightedUniformStrings(string, queries):
    strArr = list(set(string))
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    charWeights = []
    for char in strArr:
        count = string.count(char)
        index = alphabets.index(char) + 1
        charWeights += [index * x for x in range(1, count + 1)]

    returnArr = []
    for query in queries:
        if query in charWeights:
            returnArr.append('Yes')
        else:
            returnArr.append('No')
    return returnArr


# Better Solution
def weightedUniformStrings2(string, queries):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    weights = dict(zip(alphabet, range(1, 27)))
    found = Counter()

    current_letter = string[0]
    count = 1
    found[weights[current_letter] * count] = True
    for c in string[1:]:
        if c == current_letter:
            count += 1
        else:
            count = 1
            current_letter = c
        found[weights[current_letter] * count] = True

    for q in queries:
        yield "Yes" if found[q] else "No"


string1 = 'abccddde'
query1 = [1, 3, 12, 5, 9, 10]
string2 = 'aaabbbbcccddd'
query2 = [9, 7, 8, 12, 5]
print(weightedUniformStrings(string2, query1))
print(weightedUniformStrings2(string2, query1))
# getArrayWeight(string1)

