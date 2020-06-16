def minimum_bribe(value):
    counter = 0
    for i in range(len(value)):
        # print(value[i], i + 1)
        if value[i] - i + 1 > 2:
            print('Too chaotic')
            return

        for j in range(max(0, value[i] - 2), i):
            if value[j] > value[i]:
                counter += 1
    print(counter)


chaos = [2, 1, 5, 3, 4]
chaos3 = [2, 5, 1, 3, 4]
chaos2 = [1, 2, 5, 3, 7, 8, 6, 4]
minimum_bribe(chaos2)
