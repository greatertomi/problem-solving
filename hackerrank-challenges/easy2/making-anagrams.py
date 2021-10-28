# Problem Link: https://www.hackerrank.com/challenges/making-anagrams/problem


def makingAnagrams(string1, string2):
    strArr1 = list(string1)
    strArr2 = list(string2)

    count = 0
    for val in strArr1:
        if val in strArr2:
            count += 1
            index = strArr2.index(val)
            del strArr2[index]
    total = len(strArr1) - count + len(strArr2)

    return total


# print(makingAnagrams('abc', 'amnop'))
# print(makingAnagrams('cde', 'abc'))
str1 = 'absdjkvuahdakejfnfauhdsaavasdlkj'
str2 = 'djfladfhiawasdkjvalskufhafablsdkashlahdfa'

# str1 = 'absdjkvuahdak'
# str2 = 'djfladfhiawasdk'
print(makingAnagrams(str1, str2))
