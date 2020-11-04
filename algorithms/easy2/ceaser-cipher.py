# Problem Link: https://www.hackerrank.com/challenges/caesar-cipher-1/problem


def caesarCipher(string, k):
    num = k % 26
    alphabets1 = 'abcdefghijklmnopqrstuvwxyz'
    alphabets2 = alphabets1[num:] + alphabets1[:num]
    print(alphabets2)
    newWord = ''
    for char in string:
        if char.isupper():
            index = alphabets1.index(char.lower())
            newWord += alphabets2[index].upper()
        elif char.isalpha():
            index = alphabets1.index(char)
            newWord += alphabets2[index]
        else:
            newWord += char
    return newWord


string1 = "There's-a-starman-waiting-in-the-sky"
string2 = 'middle-Outz'
string3 = 'www.abc.xy'
print(caesarCipher(string3, 87))
# print(string1.index('h'))
