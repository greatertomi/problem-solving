def alternatingCharacters(string):
    new_string = ""
    count = 0
    for i in string:
        if len(new_string) == 0:
            new_string += i
        else:
            if new_string[-1] != i:
                new_string += i
            else:
                count += 1
    return count


value = "AABAAB"
value2 = "AAAA"
value3 = "BBBBB"
value4 = "ABABABAB"
value5 = "BABABA"
value6 = "AAABBB"
print(alternatingCharacters(value2))
print(alternatingCharacters(value3))
print(alternatingCharacters(value4))
print(alternatingCharacters(value5))
print(alternatingCharacters(value6))
