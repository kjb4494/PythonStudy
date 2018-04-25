def set_test_01():
    # 집합(SET)
    #   - 구조적인 성질:
    #       1) Not Order
    #       2) 중복을 허락하지 않는다.
    #   - 종류                    중요
    #       1) 여집합
    #       2) intersection set => *
    #       3) union set        => *
    #       4) 부분집합
    #       5) difference set   => *
    #       6) 곱집합('.')
    #       7) 대칭 차집합       => *
    #   - 함수
    #       1) add(x)       x: 임의의 수
    #       2) update(y)
    #       3) remove(x)

    # 대칭 차집합: http://j1w2k3.tistory.com/329

    set_A = {10, 11, 12, 13}
    set_B = {11, 13, 15, 17}

    print(type(set_A))  # SET

    # 교집합(Intersection)
    # SET_INTER = set_A.intersection(set_B)
    SET_INTER = set_A & set_B
    print(SET_INTER)  # 11, 13

    # 합집합(Union set)
    # SET_UNI = set_A.union(set_B)
    SET_UNI = set_A | set_B
    print(SET_UNI)  # 10, 11, 12, 13, 15, 17

    # 차집합(Difference set)
    # SET_DIF = set_A.difference(set_B)
    SET_DIF = set_A - set_B
    print(SET_DIF)  # 10, 12

    # 대칭 차집합(sysmmetric deffierence set)
    SET_SYM = set_A ^ set_B
    print(SET_SYM)  # 10, 12, 15, 17

    # 문자열을 집합으로 변환
    set_result = set("hello wolrd hello hello world hello world")
    print(set_result)  # 집합의 구조적 성질: 중복을 허용하지 않는다.

    # 함수사용하기
    setValue = set()  # empty set
    for i in range(0, 10):
        setValue.add(i + 1)
        # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

    # update
    setValue.update(['a', 'b', 'c', 'd', 'd', 'd', 'd'])
    print(setValue)  # 집합은 중복을 허용하지 않는다!

    # remove
    setValue.remove('a')
    print(setValue)


def set_test_02():
    # -10~10 사이의 정수 중, 4개의 수를 입력받는다. : a, b, c, d
    # 집합 A, B가 있고 입력 받은 4개의 정수로
    # 집합 A, B는 아래와 같이 정해진다.
    #       A = {integer x | a <= x <= b}
    #       B = {integer x | c <= x <= d}
    # 이 때, 집합 A와 Bc의 원소를 각각 출력하고
    # A와 Bc의 교집합을 출력하시오.

    while True:
        U = {x for x in range(-10, 11)}
        try:
            a, b, c, d = map(int, input("4개 정수 입력: ").split(' '))
        except:
            print("정수가 아닙니다.")
            continue
        if not (-10 <= a <= 10 and
            -10 <= b <= 10 and
            -10 <= c <= 10 and
            -10 <= d <= 10):
            print("-10에서 10사이의 정수만 입력하세요.")
            continue
        A = {x for x in range(a, b + 1)}
        B = {x for x in range(c, d + 1)}
        print("집합 A : {}".format(A))
        print("집합 Bc : {}".format(U - B))
        print("A와 Bc의 교집합 : {}".format(A & (U - B)))
        return

        # # step 01 -10 ~ 10 사이의 정수 입력 (4개)
        # set_A = set()
        # set_B = set()
        # set_U = set([n for n in range(-10, 11)])
        # # step 01-01 집합 A를 먼저 셋팅
        # a_value1, a_value2 = \
        #     map(int, input("A_set: ").split(' '))
        # # 앞의 값이 뒤에 값 보다 크다면
        # if a_value1 > a_value2:
        #     a_value1, a_value2 = a_value2, a_value1
        # for element in range(a_value1, a_value2 + 1):
        #     set_A.add(element)
        #
        # # step 01-02 집합 B를 셋팅
        # b_value1, b_value2 = \
        #     map(int, input("B_set: ").split(' '))
        # # 앞의 값이 뒤에 값 보다 크다면
        # if b_value1 > b_value2:
        #     b_value1, b_value2 = b_value2, b_value1
        # for element in range(b_value1, b_value2 + 1):
        #     set_B.add(element)
        #
        # # 집합 A와 B의 여집합 출력
        # print("set_A => {}".format(set_A))
        # print("set_B의 여집합 => {}".format(set_U - set_B))
        # result = set_U - set_B
        # print("set_A의 집합과 set_B의 여직합의 교집합은 {}"
        #       .format(result.intersection(set_A)))

def set_output():
    # set_test_01()
    set_test_02()