def q_04():
    # 두 정수를 입력으로 받아
    #     앞수가 뒷수 보다 크면 >
    #     앞수가 뒷수 보다 작으면 <
    #     같으면 =
    # 를 출력하는 프로그램을 작성하세요.
    while True:
        try:
            num1, num2 = map(int, input("두 정수 입력: ").split(' '))
            if num1 > num2:
                print(">")
            elif num1 < num2:
                print("<")
            else:
                print("=")
            return
        except Exception as e:
            print("입력 값이 잘못되었습니다.", e)