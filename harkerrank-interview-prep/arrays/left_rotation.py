# Problem Link
# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays


def rotate_left(array, num):
    for i in range(num):
        array = array[1:] + [array[0]]
    return array


print(rotate_left([1, 2, 3, 4, 5], 4))

