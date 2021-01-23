# Problem Link: https://www.codewars.com/kata/5825792ada030e9601000782


def zipWith(fn, arr1, arr2):
    size = min(len(arr1), len(arr2))
    result = []
    for i in range(size):
        result.append(fn(arr1[i], arr2[i]))
    return result


print(zipWith(lambda a, b: a + b, [0, 1, 2, 3, 4], [6, 5, 4, 3, 2, 1]))
