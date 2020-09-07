# Problem Link: https://www.hackerrank.com/challenges/non-divisible-subset/problem

# Logic
# 1. Create a reminder frequency list, having initial value = 0, size = k
# 2. Initialise the count which will count the max element in a set, in which
#   sum of any two number is not perfectly divisible by k
# 3. Use the index position 0 if number having remainder 0 is added with number
#   remainder is not 0, then their sum will not be perfectly divisible.
# 4. Find the pair whose sum is not perfectly divisible by the given k


def nonDivisibleSubset(k, numbers):
    counts = [0] * k
    for number in numbers:
        counts[number % k] += 1

    count = min(counts[0], 1)
    for i in range(1, k // 2 + 1):
        if i != k - i:
            count += max(counts[i], counts[k - i])
    if k % 2 == 0:
        count += 1

    return count
