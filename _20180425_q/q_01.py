def q_01():
    # 문제: http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=437&sca=20
    # 버블정렬
    while True:
        try:
            nCount = int(input("숫자 갯수 입력: "))
            if not 4 <= nCount <= 100:
                print("4에서 100사이의 수로 입력해주세요.")
                continue
        except Exception as e:
            print("입력 에러!", e)
            continue
        try:
            nList = [i for i in map(int, input("정수 입력: ").split(' ')) if 0 <= i <= 100]
            if len(nList) != nCount:
                print("입력 범위가 잘못되었습니다.")
                continue
        except Exception as e:
            print("입력 에러!", e)
            continue
        bubble_sort(nList)
        return


def bubble_sort(nList):
    for i in range(len(nList) - 1):
        for j in range(len(nList) - 1):
            if nList[j] > nList[j + 1]:
                nList[j], nList[j + 1] = nList[j + 1], nList[j]
        print(" ".join([str(i) for i in nList]))