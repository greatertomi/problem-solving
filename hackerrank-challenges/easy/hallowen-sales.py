# Problem Link: https://www.hackerrank.com/challenges/halloween-sale/problem


def howManyGames(p, d, m, s):
    count = 0
    while s >= p:
        count += 1
        s -= p
        p = max(p-d, m)
    return count


print(howManyGames(20, 3, 6, 80))
