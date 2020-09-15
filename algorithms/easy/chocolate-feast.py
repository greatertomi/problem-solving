# Problem Link: https://www.hackerrank.com/challenges/chocolate-feast/problem


def chocolateFeast(n, c, m):
    count = wrapper = n // c
    while wrapper >= m:
        bars = wrapper // m
        count += bars
        wrapper += bars
        wrapper -= bars * m
    return count


print(chocolateFeast(15, 3, 2))
print(chocolateFeast(10, 2, 5))
print(chocolateFeast(12, 4, 4))
print(chocolateFeast(6, 2, 2))

