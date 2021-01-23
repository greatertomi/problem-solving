# Problem Link: https://www.codewars.com/kata/59f08f89a5e129c543000069


def removeStringDuplicates(array):
    newValues = []
    for string in array:
        newVal = string[0]
        for val in string:
            if val != newVal[-1]:
                newVal += val
        newValues.append(newVal)
    return newValues


array1 = ["ccooddddddewwwaaaaarrrrsssss", "piccaninny", "hubbubbubboo"]
removeStringDuplicates(array1)
