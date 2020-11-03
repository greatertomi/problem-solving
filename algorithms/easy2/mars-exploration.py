# Problem Link: https://www.hackerrank.com/challenges/mars-exploration/problem


def marsExploration(string):
    count = 0
    for i in range(len(string)):
        if (i % 3 == 0 or i % 3 == 2) and string[i] != 'S':
            count += 1
        if i % 3 == 1 and string[i] != 'O':
            count += 1
    return count


string1 = 'SOSTOT'
string2 = 'SOSSPSSQSSOR'
string3 = 'SOSSOT'
string4 = 'SOSSOSSOS'
print(marsExploration(string4))
