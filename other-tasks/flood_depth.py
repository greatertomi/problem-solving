# Problem Link
# https://app.codility.com/programmers/lessons/90-tasks_from_indeed_prime_2015_challenge/flood_depth/


def flood_depth(array):
    d = None
    maxH = 0
    minH = 0
    maxD = 0
    for a in array:
        if a > maxH:
            d = maxH - minH
            maxH = a
            minH = a
        elif a < minH:
            minH = a
        else:
            d = a - minH
        if d > maxD:
            maxD = d
    return maxD

value = [1, 3, 2, 1, 2, 1, 5, 3, 3, 4, 2]
value2 = [5, 8]
print(flood_depth(value))
