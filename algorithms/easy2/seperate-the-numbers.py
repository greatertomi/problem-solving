# Problem Link: https://www.hackerrank.com/challenges/separate-the-numbers/problem


def testing(string):
    width = 2
    i = 0
    nums = []
    while i < len(string):
        num = string[i: i + width]
        nums.append(num)
        if int(nums[-1][-1]) == 9:
            width += len(nums[-1])
            i += len(nums[-1])
        else:
            i += width
        try:
            if int(num) - int(nums[-2]) != 1:
                status = 'NO'
                break
            else:
                status = 'YES'
        except IndexError:
            pass
    print(nums)


def checkForZero(arr):
    for num in arr:
        if int(num[0]) == 0:
            return True

    return False


def separateNumbers(string):
    length = len(string)
    minNum = None
    if length < 2:
        print('NO')
    else:
        status = 'NO'
        for i in range(1, length//2 + 1):
            width = i
            i = 0
            nums = []
            while i < length:
                num = string[i: i + width]
                nums.append(num)
                if int(nums[-1][-1]) == 9:
                    width += len(nums[-1])
                    i += len(nums[-1])
                else:
                    i += width
                try:
                    if int(num) - int(nums[-2]) != 1:
                        status = 'NO'
                        break
                    else:
                        status = 'YES'
                except IndexError:
                    pass
            if status == 'YES' and checkForZero(nums) is False:
                minNum = nums[0]
                break
            print(nums)
        if status == 'YES':
            print(status, minNum)
        else:
            print(status)


string1 = '99910001001'
string2 = '7891011'
string3 = '9899100'
string4 = '999100010001'

testing(string2)
# separateNumbers(string1)
# separateNumbers(string2)
# separateNumbers(string3)
# separateNumbers(string4)
