# Problem Link: https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem


def whatFlavours(cost, money):
    valueDict = {}
    for i in cost:
        if i in valueDict:
            valueDict[i] += 1
        else:
            valueDict[i] = 1

    cost1 = None
    cost2 = None
    for num in cost:
        if num * valueDict[num] == money:
            cost1 = cost2 = num
            print('here1')
            break
        elif money - num in valueDict and money - num != num:
            cost1 = num
            cost2 = money - num
            print('here2', cost1, cost2)
            break
    print(cost1, cost2)
    index1 = cost.index(cost1) + 1

    index2 = cost[index1:].index(cost2) + index1 + 1
    print(index1, index2)


# print(whatFlavours([1, 4, 5, 3, 2], 4))
# print(whatFlavours([2, 2, 4, 3], 4))
print(whatFlavours([4, 3, 2, 5, 7], 8))
