def countTinyPairs(a, b, k):
    count = 0
    for i in range(len(a)):
        value = str(a[i]) + str(b[-(i + 1)])
        if int(value) < k:
            count += 1
    return count


arr1 = [1, 2, 3]
arr2 = [1, 2, 3]
k1 = 31

arr12 = [16, 1, 4, 2, 14]
arr22 = [7, 11, 2, 0, 15]
k2 = 743
print(countTinyPairs(arr12, arr22, k2))

