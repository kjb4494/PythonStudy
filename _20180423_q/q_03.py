def q_03():
    # 단어와 문자 한 개를 입력받아서 단어에서
    # 입력받은 문자와 같은 문자를 찾아서 그 위치를 출력하는 프로그램을 작성하시오.
    # 단어에서 첫 번째 문자의 위치는 0으로 하고 찾는 문자가
    # 여러 개일 때는 처음 나오는 위치를 출력한다.
    # 만약 찾는 문자가 없을 때는 "No"라고 출력한다.
    # 대소문자는 구별되며 단어는 100자 이하이다.
    while True:
        try:
            str1, str2 = input("문자 단어 입력: ").split(' ')
            if len(str2) != 1:
                print("문자는 하나만 입력하세요.")
                continue
            if not 1 <= len(str1) <= 100:
                print("문자열은 100자 이하로 써주세요.")
                continue
            str_location = str1.find(str2)
            if str_location != -1:
                print(str_location)
                return
            else:
                print("NO")
                return
        except Exception as e:
            print("잘못된 입력입니다.", e)