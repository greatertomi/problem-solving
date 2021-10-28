# Problem Link: https://www.hackerrank.com/challenges/minimum-distances/problem


def minimumDistance(arr):
    uniqueArr = list(set(arr))
    diff = []
    for num in uniqueArr:
        indices = [i for i, x in enumerate(arr) if x == num]
        try:
            diff.append(abs(indices[0] - indices[1]))
        except IndexError:
            continue
    if len(diff) == 0:
        return -1
    return min(diff)


arr1 = [3, 2, 1, 2, 3]
arr2 = [7, 1, 3, 4, 1, 7]
arr3 = [1, 2, 3, 4, 10]
print(minimumDistance(arr3))
