# Problem Link: https://www.hackerrank.com/challenges/lilys-homework/problem
import itertools


def lilysHomework(arr):
    minArr = None
    minNum = None
    # print(arr[2:] + arr[:2])
    perms = list(itertools.permutations(arr))
    for perm in perms:
        diff = None
        for i in range(len(perm)):
            diff = sum([abs(perm[i] - perm[i - 1]) for i in range(1, len(perm))])
            if minNum is None:
                minNum = diff
                minArr = perm
            elif diff <= minNum:
                minNum = diff
                minArr = perm
        print(perm, diff, minArr)
    misplaced = 0
    for i in range(len(arr)):
        if arr[i] != minArr[i]:
            misplaced += 1
    print(misplaced)
    return misplaced//2

    # print(diff)


arr1 = [7, 15, 12, 3]
arr2 = [2, 5, 3, 1]
print(lilysHomework(arr2))

