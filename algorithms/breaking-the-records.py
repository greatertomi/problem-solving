# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem


def breakingRecords(scores):
    maxMin = [0, 0]
    currentMin = scores[0]
    currentMax = scores[0]
    for score in scores:
        if score > currentMax:
            currentMax = score
            maxMin[0] += 1
        if score < currentMin:
            currentMin = score
            maxMin[1] += 1
    print(maxMin)


# Answer: Max Min
values1 = [12, 24, 10, 24]  # 1 1
values2 = [10, 5, 20, 4, 5, 2, 25, 1]  # 2 4
values3 = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]  # 4 0

breakingRecords(values3)
