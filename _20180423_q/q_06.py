def q_06():
    # 두 개의 정수를 입력받아서
    # 첫 번째 줄에는 두 정수의 값이 같으면 1 아니면 0을 출력하고
    # 두 번째 줄에는 같지 않으면 1 같으면 0을 출력하는 프로그램을 작성하시오.
    while True:
        try:
            num1, num2 = map(int, input("두 정수 입력: ").split(' '))
            if num1 == num2:
                print("1")
            else:
                print("0")
            if num1 != num2:
                print("1")
            else:
                print("0")
            return
        except Exception as e:
            print("입력 오류!", e)