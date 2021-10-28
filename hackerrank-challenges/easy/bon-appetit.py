# Bon Appetit: https://www.hackerrank.com/challenges/bon-appetit/problem


def bonAppetit(bill, didntEat, annaPay):
    realBill = (sum(bill) - bill[didntEat])//2
    if annaPay == realBill:
        return 'Bon Appetit'
    else:
        return abs(realBill - annaPay)


bill1 = [3, 10, 2, 9]
dE1 = 1
aP1 = 7

print(bonAppetit(bill1, dE1, aP1))
