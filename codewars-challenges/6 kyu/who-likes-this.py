# https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python


def likes(array):
    if len(array) == 0:
        return 'no one likes this'

    if len(array) == 1:
        return '{} likes this'.format(array[0])

    if len(array) == 2:
        return '{} and {} like this'.format(array[0], array[1])

    if len(array) == 3:
        return '{}, {} and {} like this'.format(array[0], array[1], array[2])

    return '{}, {} and {} other like this'.format(array[0], array[1], len(array) - 2)


print(likes([]))  # must be "no one likes this"
print(likes(["Peter"]))  # must be "Peter likes this"
print(likes(["Jacob", "Alex"]))  # must be "Jacob and Alex like this"
print(likes(["Max", "John", "Mark"]))  # must be "Max, John and Mark like this"
print(likes(["Alex", "Jacob", "Mark", "Max"]))
