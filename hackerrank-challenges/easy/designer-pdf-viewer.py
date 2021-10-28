# Problem Link: https://www.hackerrank.com/challenges/designer-pdf-viewer/problem


def getLetterIndex(letter):
    alphaDict = {'a': 1, 'b': 2, 'c': 3, 'e': 5, 'd': 4, 'g': 7, 'f': 6,
                 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12, 'o': 15,
                 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20,
                 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}
    return alphaDict[letter]


def designerPdfViewer(h, word):
    maxHeight = 0
    for i in word:
        height = h[getLetterIndex(i) - 1]
        if height > maxHeight:
            maxHeight = height
    return maxHeight * len(word)


h1 = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
word1 = 'abc'

h2 = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
word2 = 'zaba'

print(designerPdfViewer(h1, word1))
