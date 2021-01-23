# https://www.codewars.com/kata/541c8630095125aba6000c00


def digitalRoot(num):
    num = str(num)
    total = sum([int(x) for x in num])
    if total < 10:
        return total
    else:
        digitalRoot(total)


print(digitalRoot(942))
# print(digitalRoot(942))
# print(digitalRoot(132189))
# print(digitalRoot(493193))
