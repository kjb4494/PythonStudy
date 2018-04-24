def q_04():
    # 세 개의 정수를 입력 받아서 합계와 평균을 출력하시오.
    # (단 평균은 소수 이하를 버리고 정수부분만 출력한다.)
    while True:
        try:
            num1, num2, num3 = map(int, input("정수 세 개 입력: ").split(' '))
            print("합계: %d" % (num1 + num2 + num3))
            print("평균: %d" % ((num1 + num2 + num3) / 3))
            return
        except Exception as e:
            print("올바른 값을 입력하세요.", e)