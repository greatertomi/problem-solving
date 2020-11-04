# Problem Link: https://www.hackerrank.com/challenges/pangrams/problem


def pangrams(string):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    string = string.lower()
    for char in alphabets:
        if char not in string:
            return 'not pangram'
    return 'pangram'


string1 = 'The quick brown fox jumps over the lazy dog'
string2 = 'We promptly judged antique ivory buckles for the next prize'
string3 = 'We promptly judged antique ivory buckles for the prize'
print(pangrams(string1))
print(pangrams(string2))
print(pangrams(string3))
