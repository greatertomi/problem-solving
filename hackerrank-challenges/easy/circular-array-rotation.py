# Problem Link: https://www.hackerrank.com/challenges/circular-array-rotation/problem


def circularArrayRotation(a, k, queries):
    aLen = len(a)
    point = k % aLen
    a = a[-point:] + a[:-point]
    results = []

    for q in queries:
        results.append(a[q])

    return results


arr1 = [1, 2, 3, 4, 5, 6]
k1 = 14
queries1 = [0, 1, 2]
print(circularArrayRotation(arr1, k1, queries1))
