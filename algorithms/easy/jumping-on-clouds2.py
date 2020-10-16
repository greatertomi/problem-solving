# Problem Link: https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem


def jumpingOnClouds(arr):
    jumps = 0
    count = 0
    while count <= len(arr) - 2:
        try:
            if arr[count + 2] == 0:
                count += 2
            else:
                count += 1
        except IndexError:
            count += 1
        jumps += 1

    return jumps


cloud1 = [0, 1, 0, 0, 0, 1, 0]
cloud2 = [0, 0, 1, 0, 0, 1, 0]
cloud3 = [0, 0, 0, 0, 1, 0]
jumpingOnClouds(cloud3)

