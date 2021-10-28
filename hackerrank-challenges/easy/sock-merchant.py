# Problem Link: https://www.hackerrank.com/challenges/sock-merchant/problem


def sockMerchant(arr):
    socks_map = {}
    count_socks = 0
    for val in arr:
        if val in socks_map:
            if socks_map[val] == 1:
                count_socks += 1
                socks_map[val] = 0
            else:
                socks_map[val] += 1
        else:
            socks_map[val] = 1
    return count_socks


arr1 = [1, 2, 1, 2, 1, 3, 2]
print(sockMerchant(arr1))
