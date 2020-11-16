# Problem Link: https://www.hackerrank.com/challenges/palindrome-index/problem


def isPalindrome(string):
    for i in range(len(string)//2):
        if string[i] != string[-(i+1)]:
            return False
    return True


def palindromeIndex(string):
    if isPalindrome(string):
        return -1

    for i in range(len(string)):
        word = string[:i] + string[i+1:]
        if isPalindrome(word):
            return i
    return -1


string1 = 'aaab'
string2 = 'baa'
string3 = 'aaa'

print(palindromeIndex(string1))
print(palindromeIndex(string2))
print(palindromeIndex(string3))
# str1 = 'abcdef'
# print(str1[:3] + str1[4:])

