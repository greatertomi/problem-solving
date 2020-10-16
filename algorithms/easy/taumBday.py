# Problem Link: https://www.hackerrank.com/challenges/taum-and-bday/problem


def taumBday(b, w, bc, wc, z):
    return b * min(bc, wc + z) + w * min(wc, bc + z)


print(taumBday(5, 9, 2, 3, 4))
print(taumBday(3, 6, 9, 1, 1))
print(taumBday(7, 7, 4, 2, 1))
print(taumBday(3, 3, 1, 9, 2))
