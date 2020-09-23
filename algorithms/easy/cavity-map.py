# Problem Link: https://www.hackerrank.com/challenges/cavity-map/problem


def cavityMap(grid):
    for i in range(1, len(grid) - 1):
        for k in range(1, len(grid[i]) - 1):
            value = grid[i][k]
            top = grid[i-1][k]
            bottom = grid[i+1][k]
            left = grid[i][k-1]
            right = grid[i][k+1]

            if value > top and value > bottom and value > left and value > right:
                grid[i] = grid[i][:k] + 'X' + grid[i][k+1:]
    return grid


# Second Approach
def cavityMap2(n, grid):
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if grid[i][j] > max(grid[i - 1][j], grid[i + 1][j], grid[i][j - 1], grid[i][j + 1]):
                grid[i] = grid[i][:j] + 'X' + grid[i][j + 1:]

    return grid


grid1 = [[9, 8, 9], [1, 9, 1], [1, 1, 1]]
grid2 = [[1, 1, 1, 2], [1, 9, 1, 2], [1, 8, 9, 2], [1, 2, 3, 4]]

print(cavityMap2(4, grid2))
# print(stringifyList(grid2))
