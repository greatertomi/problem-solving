# Problem Link: https://www.hackerrank.com/challenges/the-hurdle-race/problem


def hurdleRace(k, height):
    maxH = max(k)
    needed = 0
    if maxH > height:
        needed = maxH - height
    return needed


k1 = [1, 6, 3, 5, 2]
h1 = 4

k2 = [2, 5, 4, 5, 2]
h2 = 7
print(hurdleRace(k2, h2))
