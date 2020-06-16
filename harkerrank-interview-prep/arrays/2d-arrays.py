# Question Link:
# https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=arrays


def hourglass_sum(value):
    hourglasses = []

    for i in range(len(value) - 2):
        count = 0
        while count < len(value[i]) - 2:
            arr1 = value[i][count:count + 3]
            arr2 = value[i + 2][count:count + 3]
            mid = (count + count + 3) // 2
            arr3 = [value[i + 1][mid]]
            new_arr = arr1 + arr3 + arr2
            hourglasses.append(new_arr)
            count += 1

    maximum = None
    for i in range(len(hourglasses)):
        summer = sum(hourglasses[i])
        if i == 0:
            maximum = summer
        else:
            if summer > maximum:
                maximum = summer
    return maximum


valueArr1 = [
    [-9, -9, -9, 1, 1, 1],
    [0, -9, 0, 4, 3, 2],
    [-9, -9, -9, 1, 2, 3],
    [0, 0, 8, 6, 6, 0],
    [0, 0, 0, -2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]
valueArr2 = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]
print(hourglass_sum(valueArr2))
