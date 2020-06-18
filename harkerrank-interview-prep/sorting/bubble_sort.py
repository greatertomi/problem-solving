def countSwap(arr):
    sortedArr = sorted(arr)
    n = len(arr)
    count = 0

    while arr != sortedArr:
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                count += 1
    print("Array is sorted in {} swaps".format(count))
    print("First Element: {}".format(arr[0]))
    print("Last Element: {}".format(arr[n-1]))


value = [6, 4, 1]
countSwap(value)
"""
Array is sorted in 3 swaps.  
First Element: 1  
Last Element: 6 
"""
