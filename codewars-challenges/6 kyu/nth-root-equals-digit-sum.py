# Problem Link: https://www.codewars.com/kata/60416d5ee50db70010e0fbd4

def digitSum(n):
    array = []
    for i in range(1, 696):
        if sum([int(i) for i in str(i**n)]) == i:
            array.append(i**n)
    return array


print("here", digitSum(3))
print("testing", [int(i) for i in str(2**10)])
