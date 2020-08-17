# Problem Link: https://www.hackerrank.com/challenges/counting-valleys/problem


def countingValleys(steps):
    seaLevel = valley = 0
    for step in steps:
        if step == 'U':
            seaLevel += 1
        else:
            seaLevel -= 1

        if step == 'U' and seaLevel == 0:
            valley += 1
    return valley


arr1 = 'DDUUUUDD'
arr2 = 'UDDDUDUU'
arr3 = 'UDUUUDUDDD'
print(countingValleys(arr3))
