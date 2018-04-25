
def sort_test():
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

def sort_output():
    sort_test()
