# Problem Link: https://www.hackerrank.com/challenges/the-birthday-bar/problem


def birthday(s, d, m):
    ans = 0
    for i in range(len(s)):
        n = 0
        count = 0
        while n < m:
            count += s[i + n]
            n += 1
        if count == d:
            ans += 1
        if i + n == len(s):
            break
    return ans


choco1 = [2, 2, 1, 3, 2]
d1 = 4
m1 = 2

choco2 = [1, 2, 1, 3, 2]
d2 = 3
m2 = 2

choco3 = [1, 1, 1, 1, 1, 1]
d3 = 3
m3 = 2

choco4 = [4]
d4 = 4
m4 = 1

choco5 = [2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1]
d5 = 18
m5 = 7

print('count', birthday(choco5, d5, m5))
