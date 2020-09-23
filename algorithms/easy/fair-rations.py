# Problem Link: https://www.hackerrank.com/challenges/fair-rations/problem


def fairRations(arr):
    count = 0
    for a in range(len(arr)):
        try:
            if arr[a] % 2 == 1:
                count += 2
                arr[a + 1] += 1
        except IndexError:
            return 'NO'
    return count


arr1 = [4, 5, 6, 7]
arr2 = [2, 3, 4, 5, 6]
arr3 = [1, 2]

print(fairRations(arr1))
print(fairRations(arr2))
print(fairRations(arr3))
