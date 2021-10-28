n, m = map(int, input().split())
gridReal = [[c for c in input()] for _ in range(n)]


def lengthPlus(i, j):
    length = 1
    while i - length >= 0 and i + length < n and j - length >= 0 and j + length < m and grid[i - length][j] == \
            grid[i + length][j] == grid[i][j - length] == grid[i][j + length] == 'G':
        length += 1
    return length - 1


def maxArea():
    return max([lengthPlus(i, j) * 4 + 1 for i in range(n) for j in range(m) if grid[i][j] == 'G'])


def clearPlus(length, xMiddle, yMiddle):
    grid[xMiddle][yMiddle] = 'B'
    for d in range(1, length + 1):
        grid[xMiddle - d][yMiddle] = 'B'
        grid[xMiddle + d][yMiddle] = 'B'
        grid[xMiddle][yMiddle - d] = 'B'
        grid[xMiddle][yMiddle + d] = 'B'


result = 0
for i in range(n):
    for j in range(m):
        grid = [r.copy() for r in gridReal]
        length = lengthPlus(i, j)
        for k in range(length + 1):
            clearPlus(k, i, j)
            maxAreas = (k * 4 + 1) * maxArea()
            if maxAreas > result:
                result = maxAreas

print(result)
