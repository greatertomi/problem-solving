# Problem Link: https://www.hackerrank.com/challenges/quicksort1/problem


def quickSort(arr):
    pivot = arr[0]
    lessArr = []
    greaterArr = []
    equalsArr = []
    for num in arr:
        if num < pivot:
            lessArr.append(num)
        elif num > pivot:
            greaterArr.append(num)
        else:
            equalsArr.append(num)
    return lessArr + equalsArr + greaterArr


arr1 = [4, 5, 3, 7, 2]
arr2 = [5, 7, 4, 3, 8]
print(quickSort(arr2))
