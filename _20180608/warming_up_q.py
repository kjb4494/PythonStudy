
import string
import pprint

def q_01():
    def tmp(number):
        if number == 0:
            return 0
        return ((number % 10) * (number % 10)) + tmp(number//10)

    try:
        number = int(input("숫자 입력: "))
    except:
        print("입력 오류")
    else:
        if len(str(number)) > 9:
            print("범위 초과")
            return
        print(tmp(number))

def q_02():
    apList = list(string.ascii_uppercase)
    limitNumber = len(apList)
    try:
        mtrxSize = int(input("배열 크기 입력: "))
    except:
        print("입력 오류")
    else:
        matrix = [[' ']*mtrxSize for i in range(mtrxSize)]

        moveCount = 0
        for i in range(mtrxSize):
            for j in range(mtrxSize - i):
                matrix[i + j][mtrxSize - j - 1] = apList[moveCount % limitNumber]
                moveCount += 1
        pprint.pprint(matrix)


def warming_up_output():
    # q_01()
    q_02()