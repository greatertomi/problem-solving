# Problem Link: https://www.hackerrank.com/challenges/closest-numbers/problem


def closestNumbers(arr):
    pairs = []
    minDiff = None
    arr = sorted(arr)
    for i in range(1, len(arr)):
        if i == 1:
            minDiff = abs(arr[i-1] - arr[i])
            pairs.extend([arr[i-1], arr[i]])
        else:
            diff = abs(arr[i-1] - arr[i])
            if diff == minDiff:
                pairs.extend([arr[i-1], arr[i]])
            elif diff < minDiff:
                minDiff = diff
                pairs = [arr[i-1], arr[i]]
    return pairs


arr1 = [-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854]
arr2 = [-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854, -520, -470]
arr3 = [5, 4, 3, 2]
print(closestNumbers(arr1))
print(closestNumbers(arr2))
print(closestNumbers(arr3))
