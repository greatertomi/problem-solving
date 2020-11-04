# Problem Link: https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem
import re


def hackerrankInAString(string):
    sub = "hackerrank"
    j = 0

    for p in string:
        if p == sub[j]:
            j += 1
            if j == len(sub):
                return "YES"
    return "NO"


def hackerrankInAString2(string):
    return re.search('.*'.join("hackerrank"), string) and "YES" or "NO"


string1 = 'hereiamstackerrank'
string2 = 'hackerworld'
string3 = 'hhaacckkekraraannk'
string4 = 'rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt'
print(hackerrankInAString2(string4))
