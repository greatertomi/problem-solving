# Problem Link: https://www.hackerrank.com/challenges/encryption/problem
import math


def encryption(string):
    string = ''.join(string.split())
    length = len(string)
    col = math.ceil(math.sqrt(length))
    array = []
    temp = ''
    for i in range(1, len(string) + 1):
        temp += string[i-1]
        if i % col == 0:
            array.append(temp)
            temp = ''

    if length % col != 0:
        array.append(string[-(length % col):])
    new_string = ''

    for i in range(col):
        temp_str = ''
        for k in array:
            try:
                temp_str += k[i]
            except IndexError:
                temp_str += ''
        new_string += temp_str + ' '

    return new_string


string1 = 'if man was meant to stay on the ground god would have given us roots'
string2 = 'have a nice day'
string3 = 'feed the dog'
string4 = 'chill out'

print(encryption(string4))
