# Problem Link: https://www.hackerrank.com/challenges/cats-and-a-mouse/problem


def catAndMouse(catA, catB, mouseC):
    if abs(catA - mouseC) < abs(catB - mouseC):
        return 'Cat A'
    elif abs(catA - mouseC) > abs(catB - mouseC):
        return 'Cat B'
    else:
        return 'Mouse C'


catA1 = 2
catB1 = 5
mouseC1 = 4

catA2 = 1
catB2 = 2
mouseC2 = 3

catA3 = 1
catB3 = 3
mouseC3 = 2

print(catAndMouse(catA3, catB3, mouseC3))
