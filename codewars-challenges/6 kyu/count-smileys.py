# https://www.codewars.com/kata/583203e6eb35d7980400002a/train/python


def countSmileys(arr):
    if len(arr) == 0:
        return 0

    smileys = [':)', ';)', ':D', ';)', ':-)', ':-D', ':~)', ':~D', ';-)', ';-D', ';~)', ';~D']
    count = 0
    for char in arr:
        if char in smileys:
            count += 1
    return count


arr1 = []
arr2 = [':D', ':~)', ';~D', ':)']
arr3 = [':)', ':(', ':D', ':O', ':;']
arr4 = [';]', ':[', ';*', ':$', ';-D']

print(countSmileys(arr1))
print(countSmileys(arr2))
print(countSmileys(arr3))
print(countSmileys(arr4))
