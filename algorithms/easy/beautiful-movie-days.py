# Problem Link: https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem


def beautifulDays(start, end, divisor):
    count = 0
    for i in range(start, end + 1):
        reverseNum = int(str(i)[::-1])
        if abs(i - reverseNum) % divisor == 0:
            count += 1
    return count


start1 = 20
end1 = 23
div1 = 6
print(beautifulDays(start1, end1, div1))
