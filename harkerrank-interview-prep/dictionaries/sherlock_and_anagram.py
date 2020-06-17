def getAllSubstrings(string):
    substrings = []
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            substrings.append(string[i:j])
    return substrings


def isAnagram(str1, str2):
    strDict = {}
    for i in str1:
        if i in strDict:
            strDict[i] += 1
        else:
            strDict[i] = 1

    for i in str2:
        if i in strDict:
            strDict[i] -= 1
        else:
            return False
    return True


def countAnagrammaticPairs(currentIndex, arr):
    currentElement = arr[currentIndex]
    arrRest = arr[currentIndex+1:]
    counter = 0

    for i in range(len(arrRest)):
        print(currentElement, arrRest)
        if (len(currentElement) == len(arrRest[i])) and (isAnagram(currentElement, arrRest[i])):
            counter += 1
            print(counter)
    return counter


def sherlockAndAnagrams(string):
    substrings = getAllSubstrings(string)
    count = 0
    for i in range(len(substrings)):
        count += countAnagrammaticPairs(i, substrings)
    return count


print(sherlockAndAnagrams("abba"))

