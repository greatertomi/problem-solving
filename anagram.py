# Problem Link: https://www.hackerrank.com/challenges/anagram/problem


def anagram(string):
    length = len(string)
    if length % 2 == 1:
        return -1

    part1 = list(string[:length//2])
    part2 = list(string[length//2:])
    count = 0
    for val in part1:
        if val in part2:
            index = part2.index(val)
            del part2[index]
        else:
            count += 1
    return count


string1 = 'aaabbb'
string2 = 'ab'
string3 = 'abc'
string4 = 'mnop'
string5 = 'xyyx'
string6 = 'xaxbbbxx'

print(anagram(string1))
print(anagram(string2))
print(anagram(string3))
print(anagram(string4))
print(anagram(string5))
print(anagram(string6))

