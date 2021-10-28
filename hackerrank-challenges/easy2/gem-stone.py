# Problem Link: https://www.hackerrank.com/challenges/gem-stones/problem


def gemStones(arr):
    gemDict = {}
    for val in arr:
        newStr = list(set(val))
        for num in newStr:
            if num in gemDict:
                gemDict[num] += 1
            else:
                gemDict[num] = 1
    return list(gemDict.values()).count(len(arr))


arr1 = ['abc', 'bcd', 'bc']
arr2 = ['abcdde', 'baccd', 'eeabg']
print(gemStones(arr1))
print(gemStones(arr2))
