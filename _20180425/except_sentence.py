def except_test_01():
    try:
        value1, value2 = map(int, input(": ").split(' '))
    except Exception as e:
        print("잘못된 입력입니다.", e)
    else:
        print(">" if value1 > value2 else "<" if value1 < value2 else "=")

def except_output():
    except_test_01()