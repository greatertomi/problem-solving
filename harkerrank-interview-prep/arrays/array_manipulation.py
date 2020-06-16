def array_manipulation(n, queries):
    arr = [0 for _ in range(n)]

    for i in range(len(queries)):
        start = queries[i][0]
        end = queries[i][1]
        increment = queries[i][2]

        arr = [arr[i] + increment if start - 1 <= i < end else arr[i] for i in range(0, n)]
        print(arr)

    return max(arr)


queries1 = [
    [1, 5, 3],
    [4, 8, 7],
    [6, 9, 1]
]
queries2 = [
    [1, 2, 100],
    [2, 5, 100],
    [3, 4, 100]
]
print(array_manipulation(10, queries1))
