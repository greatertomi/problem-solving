# Problem Link: https://www.hackerrank.com/challenges/utopian-tree/problem


def utopianTree(n):
    if n == 0:
        return 1

    height = 1
    for i in range(1, n+1):
        if i % 2 == 1:
            height *= 2
        else:
            height += 1
    return height


n1 = 8
print(utopianTree(n1))
