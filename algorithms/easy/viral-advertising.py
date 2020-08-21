# Problem Link: https://www.hackerrank.com/challenges/strange-advertising/problem


def viralAdvertising(n):
    count = 0
    likers = 5
    for i in range(n):
        count += likers//2
        likers = (likers//2) * 3
    return count


viralAdvertising(5)
