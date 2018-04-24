def q_01():
    # 두 개의 값을 입력받아 사각형, 삼각형 넓이 구하기
    num1, num2 = map(int, input("숫자 입력: ").split(" "))
    print("사각형: {}".format(num1*num2))
    print("삼각형: {}".format(num1*num2/2))