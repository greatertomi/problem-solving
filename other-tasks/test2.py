import math


def function(str1, str2):
    common = ''
    diff = ''
    combined = list(set(str1 + str2))
    for char in combined:
        if char in str1 and char in str2:
            common += char
        else:
            diff += char

    totalDiff = 0
    for i in diff:
        val = str1.count(i) + str2.count(i)
        totalDiff += val
    for i in common:
        val = abs(str1.count(i) - str2.count(i))
        totalDiff += val
    return totalDiff


print(function('at', 'cat'))
print(function('boat', 'got'))
print(function('thought', 'sloughs'))

