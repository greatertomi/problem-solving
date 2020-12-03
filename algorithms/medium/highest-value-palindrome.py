# Problem Link: https://www.hackerrank.com/challenges/richie-rich/problem


def isPalindrome(string):
    return string == string[::-1]


def highestValuePalindrome(string, n, k):
    if len(string) == 1:
        return '9'

    if isPalindrome(string):
        return string

    num = k
    newStr = [0]*n
    for i in range(len(string)//2):
        if string[i] != string[-(i+1)] and num > 0:
            newStr[i] = 9
            newStr[(-(i + 1))] = 9
            num -= 1
        else:
            newStr[i] = string[i]
            newStr[(-(i + 1))] = string[-(i + 1)]
    finalVal = ''.join(map(str, newStr))
    if isPalindrome(finalVal):
        return finalVal
    return '-1'


string1 = '3943'
string2 = '092299'
string3 = '0011'

print(highestValuePalindrome('932239', 6, 2))
# print(highestValuePalindrome(string2, 6, 3))
# print(highestValuePalindrome(string3, 4, 1))
