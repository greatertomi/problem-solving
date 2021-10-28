# Problem Link: https://www.hackerrank.com/challenges/strange-code/problem


def strangeCounter(t):
    count = 1
    currentStater = 3
    timer = currentStater
    while count <= t:
        if count == t:
            return timer
        timer -= 1
        count += 1
        if timer == 0:
            timer = currentStater * 2
            currentStater = timer


# Better solution
def strangeCounter2(t):
    rem = 3
    while t > rem:
        t = t - rem
        rem *= 2

    return rem - t + 1


print(strangeCounter(9))
