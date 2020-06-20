def maximumToys(arr, amount):
    arr.sort()
    count = 0
    cost = 0
    for i in arr:
        if cost + i <= amount:
            cost += i
            count += 1
        else:
            break

    return count


prices = [1, 12, 5, 111, 200, 1000, 10]
k = 50
print(maximumToys(prices, k))
