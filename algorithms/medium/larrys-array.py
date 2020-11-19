# Problem Link: https://www.hackerrank.com/challenges/larrys-array/problem


def larrysArray(arr):
    sum1 = 0
    for i in range(0, len(arr) - 1):
        count = 0
        for j in range(i + 1, len(arr)):
            print(arr[i], arr[j])
            if arr[i] > arr[j]:
                count += 1
        sum1 += count
    if sum1 % 2 == 0:
        return 'YES'
    else:
        return 'NO'


arr1 = [1, 6, 5, 2, 4, 3]
arr2 = [3, 1, 2]
arr3 = [1, 3, 4, 2]
arr4 = [1, 2, 3, 5, 4]
print(larrysArray(arr1))
print(larrysArray(arr2))
print(larrysArray(arr3))
print(larrysArray(arr4))
