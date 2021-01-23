# Problem Link: https://www.hackerrank.com/challenges/candies/problem


def candies(arr):
    sweets = []
    for i in range(0, len(arr)):
        if len(sweets) == 0:
            sweets.append(1)
        else:
            if arr[i] > arr[i-1]:
                sweets.append(sweets[-1] + 1)
            else:
                sweets.append(1)

    return sum(sweets)


arr1 = [1, 2, 2]
arr2 = [4, 6, 4, 5, 6, 2]
arr3 = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]
arr4 = [2, 4, 3, 5, 2, 6, 4, 5]
candies(arr4)
