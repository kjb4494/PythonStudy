
def list_test_01():
    """
    # 다음과 같이 선언 가능
    sList = list()
    sList = []
    sList = [10, 20, 30, 40, 50]
    """

    # 리스트도 음수 인덱스가 있다.
    sList = [10, 20, 30, 40, 50]
    print(sList[2])     # 30
    print(sList[-3])    # 30

    # 반복문을 사용하여 리스트 요소 값 출력
    for i in sList:
        print(i, end=' ')

    print()

    # 반복문을 사용하여 리버스하기
    for i in range(0, len(sList), 1):
        print(sList[len(sList)-i-1], end=' ')

    print()

    # 20부터 40까지 음수인덱스 섞어서 코딩
    print(" ".join(str(i) for i in sList[1:-1]))

    # 특정 인덱스의 리스트 요소 값 바꾸기
    sList[0] = 100
    sList[2:4] = ['A', 'B']
    print(sList)

    # 이런식의 적재는 불가능하다!
    # for i in range(0, 10):
    #     sList[i] = i + 10
    # print(sList)

def q_01():
    # 문자 10개를 저장할 수 있는 배열을 만들고
    # 10개의 문자를 입력받아 입력받은 문자를 이어서
    # 출력하는 프로그램을 작성하시오.
    sList = input("10개 문자 입력: ").split(' ')[:10]
    print("".join(sList))

def q_02():
    # 10개의 문자를 입력받아서
    # 첫 번째 네 번째 일곱 번째 입력받은 문자를
    # 차례로 출력하는 프로그램을 작성하시오.
    sList = [i for i in map(str, input("10개 문자 입력: ").split(' '))][:10]
    print("{} {} {}".format(sList[0], sList[3], sList[6]))

def q_03():
    # 100 개의 정수를 저장할 수 있는 배열을 선언하고
    # 정수를 차례로 입력받다가 0 이 입력되면 0 을 제외하고
    # 그 때까지 입력된 정수를 가장 나중에 입력된 정수부터
    # 차례대로 출력하는 프로그램을 작성하시오.
    sList = [i for i in map(int, input("정수 입력: ").split(' '))][:100]
    index = 0
    for i in range(len(sList)):
        if sList[i] == 0:
            break
        else:
            index += 1
    print(sList[:index])

def list_test_02():
    # List 요소 삭제하기
    sList = [10, 20, 30]
    del sList[0]
    print(sList)        # [20, 30]

def list_test_03():
    # List의 각종 함수들
    sList = list()
    
    # append 함수 (요소 추가)
    sList.append(10)
    sList.append(12)
    sList.append(15)
    print(sList)

    # pop 함수 (요소 제거)
    sList.pop(1)
    print(sList)

    # extend 함수 (복수 요소 추가)
    sList.extend([40, 30, 10])
    print(sList)

    # remove 함수
    # 특정 값을 가진 요소 중 제일 첫 번째를 삭제한다.
    # 없을 시 에러난다.
    try:
        sList.remove(40)
        sList.remove(41)        # Error! list.remove(x): x not in list
    except Exception as e:
        print("Error!", e)
    print(sList)

    # index 함수
    # 특정 값을 가진 요소 중 제일 첫 번째의 인덱스 값을 출력한다.
    # 없을 시 에러난다.
    try:
        print(sList.index(30))  # 2
        print(sList.index(60))  # Error! 60 is not in list
    except Exception as e:
        print("Error!", e)

    try:
        print(sList.index(30, 3))  # 범위는 인덱스 3에서 부터 search
    except Exception as e:
        print("Error!", e)
    try:
        print(sList.index(30, 3, 10))  # 범위는 인덱스 3에서 부터 10까지 search
    except Exception as e:
        print("Error!", e)

def list_test_04():
    # List의 주소할당에 대하여...
    sList = [i * 100 for i in range(30)]
    for i in range(len(sList)):
        print(i, hex(id(sList[i])))

def list_output():
    # list_test_01()
    # q_01()
    # q_02()
    # q_03()
    # list_test_02()
    # list_test_03()
    list_test_04()