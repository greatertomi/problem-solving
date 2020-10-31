# Problem Link: https://www.hackerrank.com/challenges/strong-password/problem


def strongPassword(password: str):
    numCheck = False
    lcCheck = False
    ucCheck = False
    scCheck = False
    lenCheck = False
    requiredLen = 0
    if len(password) > 6:
        lenCheck = True
    for char in password:
        if char.isupper():
            ucCheck = True
        elif char.islower():
            lcCheck = True
        elif char.isnumeric():
            numCheck = True
        elif char.isalnum() is False:
            scCheck = True

    if numCheck is False:
        requiredLen += 1
    if lcCheck is False:
        requiredLen += 1
    if scCheck is False:
        requiredLen += 1
    if ucCheck is False:
        requiredLen += 1
    print(numCheck, lcCheck, scCheck, ucCheck, lenCheck, requiredLen)
    if lenCheck is False and len(password) + requiredLen < 6:
        needed = 6 - len(password)
        requiredLen += needed - requiredLen
    return requiredLen


password1 = 'Ab1'
password2 = '#HackerRank'
password3 = '4700'
print(strongPassword(password3))
