# Problem Link: https://www.hackerrank.com/challenges/matrix-rotation-algo/problem


# 00 01 02 03 13 23 33 32 31 30 20 10
def matrixRotation(matrix):
    colLen = len(matrix)
    rowLen = len(matrix[0])
    row = 0
    col = 0
    array = []
    for i in range(12):
        array.append((row, col))



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
