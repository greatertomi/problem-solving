def minimum_swaps(arr):
    tmp = arr.copy()
    for i, v in enumerate(arr):
        tmp[v - 1] = i
    count = 0

    for i in range(len(arr) - 1):
        a = arr[i]
        if a != i + 1:
            arr[i] = i + 1
            arr[tmp[i]] = a
            tmp[a - 1] = tmp[i]
            count += 1
    return count


val = [2, 3, 4, 1, 5]
print(minimum_swaps(val))
