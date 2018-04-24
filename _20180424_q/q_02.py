def q_02():
    # 10개의 정수를 입력받아 그 중 가장 작은 수를
    # 출력하는 프로그램을 작성하시오.(입력받을 정수는 1000을 넘지 않는다.)
    while True:
        try:
            sList = [i for i in map(int, input("정수 10개 입력: ").split(' ')) if i <= 1000][:10]
            if sList[9] is None:
                continue
            print(min(sList))
            return
        except Exception as e:
            print("입력 값이 잘못되었습니다.", e)