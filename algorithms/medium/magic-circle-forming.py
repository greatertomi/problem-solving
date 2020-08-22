# Problem Link: https://www.hackerrank.com/challenges/magic-square-forming/problem
import sys


def formingMagicSquare(arr):
    arr = sum(arr, [])  # Converts 2d to 1d

    magic = [[8, 1, 6, 3, 5, 7, 4, 9, 2], [6, 1, 8, 7, 5, 3, 2, 9, 4],
             [4, 3, 8, 9, 5, 1, 2, 7, 6], [2, 7, 6, 9, 5, 1, 4, 3, 8],
             [2, 9, 4, 7, 5, 3, 6, 1, 8], [4, 9, 2, 3, 5, 7, 8, 1, 6],
             [6, 7, 2, 1, 5, 9, 8, 3, 4], [8, 3, 4, 1, 5, 9, 6, 7, 2]]

    minimumCost = sys.maxsize
    for mag in magic:
        diff = 0
        for i, j in zip(arr, mag):
            diff += abs(i - j)
        minimumCost = min(minimumCost, diff)

    return minimumCost


square1 = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
square2 = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]
square3 = [[4, 8, 2], [4, 5, 7], [6, 1, 6]]
formingMagicSquare(square1)
