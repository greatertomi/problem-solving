# Problem Link: https://www.hackerrank.com/challenges/append-and-delete/problem


def appendAndDelete(s, t, k):
    if len(s) + len(t) <= k:
        return 'Yes'
    point = None

    for i in range(0, max(len(s), len(t))):
        try:
            if s[i] != t[i]:
                point = i
                break
        except IndexError:
            point = i
            break

    if point is None:
        count_diff = abs(len(s) - len(t))
    else:
        count_diff = (len(s) - point) + (len(t) - point)

    if count_diff <= k:
        return 'Yes'
    else:
        return 'No'


s1 = 'hackerrank'
t1 = 'hackerhappy'
k1 = 9

s2 = 'ashley'
t2 = 'ash'
k2 = 2

s3 = 'qwerasdf'
t3 = 'qwerbsdf'
k3 = 6

s4 = 'zzzzz'
t4 = 'zzzzzzz'
k4 = 4

s5 = 'y'
t5 = 'yu'
k5 = 2
print(appendAndDelete(s5, t5, k5))
