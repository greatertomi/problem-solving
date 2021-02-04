# Problem Link: https://www.codewars.com/kata/561e9c843a2ef5a40c0000a4/train/python


def isPrime(num):
    if num <= 0 or num == 1:
        return False
    i = 2
    while i <= num ** 0.5:
        if num % i == 0:
            return False
        i += 1
    return True


def gap(num, start, end):
    if start % 2 == 0:
        start += 1
    prev = start
    for i in range(start, end + 1, 2):
        if isPrime(i):
            if i - prev == num:
                return [prev, i]
            else:
                prev = i
    return None


# print(isPrime(4))
print(gap(2, 3, 50))
