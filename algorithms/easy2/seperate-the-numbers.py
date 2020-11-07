# Problem Link: https://www.hackerrank.com/challenges/separate-the-numbers/problem


def separateNumbers(string):
    length = len(string)
    if length < 2:
        return 'NO'

    status = 'NO'
    width = 2
    i = 0
    nums = []
    while i < length:
        num = string[i: i + width]
        print(num)
        i += width


string1 = '1234'
string2 = '91011'
string3 = '99100'
string4 = '101103'
string5 = '010203'
string6 = '13'
string7 = '1'
print(separateNumbers(string2))
