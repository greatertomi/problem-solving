# https://app.codility.com/programmers/task/cover_buildings


def getAllIndexes(arr, value):
    indexArr = []
    for i in range(len(arr)):
        if arr[i] == value:
            indexArr.append(i)
    return indexArr


def coverBuilding(arr):
    maxVal = max(arr)
    maxCount = arr.count(maxVal)

    if maxCount == 1:
        maxIndex = arr.index(maxVal)
        if maxIndex == 0:
            return maxVal + (len(arr[maxIndex + 1:]) * max(arr[maxIndex + 1:]))

        num1 = len(arr[maxIndex:]) * maxVal
        num2 = len(arr[:maxIndex]) * max(arr[:maxIndex])
        return num1 + num2

    maxIndex = getAllIndexes(arr, maxVal)
    if 0 in maxIndex and len(arr) - 1 in maxIndex:
        return maxVal * len(arr)

    side1 = sum(arr[:maxIndex[-1]])
    side2 = sum(arr[maxIndex[-1] + 1:])

    if side1 >= side2:
        num1 = len(arr[:maxIndex[-1] + 1]) * maxVal
        num2 = len(arr[maxIndex[-1] + 1:]) * max(arr[maxIndex[-1] + 1:])
    else:
        num1 = len(arr[maxIndex:]) * maxVal
        num2 = len(arr[:maxIndex]) * max(arr[:maxIndex])
    return num1 + num2


arr1 = [1, 1, 1]
arr2 = [5, 3, 2, 4]
arr3 = [5, 3, 5, 2, 1]
arr4 = [7, 7, 3, 7, 7]
arr5 = [1, 1, 7, 6, 6, 6]
print(coverBuilding(arr1))
