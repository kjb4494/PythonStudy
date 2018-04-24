def q_07():
    # 문자열(100자 이하)을 입력받은 후 정수를 입력받아
    # 해당위치의 문자를 제거하고 출력하는 작업을 반복하다가
    # 문자 1개가 남으면 종료하는 프로그램을 작성하시오.

    # 첫 번째 문자의 위치는 1이며 만약 입력받은 번호가
    # 문자열의 길이 이상이면 마지막 문자를 제거한다.
    while True:
        input_str = input("문자열 입력: ")
        if len(input_str) == 0 or len(input_str) > 100:
            print("문자열을 제대로 입력해주세요.")
            continue
        while len(input_str) != 1:
            try:
                input_num = int(input("숫자 입력: "))
                if input_num == 0:
                    print("입력값이 잘못되었습니다.")
                    print(input_str)
                elif input_num <= len(input_str):
                    input_str = input_str[:input_num - 1] + input_str[input_num:]
                    print(input_str)
                else:
                    input_str = input_str[:-1]
                    print(input_str)
            except Exception as e:
                print("올바른 숫자를 입력해주세요.", e)
                print(input_str)
        return
