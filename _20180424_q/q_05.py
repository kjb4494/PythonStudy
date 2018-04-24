def q_05():
    # 두 자연수가 주어진다. 두 수 사이의 수(두 수 포함)를
    # 차례대로 출력하는 프로그램을 작성하시오.

    # 입력
    # 두 수가 입력으로 주어진다. 두 수는 100 이하의 자연수이다.

    # 출력
    # 두 수 사이에 공백을 하나 준다.
    while True:
        try:
            num01, num02 = map(int, input("두 자연수 입력: ").split(' '))
            if 0 <= num01 and 0 <= num02:
                if num01 > num02:
                    num01, num02 = num02, num01
                nList = []
                for i in range(num01, num02 + 1):
                    nList.append(str(i))
                print(" ".join(nList))
                return
            else:
                print("자연수를 입력해주세요.")
                continue
        except Exception as e:
            print("입력 값이 잘못되었습니다.", e)