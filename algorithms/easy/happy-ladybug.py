# Problem Link: https://www.hackerrank.com/challenges/happy-ladybugs/problem


def happyLadyBug(values):
    valDict = {}
    for val in values:
        if val != '_':
            if val in valDict:
                valDict[val] += 1
            else:
                valDict[val] = 1
    if '_' not in values:
        return 'NO'
    elif 1 in valDict.values():
        return 'NO'
    print(valDict)
    return 'YES'


def happyLadyBug2(values):
    valLen = len(values)
    for val in values:
        if val != '_' and values.count(val) == 1:
            return 'NO'

    if values.count('_') == 0:
        for i in range(1, valLen - 1):
            if values[i-1] != values[i] and values[i+1] != values[i]:
                return 'NO'
    return 'YES'


print(happyLadyBug2('_'))
print(happyLadyBug2('RBRB'))
print(happyLadyBug2('RRRR'))
print(happyLadyBug2('BBB'))
print(happyLadyBug2('BBB_'))

