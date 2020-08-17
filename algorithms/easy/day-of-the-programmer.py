# Problem Link: https://www.hackerrank.com/challenges/day-of-the-programmer/problem


def leapYearCheck(year):
    if year < 1918:
        if year % 4 == 0:
            return True
        else:
            return False
    elif year > 1918:
        if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
            return True
        else:
            return False


def dayOfProgrammer(year):
    preDays = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31
    if year == 1918:
        preDays -= 13
    elif leapYearCheck(year):
        preDays += 1
    day = 256 - preDays
    print(preDays)
    return '{}.09.{}'.format(day, year)


print(dayOfProgrammer(2000))
