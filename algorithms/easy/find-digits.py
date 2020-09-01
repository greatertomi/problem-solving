# Problem: https://www.hackerrank.com/challenges/find-digits/problem


def findDigits(num):
    numArr = [int(d) for d in str(num)]
    count = 0
    for i in numArr:
        if i != 0 and num % i == 0:
            count += 1
    return count


print(findDigits(12))
print(findDigits(1024))
