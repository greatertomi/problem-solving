# Problem Link: https://www.hackerrank.com/challenges/lisa-workbook/problem


def lisaWorkbook(n, k, arr):
    current_page = 1
    count = 0
    for i in arr:
        num = 1
        while num <= i:
            if num == current_page:
                count += 1
            if num % k == 0:
                current_page += 1
            num += 1
        if i % k != 0:
            current_page += 1
    return count


n1 = 5
k1 = 3
arr1 = [4, 2, 6, 1, 10]

n2 = 10
k2 = 5
arr2 = [3, 8, 15, 11, 14, 1, 9, 2, 24, 31]

print(lisaWorkbook(n2, k2, arr2))
