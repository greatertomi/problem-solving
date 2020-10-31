# Problem Link: https://www.hackerrank.com/challenges/camelcase/problem


def camelCase(word: str):
    count = 1
    for i in word:
        if i.isupper():
            count += 1
    return count


word1 = 'saveChangesInTheEditor'
print(camelCase(word1))
