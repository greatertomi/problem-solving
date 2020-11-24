# Problem Link: https://www.hackerrank.com/challenges/matrix-rotation-algo/problem


def processInternals(arr):
    colLen = len(arr)
    rowLen = len(arr[0])
    array = []
    kept = []
    internal = []
    for i in range(colLen):
        if i == 0:
            array.extend(arr[i])
        elif i == colLen - 1:
            array.extend(arr[i][::-1])
        else:
            array.append(arr[i][-1])
            internal.append(arr[i][1:-1])
            kept.append(arr[i][0])
    array = array + kept
    return array, internal


# 00 01 02 03 13 23 33 32 31 30 20 10
def matrixRotation(matrix):
    colLen = len(matrix)
    rowLen = len(matrix[0])
    array = []
    kept = []
    internal = []
    for i in range(colLen):
        row = []
        for j in range(rowLen):
            row.append((i, j))
        if i == 0:
            array.extend(row)
        elif i == colLen - 1:
            row.reverse()
            array.extend(row)
        else:
            array.append(row[-1])
            internal.append(row[1:-1])
            kept.append(row[0])
    kept.reverse()
    array = array + kept
    print(array)
    print(processInternals(internal))


matrix1 = [
    [1, 2, 3, 4],
    [12, 1, 2, 5],
    [11, 4, 3, 6],
    [10, 9, 8, 7]
]
rotate1 = 2

matrix2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
rotate2 = 2

matrix3 = [
    [1, 2, 3, 4],
    [7, 8, 9, 10],
    [13, 14, 15, 16],
    [19, 20, 21, 22],
    [25, 26, 27, 28]
]
rotate3 = 7

matrixRotation(matrix1)
