# Problem Link: https://www.hackerrank.com/challenges/kangaroo/problem


def kangaroo(x1, v1, x2, v2):
    if (x2 > x1 and v2 > v1) or (x1 > x2 and v1 > v2):
        return 'NO'
    pos1 = x1
    pos2 = x2
    count = 0
    while (pos1 != pos2) and (count < 1000):
        pos1 += v1
        pos2 += v2
        count += 1
        print(pos1, pos2)
    if pos1 == pos2:
        return 'YES'
    else:
        return 'NO'


k1 = [0, 3, 4, 2]
k2 = [0, 2, 5, 3]
# print(kangaroo(k1[0], k1[1], k1[2], k1[3]))
print(kangaroo(k2[0], k2[1], k2[2], k2[3]))
