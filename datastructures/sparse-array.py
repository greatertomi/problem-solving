from collections import Counter


def matching_string(strings, queries):
    count = []
    num = Counter(strings)
    for char in queries:
        count.append(num[char])
    print(count)


s1 = ['aba', 'baba', 'aba', 'xzxb']
s2 = ['aba', 'xzxb', 'ab']
a1 = ['def', 'de', 'fgh']
a2 = ['de', 'lmn', 'fgh']
b1 = ['abcde', 'sdaklfj', 'asdjf', 'na', 'basdn', 'sdaklfj', 'asdjf', 'na', 'asdjf', 'na', 'basdn', 'sdaklfj', 'asdjf']
b2 = ['abcde', 'sdaklfj', 'asdjf', 'na', 'basdn']
matching_string(b1, b2)
