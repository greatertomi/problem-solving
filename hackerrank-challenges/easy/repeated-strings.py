# Problem Link: https://www.hackerrank.com/challenges/repeated-string/problem


def repeatedStrings(string, n):
    countA = 0
    for i in range(len(string)):
        if string[i] == 'a':
            countA += 1
    totalA = (n // len(string))*countA
    rems = n % len(string)

    for i in range(rems):
        if string[i] == 'a':
            totalA += 1
    return totalA


s1 = 'aba'
n1 = 10

s2 = 'a'
n2 = 1000000

s3 = 'abcac'
n3 = 10

print(repeatedStrings(s2, n2))
