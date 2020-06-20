from statistics import median


def activityNotification(expenditure, d):
    count = 0
    for i in range(d, len(expenditure)):
        trails = expenditure[i-d:i]
        med = median(trails)
        if expenditure[i] >= med*2:
            count += 1
            print(count)
    return count


value = [2, 3, 4, 2, 3, 6, 8, 4, 5]
value2 = [10, 20, 30, 40, 50]
value3 = [1, 2, 3, 4, 4]
print('final', activityNotification(value3, 4))
