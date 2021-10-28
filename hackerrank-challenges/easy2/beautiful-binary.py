# Problem Link: https://www.hackerrank.com/challenges/beautiful-binary-string/problem


def beautifulBinary(binary):
    count = 0
    binArr = list(binary)
    for i in range(2, len(binary)):
        if int(binArr[i-1]) == 1 and int(binArr[i-2]) == 0 and int(binArr[i]) == 0:
            binArr[i] = 1
            count += 1
    print(count)


def beautifulBinary2(binary):
    binary = binary.replace('010', '191')
    return binary.count('9')


def beautifulBinary3(binary):
    return binary.count('010')


binary1 = '0101010'
binary2 = '01100'
binary3 = '0100101010'
# binary1 = binary1.replace('010', '191')
# print(binary2.count('0'))
print(beautifulBinary2(binary1))
print(beautifulBinary2(binary2))
print(beautifulBinary2(binary3))
