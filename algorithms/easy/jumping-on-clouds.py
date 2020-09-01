# Problem Link: https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem


def jumpingOnClouds(c, k):
    n = len(c)
    energy = 100
    i = k % n
    energy -= c[i] * 2 + 1
    while i != 0:
        i = (i + k) % n
        energy -= c[i] * 2 + 1
    return energy


c1 = [0, 0, 1, 0]
k1 = 2

c2 = [0, 0, 1, 0, 0, 1, 1, 0]
k2 = 2

c3 = [1, 1, 1, 0, 1, 1, 0, 0, 0, 0]
k3 = 3
print(jumpingOnClouds(c3, k3))
