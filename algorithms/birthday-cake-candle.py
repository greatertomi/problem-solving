# Problem Link: https://www.hackerrank.com/challenges/birthday-cake-candles/problem


def birthdayCakeCandle(arr):
    maximum = max(arr)
    return arr.count(maximum)


candles = [3, 2, 1, 3]
print(birthdayCakeCandle(candles))
