# Problem Link: https://www.hackerrank.com/challenges/two-pluses/problem


def getPositionalVal(grid, i, j):
    valueArr = [1]
    currentVal = 1
    stopPoint = min(len(grid) - 1 - i, i, len(grid[1]) - j - 1, j)
    for p in range(1, stopPoint+1):
        if grid[i-p][j] == 'G' and grid[i+p][j] == 'G' and grid[i][j-p] == 'G' and grid[i][j+p] == 'G':
            currentVal += 4
            valueArr.append(currentVal)
        else:
            break
    return max(valueArr)


def twoPluses(grid):
    goodPluses = []
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[i])-1):
            if grid[i][j] == 'G':
                goodPluses.append(getPositionalVal(grid, i, j))
    goodPluses.sort()
    print(goodPluses)
    # return goodPluses[-1]*goodPluses[-2]


grid1 = [
    'GGGGGG',
    'GBBBGB',
    'GGGGGG',
    'GGBBGB',
    'GGGGGG'
]

grid2 = [
    'BGBBGB',
    'GGGGGG',
    'BGBBGB',
    'GGGGGG',
    'BGBBGB',
    'BGBBGB'
]

grid3 = [
    'GGGGGGG',
    'BGBBBBG',
    'BGBBBBG',
    'GGGGGGG',
    'GGGGGGG',
    'BGBBBBG',
]

print(twoPluses(grid3))
# print(getPositionalVal(grid2, 3, 4))
