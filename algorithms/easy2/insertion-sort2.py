# Problem Link: https://www.hackerrank.com/challenges/insertionsort2/problem


def insertionSort(arr):
    for i in range(1, len(arr)):
        currentVal = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > currentVal:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = currentVal
        print(arr)
    # return arr


arr1 = [1, 4, 3, 5, 6, 2]
arr2 = [3, 4, 7, 5, 6, 2, 1]
insertionSort(arr1)

