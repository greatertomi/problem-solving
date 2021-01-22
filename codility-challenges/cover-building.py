# https://app.codility.com/programmers/task/cover_buildings


def getOccurrences(arr, value):
    indexArr = []
    for i in range(len(arr)):
        if arr[i] == value:
            indexArr.append(i)
    return indexArr


def coverBuilding(arr):
    maxVal = max(arr)
    maxCount = arr.count(maxVal)
    total = None
    if maxCount == 1:
        maxIndex = arr.index(maxVal)
        num1 = len(arr[maxIndex:]) * maxVal
        num2 = len(arr[:maxIndex]) * max(arr[:maxIndex])
        print(num1, num2)
        total = num1 + num2
    else:
        pass


arr1 = [3, 1, 4]
arr2 = [5, 3, 2, 4]
arr3 = [5, 3, 5, 2, 1]
arr4 = [7, 7, 3, 7, 7]
arr5 = [1, 1, 7, 6, 6]
coverBuilding(arr3)
