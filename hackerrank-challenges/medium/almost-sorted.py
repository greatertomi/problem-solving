# Problem Link: https://www.hackerrank.com/challenges/almost-sorted/problem


def reversal(arr, start, end):
    subArr = arr[start:end+1]
    subArr = subArr[::-1]
    newArr = arr[:start] + subArr + arr[end+1:]
    return newArr


def almostSorted(arr):
    sortedArr = sorted(arr)
    if arr == sortedArr:
        print('yes')
        return

    # Handles swap
    misplaced = []
    swappedArr = arr
    for i in range(len(arr)):
        if arr[i] != sortedArr[i]:
            misplaced.append(i)
    if len(misplaced) == 2:
        swappedArr[misplaced[0]], swappedArr[misplaced[1]] = swappedArr[misplaced[1]], swappedArr[misplaced[0]]
    if swappedArr == sortedArr:
        print('yes')
        print('swap {} {}'.format(misplaced[0]+1, misplaced[1]+1))
        return

    # Handles Reversal
    start = None
    end = None
    for i in range(len(arr)):
        if arr[i] != sortedArr[i]:
            if start is None:
                start = i
            else:
                end = i

    if start is not None and end is not None:
        reversedArr = reversal(arr, start, end)
        if reversedArr == sortedArr:
            print('yes')
            print('reverse {} {}'.format(start+1, end+1))
            return
        else:
            print('no')
            return
    else:
        print('no')
        return


arr1 = [2, 3, 5, 4]
arr2 = [4, 2]
arr3 = [3, 1, 2]
arr4 = [1, 5, 4, 3, 2, 6]
arr5 = [2, 4, 7, 8, 10]
# almostSorted(arr1)
# almostSorted(arr2)
almostSorted(arr3)
# almostSorted(arr4)
# almostSorted(arr5)
