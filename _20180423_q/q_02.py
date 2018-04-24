def q_02():
    # 5개 이상 100개 이하의 문자로 된 단어를 입력받은 후
    # 앞에서부터 5자를 출력하는 프로그램을 작성하시오.
    while True:
        try:
            input_string = input("입력: ")
            if 5 <= len(input_string) <= 100:
                print(input_string[:5])
                return
            else:
                print("5개 이상 100개 이하의 문자를 입력해주세요.")
        except Exception as e:
            print("잘못된 입력입니다.", e)