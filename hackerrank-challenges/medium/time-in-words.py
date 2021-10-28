# Problem Link: https://www.hackerrank.com/challenges/the-time-in-words/problem


def timeInWords(h, m):
    m = int(m)
    units = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
             8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
             14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
             19: 'nineteen', 20: 'twenty', 21: 'twenty one', 22: 'twenty two', 23: 'twenty three',
             24: 'twenty four', 25: 'twenty five', 26: 'twenty six', 27: 'twenty seven',
             28: 'twenty eight', 29: 'twenty nine'}

    if m == 0:
        return units[h] + " o' clock"
    elif m == 15:
        return 'quarter past ' + units[h]
    elif m == 30:
        return 'half past ' + units[h]
    elif m == 45:
        return 'quarter to ' + units[h + 1]
    elif m < 30:
        if m == 1:
            return '{} minute past {}'.format(units[m], units[h])

        return '{} minutes past {}'.format(units[m], units[h])
    else:
        diff = 60-m
        if diff == 1:
            return '{} minutes to {}'.format(units[diff], units[h + 1])

        return '{} minutes to {}'.format(units[diff], units[h + 1])


print(timeInWords(5, 47))
