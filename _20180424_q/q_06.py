def q_06():
    # 정수를 입력으로 받아 입력 받은 수를 거꾸로 출력하는 문제이다.

    # 입력
    # 입력의 첫 수는 수의 개수 n 이다. ( 1 <= n <= 1000 )
    # 다음 줄에는 수들이 입력으로 주어진다. 각 수의 범위는 -10000 < n < 10000 이다.

    # 출력
    # 한 줄에 입력받은 수를 거꾸로 출력한다.

    while True:
        try:
            nCount = int(input("입력될 수의 개수: "))
            if not 1 <= nCount <= 1000:
                print("1 이상 1000 이하의 수로 입력하세요.")
                continue
            nList = [i for i in map(int, input("정수 입력: ").split(' ')) if -10000 < i < 10000][:nCount]
            if nList[nCount - 1] is None:
                continue
            print(" ".join([str(i) for i in nList[::-1]]))
            return
        except Exception as e:
            print("입력 값이 잘못되었습니다.", e)