# Problem Link: https://www.hackerrank.com/challenges/palindrome-index/problem

def isPalindrome(string):
    for i in range(0, len(string)//2):
        if string[i] != string[-(1 + i)]:
            return False
    return True


def palindromeIndex(string):
    pass


palindromeIndex('aaaba')
# palindromeIndex('baa')
# palindromeIndex('aaa')

