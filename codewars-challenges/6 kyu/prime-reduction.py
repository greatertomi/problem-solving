# Problem Link: https://www.codewars.com/kata/59aa6567485a4d03ff0000ca


def breakdownNumber(num):
    currentNum = num
    count = 0
    while currentNum > 1:
        currentNum = sum([int(x) ** 2 for x in str(currentNum)])
        count += 1
        if count > 80:
            break
    return currentNum == 1


def isPrime(num):
    if num == 1:
        return False

    result = True
    for i in range(2, num//2):
        if num % i == 0:
            result = False
            break
    return result


def primeReduction(start, end):
    primes = [x for x in range(start, end) if isPrime(x)]
    results = [breakdownNumber(x) for x in primes]
    return results.count(True)


print(breakdownNumber(23))
# print(primeReduction(1, 25))
# print(primeReduction(100, 1000))
# print(primeReduction(100, 2000))
# print(primeReduction(100, 3000))
# print(primeReduction(100, 4000))

