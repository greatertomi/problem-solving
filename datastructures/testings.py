from collections import Counter


def compression(word):
    str_count = Counter(word)
    new_str = ""
    for i in str_count:
        if str_count[i] > 1:
            new_str += str(str_count[i])
        new_str += i

    return new_str


def removal(word, k):
    min_length = 0
    for p in range(len(word) - k):
        new_word = None
        if p == 0:
            new_word = word[p+k:]
            comp = compression(new_word)
            word_len = len(comp)
            if min_length == 0:
                min_length = word_len
            else:
                if word_len < min_length:
                    min_length = word_len
        else:
            new_word = word[:p] + word[p+k:]
            comp = compression(new_word)
            word_len = len(comp)
            if min_length == 0:
                min_length = word_len
            else:
                if word_len < min_length:
                    min_length = word_len
    return min_length


string = "AAAAAAAAAAABXXAAAAAAAAAA"
string2 = "ABBBCCDDCCC"
print(removal(string, 3))
# print(compression(string))
# print(compression(string2))
# print(new_str)
