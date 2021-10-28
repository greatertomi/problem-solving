# Problem Link: https://www.hackerrank.com/challenges/electronics-shop/problem


def getMoneySpent(keyboards, drives, b):
    maxCost = -1
    for keyboard in keyboards:
        for drive in drives:
            total = keyboard + drive
            if maxCost < total <= b:
                maxCost = total
    return maxCost


keyboards1 = [3, 1]
drives1 = [5, 2, 8]
b1 = 10

keyboards2 = [4]
drives2 = [5]
b2 = 5

print(getMoneySpent(keyboards1, drives1, b1))
