def q_03():
    # 승지는 주사위 놀이를 하다가 주사위를 10번 던져서
    # 각 숫자가 몇 번씩 나왔는지 알아보려고 한다.
    # 한번 던질 때마다 나온 주사위의 숫자를 입력받아서
    # 각 숫자가 몇 번씩 나왔는지 출력하는 프로그램을 작성하시오.
    while True:
        try:
            sList = [i for i in map(int, input("정수 10개 입력: ").split(' ')) if 1 <= i <= 6][:10]
            if sList[9] is None:
                continue
            rList = [0, 0, 0, 0, 0, 0]
            for i in sList:
                rList[i-1] += 1
            print(''.join([str(i+1) + " : " + str(rList[i]) + "\n" for i in range(len(rList))]))
            return
        except Exception as e:
            print("입력 값이 잘못되었습니다.", e)