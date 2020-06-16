def minimum_swap(arr):
    sorted_arr = sorted(arr)
    swaps = 0
    i = 0
    while sorted_arr != arr:
        original_index = sorted_arr.index(arr[i])
        if i != original_index:
            sw1 = arr[i]
            sw2 = arr[original_index]
            arr[i] = sw2
            arr[original_index] = sw1
            swaps += 1
            i = 0
        else:
            i += 1
            print('after', arr, i)
    print(swaps)


val = [7, 1, 3, 2, 4, 5, 6]
val2 = [4, 3, 1, 2]
val3 = [2, 3, 4, 1, 5]
minimum_swap(val3)
