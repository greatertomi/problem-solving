def array_manipulation(n, queries):
    arr = [0]*n
    for i in queries:
        arr[i[0] - 1] += i[2]
        if i[1] != len(arr):
            arr[i[1]] -= i[2]

    maxval = 0
    itt = 0
    print(arr)
    for q in arr:
        itt += q
        print(q, itt, maxval)
        if itt > maxval:
            maxval = itt
    return maxval


queries1 = [
    [1, 5, 3],
    [4, 8, 7],
    [6, 9, 1]
]
print(array_manipulation(10, queries1))
