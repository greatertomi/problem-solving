# https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python


def oddInt(arr):
    value_dict = {}
    for val in arr:
        if val in value_dict:
            value_dict[val] += 1
        else:
            value_dict[val] = 1
    values = list(value_dict.values())
    odd = [x for x in values if x % 2 == 1]
    return list(value_dict.keys())[values.index(odd[0])]


arr1 = [20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]
arr2 = [1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]
arr3 = [20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]
arr4 = [10]
arr5 = [1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1]
arr6 = [5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10]
print(oddInt(arr1))
print(oddInt(arr2))
print(oddInt(arr3))
print(oddInt(arr4))
print(oddInt(arr5))
print(oddInt(arr6))
