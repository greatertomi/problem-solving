# Problem length: https://www.hackerrank.com/challenges/divisible-sum-pairs/problem


def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(len(ar)):
        for j in range(i+1, len(ar)):
            if i < j and (ar[i] + ar[j]) % k == 0:
                count += 1
    return count


ar1 = [1, 2, 3, 4, 5, 6]
n1 = 6,
k1 = 5

ar2 = [1, 3, 2, 6, 1, 2]
n2 = 6,
k2 = 3

print(divisibleSumPairs(n2, k2, ar2))
