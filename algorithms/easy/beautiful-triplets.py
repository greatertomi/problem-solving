# Problem Link: https://www.hackerrank.com/challenges/beautiful-triplets/problem


def beautifulTriplets(d, arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] + d in arr and arr[i] + 2 * d in arr:
            count += 1
    return count


d1 = 3
arr1 = [2, 2, 3, 4, 5]

d2 = 3
arr2 = [1, 2, 4, 5, 7, 8, 10]
print(beautifulTriplets(d2, arr2))
