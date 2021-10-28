# Problem Link: https://www.hackerrank.com/challenges/picking-numbers/problem


def pickingNumbers(arr):
    numbers = list(set(arr))
    maxCount = 0
    for i in numbers:
        count = 0
        for k in arr:
            if k >= i and abs(i - k) <= 1:
                count += 1
            if count > maxCount:
                maxCount = count
    return maxCount


arr1 = [1, 1, 2, 2, 4, 4, 5, 5, 5]
arr2 = [4, 6, 5, 3, 3, 1]
arr3 = [1, 2, 2, 3, 1, 2]
print(pickingNumbers(arr3))

