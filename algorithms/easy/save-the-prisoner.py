# Problem Link: https://www.hackerrank.com/challenges/save-the-prisoner/problem


def saveThePrisoner(num, sweets, start):
    last = ((sweets - 1) + (start - 1)) % num + 1
    return last
    # (start + sweets - 1) % num or num


print(saveThePrisoner(4, 6, 2))
print(saveThePrisoner(3, 7, 3))
print(saveThePrisoner(7, 19, 2))
