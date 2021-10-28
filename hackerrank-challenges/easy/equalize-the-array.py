# Problem Link: https://www.hackerrank.com/challenges/equality-in-a-array/problem


def equalizeArray(arr):
    most_occurring = max(arr, key=arr.count)
    countVal = arr.count(most_occurring)
    return len(arr) - countVal


arr1 = [1, 2, 2, 3]
arr2 = [3, 3, 2, 1, 3]
print(equalizeArray(arr2))
