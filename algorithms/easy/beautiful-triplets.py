# Problem Link: https://www.hackerrank.com/challenges/beautiful-triplets/problem


def beautifulTriplets(d, arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                if arr[j] - arr[i] == arr[k] - arr[j] == d:
                    count += 1
    return count


d1 = 3
arr1 = [2, 2, 3, 4, 5]

d2 = 3
arr2 = [1, 2, 4, 5, 7, 8, 10]
beautifulTriplets(d2, arr2)
