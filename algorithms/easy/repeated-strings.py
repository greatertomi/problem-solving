# Problem Link: https://www.hackerrank.com/challenges/repeated-string/problem
import math


def repeatedStrings(string, n):
    countA = 0
    for i in range(len(string)):
        if string[i] == 'a':
            countA += 1



s1 = 'aba'
n1 = 10

s2 = 'a'
n2 = 1000000

s3 = 'abcac'
n3 = 10

print(repeatedStrings(s3, n3))
