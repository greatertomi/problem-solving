# Problem Link: https://www.hackerrank.com/challenges/time-conversion/problem


def timeConversion(time):
    timeArr = time.split(':')
    sec = timeArr[-1][0:2]
    geo = timeArr[-1][2:]
    newTimeStr = None
    if geo == 'PM':
        if timeArr[0] == '12':
            newTimeStr = '{}:{}:{}'.format('12', timeArr[1], sec)
        else:
            newTimeStr = '{}:{}:{}'.format(int(timeArr[0]) + 12, timeArr[1], sec)
    elif geo == 'AM':
        if timeArr[0] == '12':
            newTimeStr = '{}:{}:{}'.format('00', timeArr[1], sec)
        else:
            newTimeStr = '{}:{}:{}'.format(timeArr[0], timeArr[1], sec)

    return newTimeStr


timeStr1 = '07:05:45AM'
timeStr2 = '12:30:22AM'
timeStr3 = '12:45:54PM'
print(timeConversion(timeStr3))
