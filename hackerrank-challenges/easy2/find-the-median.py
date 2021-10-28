# Problem Link: https://www.hackerrank.com/challenges/find-the-median/problem


def findMedian(arr):
    arr.sort()
    median = arr[len(arr)//2]
    return median


arr1 = [1, 2, 3, 4, 5]
arr2 = [0, 1, 2, 4, 6, 5, 3]
findMedian(arr2)

