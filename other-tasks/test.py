from random import randint


def multiplication_learning():
    a = randint(0, 9)
    b = randint(0, 9)
    questionList = ['What is {} multiplied by {}'.format(a, b), a*b]
    return questionList


def noiseMaker(status):
    num = randint(0, 3)
    right_response = ['Very Good!', 'Excellent!', 'Nice Work!', 'Keep up the good work!']
    wrong_response = ['No, please try again!', 'Wrong, try once more.', "Don't give up!", 'No. keep trying.']
    if status == 'correct':
        return right_response[num]
    else:
        return wrong_response[num]


currentQuestion = multiplication_learning()
print(currentQuestion[0])
answer = int(input('Enter your answer: '))
counter = 1

while counter < 10:
    if answer == currentQuestion[1]:
        print(noiseMaker('correct'))
        currentQuestion = multiplication_learning()
        print(currentQuestion[0])
        answer = int(input('Enter your answer: '))
        counter += 1
    else:
        print(noiseMaker('wrong'))
        print(currentQuestion[0])
        answer = int(input('Enter your answer: '))


