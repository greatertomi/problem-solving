# Problem Link: https://www.hackerrank.com/challenges/insertionsort1/problem


def insertionSort(arr):
    value = arr[-1]
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > value:
            arr[i], arr[i+1] = arr[i], arr[i]
            print(*arr)
            if i == 0:
                arr[i], arr[i + 1] = value, arr[i]
                print(*arr)
        elif arr[i] < value:
            arr[i + 1] = value
            print(*arr)
            break


arr1 = [2, 4, 6, 8, 3]
arr2 = [1, 2, 4, 5, 3]
arr3 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
# insertionSort(arr3)
