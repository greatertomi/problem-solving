# Problem Link: https://www.hackerrank.com/challenges/apple-and-orange/problem


def countApplesAndOranges(s, t, a, b, apples, oranges):
    falls = [0, 0]
    for i in apples:
        if s <= a + i <= t:
            falls[0] += 1

    for k in oranges:
        if s <= b + k <= t:
            falls[1] += 1
    print(falls)


s1 = 7
t1 = 10
a1 = 4
b1 = 12
apples1 = [2, 3, -4]
oranges1 = [3, -2, -4]
countApplesAndOranges(s1, t1, a1, b1, apples1, oranges1)

s2 = 7
t2 = 11
a2 = 5
b2 = 15
apples2 = [-2, 2, 1]
oranges2 = [5, -6]
countApplesAndOranges(s2, t2, a2, b2, apples2, oranges2)
