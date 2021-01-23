# https://app.codility.com/programmers/task/replacing_books/


def calculateReplacement(arr, k):
    count = 0
    for num in range(arr[0], arr[-1] + 1):
        if num in arr:
            count += 1
        elif num not in arr and k > 0:
            count += 1
            k -= 1
        else:
            break
    if k > 0:
        count += k
    return count


def replacingBooks(arr, k):
    value_dict = {}
    for i in range(len(arr)):
        if arr[i] in value_dict:
            value_dict[arr[i]].append(i)
        else:
            value_dict[arr[i]] = [i]
    dist = [calculateReplacement(x, k) for x in value_dict.values()]
    return max(dist)


print(replacingBooks([1, 1, 3, 4, 3, 3, 4], 2))
print(replacingBooks([4, 5, 5, 4, 2, 2, 4], 0))
print(replacingBooks([1, 3, 3, 2], 2))
