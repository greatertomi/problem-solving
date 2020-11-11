# Problem Link: https://www.hackerrank.com/challenges/separate-the-numbers/problem


def sequential(string, sub_string):
    if not string:
        return True
    if string.startswith(sub_string):
        length = len(sub_string)
        return sequential(string[length:], str(int(sub_string) + 1))
    return False


def handleSeparation(string):
    for i in range(1, len(string)//2 + 1):
        sub_string = string[:i]
        if sequential(string, sub_string):
            return 'YES ' + sub_string
    return 'NO'


def separateNumbers(string):
    print(handleSeparation(string))


# A more elegant solution
def separateNumbers2(string):
    length = len(string)
    for i in range(1, length // 2 + 1):
        check = string[:i]
        add = int(check)
        while check in string:
            add += 1
            check += f'{add}'
            if check == string:
                break
        else:
            continue
        print('YES', string[:i])
        break
    else:
        print('NO')


string1 = '99910001001'
string2 = '7891011'
string3 = '9899100'
string4 = '999100010001'

separateNumbers2(string1)
separateNumbers2(string2)
separateNumbers2(string3)
separateNumbers2(string4)
