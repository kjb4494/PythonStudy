
def sort_test_01():
    # 정렬 (SORTED)


    # 구현할 수 있어야한다.

    # 1. 버블정렬
    #   Index   0   1   2   3
    #   Value   4   3   2   1
    #   1cyc    3   4   2   1
    #           3   2   4   1
    #           3   2   1   4
    #   2cyc    2   3   1   4
    #           2   1   3   4
    #   3cyc    1   2   3   4

    # 2. 삽입

    # 3. 병합

    # 4. 퀵

    vList = [40, 30, 20, 10]

    # 방법1: 정렬알고리즘
    # 방법2: 내장함수 : sort()

    # 오름차순 정렬
    vList.sort()
    print("오름 차순에 대한 결과 {re}".format(re=vList))

    # 내림차순 정렬
    vList.sort(reverse=True)
    print("내림 차순에 대한 결과 {re}".format(re=vList))

    vList.reverse()
    print(vList)
    print("{0}".format(vList))

def sort_test_02():

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

    # 대칭 차집합: http://j1w2k3.tistory.com/329

    set_A = {10, 11, 12, 13}
    set_B = {11, 13, 15, 17}

    print(type(set_A))  # SET

    # 교집합(Intersection)
    # SET_INTER = set_A.intersection(set_B)
    SET_INTER = set_A & set_B
    print(SET_INTER)        # 11, 13

    # 합집합(Union set)
    # SET_UNI = set_A.union(set_B)
    SET_UNI = set_A | set_B
    print(SET_UNI)          # 10, 11, 12, 13, 15, 17

    # 차집합(Difference set)
    # SET_DIF = set_A.difference(set_B)
    SET_DIF = set_A - set_B
    print(SET_DIF)          # 10, 12

    # 대칭 차집합(sysmmetric deffierence set)
    SET_SYM = set_A ^ set_B
    print(SET_SYM)          # 10, 12, 15, 17

    # 문자열을 집합으로 변환
    set_result = set("hello wolrd hello hello world hello world")
    print(set_result)       # 집합의 구조적 성질: 중복을 허용하지 않는다.

def sort_output():
    # sort_test_01()
    sort_test_02()