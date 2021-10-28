# Problem Link: https://www.hackerrank.com/challenges/gridland-metro/problem
import bisect


def gridlandMetro(rows, cols, k, tracks):
    array = [[0 for _ in range(cols)] for _ in range(rows)]
    for track in tracks:
        path = array[track[0] - 1]
        length = track[2] - track[1] + 1
        newPath = path[:track[1] - 1] + [1] * length + path[track[2]:]
        array[track[0] - 1] = newPath
    print(array)
    total = sum([x.count(0) for x in array])
    return total


def gridlandMetroSolution(rows, cols, k, tracks):
    data = {}
    for row, col1, col2 in tracks:
        if row not in data:
            data[row] = [col1, col2]
        else:
            index1 = bisect.bisect_left(data[row], col1)
            index2 = bisect.bisect_right(data[row], col2)
            if index1 % 2:
                if index2 % 2:
                    data[row][index1:index2] = []
                else:
                    data[row][index1:index2] = [col2]
            else:
                if index2 % 2:
                    data[row][index1:index2] = [col1]
                elif index1 != index2:
                    data[row][index1:index2] = [col1, col2]
                else:
                    data[row].insert(index1, col1)
                    data[row].insert(index1+1, col2)
    area = 0
    for row in data.values():
        for i in range(len(row)//2):
            area += row[2*i+1] - row[2*i] + 1
    return rows * cols - area


track1 = [(1, 1, 4), (2, 2, 4), (3, 1, 2), (4, 2, 3)]
track2 = [(2, 2, 3), (3, 1, 4), (4, 4, 4)]
track3 = [(1, 1, 2), (1, 4, 4), (2, 1, 2), (2, 2, 3), (2, 4, 5), (4, 1, 2), (4, 4, 5)]

gridlandMetroSolution(4, 4, 4, track1)
# print(gridlandMetro(4, 4, 3, track2))
# print(gridlandMetro(4, 5, 7, track3))  # 8
