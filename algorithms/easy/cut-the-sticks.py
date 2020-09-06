# Problem Link: https://www.hackerrank.com/challenges/cut-the-sticks/problem


def cutTheSticks(arr):
    arrLen = len(arr)
    results = []
    while arrLen > 0:
        results.append(arrLen)
        minVal = min(arr)
        arr = [a - minVal for a in arr if a - minVal > 0]
        arrLen = len(arr)
    return results


sticks1 = [1, 2, 3]
sticks2 = [5, 4, 4, 2, 2, 8]
sticks3 = [1, 2, 3, 4, 3, 3, 2, 1]
print(cutTheSticks(sticks3))
