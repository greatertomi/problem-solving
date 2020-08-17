# Problem Link: https://www.hackerrank.com/challenges/migratory-birds/problem


def migratoryBirds(arr):
    bird_dict = {}
    for i in arr:
        if i in bird_dict:
            bird_dict[i] += 1
        else:
            bird_dict[i] = 1
    return max(bird_dict, key=bird_dict.get)


arr1 = [1, 1, 2, 2, 3]
arr2 = [1, 4, 4, 4, 5, 3]
arr3 = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]

migratoryBirds(arr3)
