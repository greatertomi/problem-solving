def countTriplets(arr, r):
    triplets = []
    arr = sorted(arr)
    n = len(arr)
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                triplets.append((arr[i], arr[j], arr[k]))

    for val in triplets:
        if val[0]*r == val[1] and val[1]*r == val[2]:
            count += 1

    return count


# value = [1, 3, 9, 9, 27, 81]
value2 = [1, 5, 5, 25, 125]
print(countTriplets(value2, 5))
