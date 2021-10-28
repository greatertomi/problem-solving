# Problem Link: https://www.hackerrank.com/challenges/absolute-permutation/problem
from itertools import permutations


# My Solution
def absolutePermutation(num, k):
    values = [x for x in range(1, num + 1)]
    perms = list(permutations(values))
    perfectPerm = None
    broke = None

    for perm in perms:
        broke = False
        for i in range(len(perm)):
            if abs(i+1 - perm[i]) != k:
                broke = True
                break

        if broke is False:
            perfectPerm = list(perm)
            break
    if broke is False:
        print(*perfectPerm)
    else:
        print("-1")


# Better Solution
def absolutePermutation2(num, k):
    if k == 0:
        print(*list(range(1, num + 1)))
    elif (num/k) % 2 != 0:
        return -1
    else:
        add = True
        perm = []

        for i in range(1, num + 1):
            if add:
                perm.append(i+k)
            else:
                perm.append(i-k)

            if i % k == 0:
                if add:
                    add = False
                else:
                    add = True
        print(*perm)


print(absolutePermutation2(4, 2))
print(absolutePermutation2(2, 1))
print(absolutePermutation2(3, 0))
print(absolutePermutation2(3, 2))
