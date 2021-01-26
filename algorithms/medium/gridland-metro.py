# Problem Link: https://www.hackerrank.com/challenges/gridland-metro/problem


def gridlandMetro(rows, cols, k, tracks):
    array = [[0 for i in range(cols)] for j in range(rows)]
    path = array[1]
    # Start from here
    newPath = path[:1] + [3] * 2 + path[3:]
    print(path, newPath, array)
    for track in tracks:
        path = array[track[0]]
        path[track[1]: track[2]] = 1
        print(path, array)
    print('final', array)


track1 = [(1, 1, 4), (2, 2, 4), (3, 1, 2), (4, 2, 3)]
track2 = [(2, 2, 3), (3, 1, 4), (4, 4, 4)]
gridlandMetro(4, 4, 4, track1)
# gridlandMetro(4, 4, 3, track2)
