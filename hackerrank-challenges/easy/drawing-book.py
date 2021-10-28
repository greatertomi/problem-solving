# Problem Link: https://www.hackerrank.com/challenges/drawing-book/problem


# My answer
def pageCount(num, page):
    if num == page:
        return 0
    fromFront = page//2
    fromBack = num//page
    if num % page == 1:
        fromBack -= 1
    return min(fromFront, fromBack)


# Correct Answer
def pageCount2(num, page):
    return min(page // 2, num // 2 - page // 2)


print(pageCount2(10, 4))
