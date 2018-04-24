def if_test_01():
    num_01 = int(input(": "))

    if num_01 % 2 == 0:
        print("Even_number")
    else: # num_01 % 2 == 1
        print("Odd_number")

def if_test_02():
    # 대문자는 소문자로, 소문자는 대문자로 바꾸기
    s = "Kitri Wolrd"
    for i in s:
        if 'a' <= i <= 'z':
            # i.upper()
            print(chr(ord(i) - 32), end="")
        elif 'A' <= i <= 'Z':
            # i.lower()
            print(chr(ord(i) + 32), end="")
        else:
            print(i, end="")

    print()

    # swapcase 활용하기
    print(s.swapcase())

def if_q_01():
    # 두 개의 정수를 입력받아 큰 수에서 작은 수를 뺀 차를 출력하는 프로그램을 작성하시오.
    num01, num02 = map(int, input("두 수를 입력: ").split(' '))
    if num01 > num02:
        print(num01 - num02)
    else:
        print(num02 - num01)

    # 절대값 함수 이용하기
    print(abs(num01 - num02))

def if_q_02():
    # 정수를 입력받아 첫 줄에 입력 받은 숫자를 출력하고
    # 둘째 줄에 음수이면 “minus” 라고 출력하는 프로그램을 작성하시오.
    num01 = int(input("숫자 입력: "))
    print(abs(num01))
    if num01 < 0:
        print("minus")

def if_test_03():
    strValue = ""
    lstValue = []
    tupValue = ()
    dictValue = {}
    intValue = 0

    # 빈 깡통은 if문에서 모두 거짓으로 구분된다.
    if strValue or lstValue or tupValue \
            or dictValue or intValue:
        print("CALL ~1")
    else:
        print("CALL ~2")

    # 출력: CALL ~2

    # 비교 연산자
    # x < y : " y가 x보다 클 경우 " 참
    # x > y : " y가 x보다 작을 경우 " 참
    # x == y : " x와 y가 같을 경우 " 참 ("===")
    # x != y : " x와 y가 다를 경우 " 참
    # x <= y : " y가 x보다 크거나 같을 경우 " 참
    # x >= x : " y가 x보다 작거나 같을 경우 " 참

def if_test_04():
    strValue = ""
    lstValue = []
    tupValue = ()
    dictValue = {}
    intValue = 0

    # 비어있다고 NULL값인건 아니다.
    if strValue is not None or \
            lstValue is not None or \
            tupValue is not None or \
            dictValue is not None or \
            intValue is not None:
        print("CALL ~1")
    else:
        print("CALL ~2")

    # 출력: CALL ~1

def if_sentence_output():
    # if_test_01()
    # if_test_02()
    # if_q_01()
    # if_q_02()
    # if_test_03()
    if_test_04()