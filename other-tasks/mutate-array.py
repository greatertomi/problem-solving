def mutateArray(n, a):
    if len(a) == 1:
        return a

    newArr = []
    for i in range(len(a)):
        if i == 0:
            newArr.append(0 + a[i] + a[i+1])
        elif i == n-1:
            newArr.append(a[i-1] + a[i] + 0)
        else:
            newArr.append(a[i-1] + a[i] + a[i+1])
    print(newArr)


a1 = [4, 0, 1, -2, 3]
a2 = [9, 2]
mutateArray(2, a2)
