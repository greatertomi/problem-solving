# Problem Link: https://www.hackerrank.com/challenges/big-sorting/problem


def bigSorting(array):
    intArr = list(map(int, array))
    intArr.sort()
    strArr = list(map(str, intArr))

    return strArr


array1 = ['8', '1', '2', '100', '12303479849857341718340192371', '3084193741082937', '3084193741082938', '111', '200']
# print(bigSorting(array1))
print(bigSorting(array1))
