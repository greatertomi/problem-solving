def countA(arr):
    count = 0
    for i in arr:
        if 'a' in i:
            count += 1
    return count


def combination(word):
    length = len(word)
    count = []

    for _ in range(length):
        new_word = word[1:] + word[0]
        array = ['', '', '']
        num = 0
        for i in word:
            array[num] += i
            num += 1
            if num == 3:
                num = 1
        word = new_word
        count.append(countA(array))
    return count[0]


string = "babaa"
string2 = "ababa"
print(combination(string))
