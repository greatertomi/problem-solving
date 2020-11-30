# Problem Link: https://www.hackerrank.com/challenges/countingsort4/problem


def countSort(arr):
    nums = [num[0] for num in arr]
    baskets = [[] for _ in range(max(nums) + 1)]

    for i in range(len(arr)):
        if i < len(arr) // 2:
            baskets[arr[i][0]].append('-')
        else:
            baskets[arr[i][0]].append(arr[i][1])
    newString = ''
    for val in baskets:
        newString += ' '.join(map(str, val))
        newString += ' '
    print(newString)


def countSort2(arr):  # use n instead of len(arr)
    n = len(arr)

    for l in arr:
        l[0] = int(l[0])  # convert first list item to integer

    for i in range(n // 2):  # replace first half with hyphen
        arr[i][1] = "-"

    # sort by number into empty list array
    output = [[] for _ in range(n)]
    for l in arr:
        output[l[0]].append(l[1])

    print(' '.join(j for i in output for j in i))


arr1 = [[0, 'a'], [1, 'b'], [0, 'c'], [1, 'd']]
arr2 = [[0, 'ab'], [6, 'cd'], [0, 'ef'], [6, 'gh'], [4, 'ij'], [0, 'ab'], [6, 'cd'], [0, 'ef'], [6, 'gh'], [0, 'ij'],
        [4, 'that'], [3, 'be'], [0, 'to'], [1, 'be'], [5, 'question'], [1, 'or'], [2, 'not'], [4, 'is'], [2, 'to'],
        [4, 'the']]

countSort2(arr2)
