def q_05():
    # 정수 2개를 입력받아서 첫 번째 수에는 100을 증가시켜 저장하고
    # 두 번째 수는 10으로 나눈 나머지를 저장한 후
    # 두 수를 차례로 출력하는 프로그램을 작성하시오.
    while True:
        try:
            num1, num2 = map(int, input("두 수 입력: ").split(' '))
            num1 += 100
            num2 %= 10
            print("%d %d" % (num1, num2))
            return
        except Exception as e:
            print("입력 오류!", e)