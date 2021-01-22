# Problem Link: https://app.codility.com/programmers/task/rectangles_strip


def rectangleStrip(arr1, arr2):
    valueMap = {}
    for i in range(len(arr1)):
        if arr1[i] == arr2[i]:
            if arr1[i] in valueMap:
                valueMap[arr1[i]] += 1
            else:
                valueMap[arr1[i]] = 1
        else:
            if arr1[i] in valueMap:
                valueMap[arr1[i]] += 1
            else:
                valueMap[arr1[i]] = 1

            if arr2[i] in valueMap:
                valueMap[arr2[i]] += 1
            else:
                valueMap[arr2[i]] = 1
    return max(valueMap.values())


print(rectangleStrip([2, 3, 2, 3, 5], [3, 4, 2, 4, 2]))
print(rectangleStrip([2, 3, 1, 3], [2, 3, 1, 3]))
print(rectangleStrip([2, 10, 4, 1, 4], [4, 1, 2, 2, 5]))
