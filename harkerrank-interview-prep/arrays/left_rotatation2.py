from collections import deque


def rotate_left(array, num):
    dq = deque()

    for elem in array:
        dq.append(elem)
    dq.rotate(-num)

    return dq


print(rotate_left([1, 2, 3, 4, 5], 4))
