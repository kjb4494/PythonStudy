def q_01():
    # 문자열을 입력받은 뒤 그 문자열을 이어서 두 번 출력하는 프로그램을 작성하시오.
    # 문자열의 길이는 100이하이다.
    while True:
        try:
            input_string = input("문자열 입력: ")
            if len(input_string) > 100:
                print("문자열이 너무 깁니다.")
                continue
            print(input_string*2)
            return
        except Exception as e:
            print("잘못된 입력입니다.", e)