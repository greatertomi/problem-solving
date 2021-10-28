# Problem Link: https://www.hackerrank.com/challenges/richie-rich/problem


def isPalindrome(string):
    return string == string[::-1]


def highestValuePalindrome(string, n, k):
    if len(string) == 1:
        return '9'

    num = k
    newStr = [x for x in string]
    for i in range(len(string)//2):
        if string[i] != string[-(i+1)] and num > 0:
            newStr[i] = 9
            newStr[(-(i + 1))] = 9
            num -= 1
        else:
            newStr[i] = string[i]
            newStr[(-(i + 1))] = string[-(i + 1)]

    betterStr = ''.join(map(str, newStr))
    if isPalindrome(betterStr) and num > 0:
        for i in range(len(betterStr)):
            if num >= 2 and int(betterStr[i]) != 9:
                newStr[i] = 9
                newStr[(-(i + 1))] = 9
                num -= 2
            elif num < 2:
                break
        if num == 1 and len(betterStr) % 2 == 1 and '9' not in betterStr:
            newStr[len(betterStr) // 2] = 9
        finalVal = ''.join(map(str, newStr))
        if isPalindrome(finalVal):
            return finalVal
        else:
            return '-1'
    else:
        if isPalindrome(betterStr):
            return betterStr
        else:
            return '-1'


# Better answer
def highestValuePalindrome2(s, n, k):
    s = list(s)
    if n <= k:
        return '9' * n
    mink = [0] * (n // 2 + 1)
    for i in range(n // 2 - 1, -1, -1):
        if s[i] != s[n - 1 - i]:
            mink[i] = mink[i + 1] + 1
        else:
            mink[i] = mink[i + 1]
    if mink[0] > k:
        return '-1'
    i = 0
    while i < n // 2 and k > mink[i]:
        if s[i] == '9':
            if s[n - 1 - i] != '9':
                s[n - 1 - i] = '9'
                k -= 1
        elif s[n - 1 - i] == '9':
            s[i] = '9'
            k -= 1
        elif k - 2 >= mink[i + 1]:
            s[i] = s[n - 1 - i] = '9'
            k -= 2
        else:
            if s[i] != s[n - 1 - i]:
                s[i] = s[n - 1 - i] = max(s[n - 1 - i], s[i])
                k -= 1
        i += 1
    if i < n // 2:
        for j in range(i, n // 2):
            if s[j] > s[n - 1 - j]:
                s[n - 1 - j] = s[j]
            else:
                s[j] = s[n - 1 - j]
    elif n % 2:
        if k > 0:
            s[n // 2] = '9'
    return ''.join(s)


print(highestValuePalindrome('932239', 6, 2))
print(highestValuePalindrome('3943', 4, 4))
print(highestValuePalindrome('11331', 5, 4))
print(highestValuePalindrome('3943', 4, 1))
print(highestValuePalindrome('12321', 5, 1))
