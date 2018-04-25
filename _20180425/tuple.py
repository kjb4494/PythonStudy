def tuple_test_01():
    # 순차적으로 접근가능한 데이터
    # 구조적인 특징
    #   - 생성, 삭제, 수정이 불가능
    #       - 클라이언트 정보(이름, 주민등록번호, 성별) 등에 사용
    #       - 제공되는 함수의 갯수가 적다.
    #       - 속도(처리속도)가 빠르다.

    # 초기 선언
    tValue = tuple()
    print(tValue)
    tValue = 12,
    print(type(tValue))  # tuple

    print()

    sTuple = 'a', 'b', 'c', 'd', 'e'
    print(type(sTuple))  # tuple
    sTuple = ('a', 'b', 'c', 'd', 'e')
    print(type(sTuple))  # tuple

    print()

    # 문제 !
    # 튜플일까?
    t1 = (1)
    print(type(t1))  # int
    t2 = (1,)
    print(type(t2))  # tuple
    t3 = tuple("hello wolrd")
    print(t3)  # ('h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'l', 'r', 'd')
    print(type(t3))  # tuple


def tuple_test_02():
    # 데이터 접근 방법
    # index 접근 가능 (왜냐하면 시퀸스 타입이기 때문에)
    t1 = tuple("hello wolrd")
    print(t1[4])

    # 반복문으로 데이터 접근
    for i in t1:
        print(i, end=" ")
    print()

    # 슬라이싱으로 데이터 접근 가능
    print(t1[2:6])


def tuple_test_03():
    # 튜플의 연산
    t1 = 1, 2, 3
    t2 = 4, 5, 6
    t3 = t1 + t2
    print(t3)           # (1,2,3,4,5,6)

    # 튜플의 문자열 연산
    t4 = 'a', 'b', 'c'
    print(t4 * 3)       # ('a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c')


def tuple_test_04():
    # packing
    sTuple = 10, 20, 30, 40

    # unpacking
    a, b, _, _ = sTuple     # _는 값을 선언하지 않겠다는 뜻
    print(a, b)

    # swap
    a, b = 10, 20
    a, b = b, a
    print(a, b)

    divV = {1: 'A', 2: 'B', 3: 'C'}
    for s in divV.items():
        print(type(s), "k: ", s[0], "v: ", s[1])

def tuple_output():
    # tuple_test_01()
    # tuple_test_02()
    # tuple_test_03()
    tuple_test_04()
