# Problem Link: https://www.hackerrank.com/challenges/funny-string/problem


def funnyString(string):
    strArray1 = [ord(char) for char in string]
    strArray2 = strArray1[::-1]
    arr1 = [abs(strArray1[i] - strArray1[i-1]) for i in range(1, len(strArray1))]
    arr2 = [abs(strArray2[i] - strArray2[i-1]) for i in range(1, len(strArray2))]
    if arr1 == arr2:
        return 'Funny'
    else:
        return 'Not Funny'


string1 = 'lmnop'
string2 = 'acxz'
string3 = 'bcxz'
print(funnyString(string1))
print(funnyString(string2))
print(funnyString(string3))
