# Problem Link: https://www.hackerrank.com/challenges/flatland-space-stations/problem


# My solution
def flatlandSpaceStations(n, c):
    maxStationDist = 0
    for i in range(n):
        # Finds the closest station
        min_dist = min(c, key=lambda x: abs(x - i))
        dist = abs(i - min_dist)
        if dist > maxStationDist:
            maxStationDist = dist
    return maxStationDist


# Better solution
def flatlandSpaceStations2(n, c):
    c.sort()
    maxd = max(c[0], n-1 - c[-1])
    for i in range(len(c)-1):
        maxd = max((c[i+1]-c[i])//2, maxd)
    return maxd


n1 = 3
c1 = [0]

n2 = 5
c2 = [0, 4]

n3 = 6
c3 = [0, 1, 2, 4, 3, 5]

n4 = 8
c4 = [1, 5]
print(flatlandSpaceStations(n4, c4))
