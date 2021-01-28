# Problem Link: https://www.codewars.com/kata/550498447451fbbd7600041c/train/python


def checkSameness(arr1: list, arr2: list):
    if len(arr1) != len(arr2):
        return False

    for val in arr1:
        double = val * val
        if double in arr2:
            arr2.remove(double)
        else:
            return False
    return True


arrayA1 = [121, 144, 19, 161, 19, 144, 19, 11]
arrayA2 = [121, 14641, 20736, 361, 25921, 361, 20736, 361]

arrayB1 = [121, 144, 19, 161, 19, 144, 19, 11]
arrayB2 = [132, 14641, 20736, 361, 25921, 361, 20736, 361]

print(checkSameness(arrayB1, arrayB2))
