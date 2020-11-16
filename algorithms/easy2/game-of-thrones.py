# Problem Link: https://www.hackerrank.com/challenges/game-of-thrones/problem


def gameOfThrones(string):
    unique = list(set(string))
    count1 = 0
    for i in unique:
        count = string.count(i)
        if count % 2 == 1:
            count1 += 1
    if count1 <= 1:
        return True
    else:
        return False


string1 = 'aaabbbb'
string2 = 'cdefghmnopqrstuvw'
string3 = 'cdcdcdcdeeeef'

print(gameOfThrones(string3))
