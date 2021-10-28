# Problem Link: https://www.hackerrank.com/challenges/reduced-string/problem


def reducedOnce(string):
    reduced = ''
    i = 0
    while i <= len(string):
        if i == len(string) - 1:
            reduced += string[-1]
            break
        else:
            try:
                if string[i] == string[i + 1]:
                    i += 2
                else:
                    reduced += string[i]
                    i += 1
            except IndexError:
                if reduced == '':
                    reduced = 'Empty String'
                break
    return reduced


def superReducedString(string):
    initial = reducedOnce(string)
    # print('1', initial)
    while initial != reducedOnce(initial):
        initial = reducedOnce(initial)
    return initial


print(superReducedString('aaabccddd'))
print(superReducedString('kagoyzkgfjnyvjewazalxngpdcfahneqoqgiyjgpzobhaghmgzmnwcmeykqzgajlmuerhhsanpdtmrzibswswzjjbjqytgfewiuu'))
print(superReducedString('aa'))
print(superReducedString('baab'))
