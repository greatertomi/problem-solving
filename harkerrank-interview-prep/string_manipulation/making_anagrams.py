def makeAnagram(string, string2):
    string1 = string[::-1]
    for i in range(len(string)):
        if string[i] in string2:
            pos1 = string1.index(string[i])
            pos2 = string2.index(string[i])
            string1 = string1[:pos1] + string1[pos1+1:]
            string2 = string2[:pos2] + string2[pos2+1:]
    return len(string1) + len(string2)


value = "cde"
value2 = "abc"
print(makeAnagram(value, value2))
