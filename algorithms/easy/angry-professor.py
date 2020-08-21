# Problem Link: https://www.hackerrank.com/challenges/angry-professor/problem


def angryProfessor(arrivalTime, threshold):
    count = 0
    for i in arrivalTime:
        if i <= 0:
            count += 1
    if count >= threshold:
        return 'NO'
    else:
        return 'YES'


arrivalTime1 = [-1, -3, 4, 2]
th1 = 3

arrivalTime2 = [0, -1, 2, 1]
th2 = 2
print(angryProfessor(arrivalTime2, th2))
