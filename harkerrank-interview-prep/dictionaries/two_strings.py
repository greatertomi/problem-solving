def twoStrings(s1, s2):
    status = "NO"
    for char in s1:
        if char in s2:
            status = "YES"
            break
        else:
            status = "NO"
    print(status)


word1 = "Hi"
word2 = "World"
twoStrings(word1, word2)
