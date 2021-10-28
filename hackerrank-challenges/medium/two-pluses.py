# Problem Link: https://www.hackerrank.com/challenges/two-pluses/problem


def getPositionalVal(grid, i, j):
    valueArr = [1]
    currentVal = 1
    touchedPoints = [(i, j)]
    stopPoint = min(len(grid) - 1 - i, i, len(grid[1]) - j - 1, j)
    for p in range(1, stopPoint+1):
        if grid[i-p][j] == 'G' and grid[i+p][j] == 'G' and grid[i][j-p] == 'G' and grid[i][j+p] == 'G':
            currentVal += 4
            touchedPoints.extend([(i-p, j), (i+p, j), (i, j-p), (i, j+p)])
            valueArr.append(currentVal)
        else:
            break
    return max(valueArr), touchedPoints


def hasDuplicate(mainArr, incoming):
    for val in incoming:
        if val in mainArr:
            return True
    return False


def twoPluses(grid):
    goodPluses = [1]
    touchedPoints = []
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[i])-1):
            if grid[i][j] == 'G':
                val = getPositionalVal(grid, i, j)
                # print('tP -> ', touchedPoints, 'new -> ', val[1])
                # or val[0] > max(goodPluses)
                if val[0] > 1 and (hasDuplicate(touchedPoints, val[1]) is False):
                    goodPluses.append(val[0])
                    touchedPoints.extend(val[1])
    goodPluses.sort()
    # print(goodPluses)
    if len(goodPluses) > 1:
        return goodPluses[-1]*goodPluses[-2]
    elif len(goodPluses) == 1:
        return goodPluses[-1]
    else:
        return 0


grid1 = [
    'BBBBBGGBGG',
    'GGGGGGGGGG',
    'GGGGGGGGGG',
    'BBBBBGGBGG',
    'BBBBBGGBGG',
    'GGGGGGGGGG',
    'BBBBBGGBGG',
    'GGGGGGGGGG',
    'BBBBBGGBGG',
    'GGGGGGGGGG'
]
# 85

grid2 = [
    'GGGGGGGGGG',
    'GBBBBBBGGG',
    'GGGGGGGGGG',
    'GGGGGGGGGG',
    'GBBBBBBGGG',
    'GGGGGGGGGG',
    'GBBBBBBGGG',
    'GBBBBBBGGG',
    'GGGGGGGGGG'
]
# 45

grid3 = [
    'GGGGGGGG',
    'GBGBGGBG',
    'GBGBGGBG',
    'GGGGGGGG',
    'GBGBGGBG',
    'GGGGGGGG',
    'GBGBGGBG',
    'GGGGGGGG'
]
# 81

print(twoPluses(grid1))
# print(getPositionalVal(grid2, 3, 4))

