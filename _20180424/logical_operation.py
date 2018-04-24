def lo_test_01():
    # 논리 연산자 - 비트 연산자 구분할 것!
    print(10 or 0)      # 10
    print(0 or 10)      # 10
    print(0 and 10)     # 0
    print(12 and 14)    # 14
    print(12 or 14)     # 12
    print("" or "hello wolrd")      # hello wolrd
    print([] and [10, 20, 30])      # []

def lo_test_02():
    s = "asfsagavsdaghszd"
    if 'z' in s:
        print("z가 있습니다.")
    else:
        print("z가 없습니다.")

def lo_test_03():
    sList = [n for n in range(10, 21)]
    if 12 in sList:
        print(sList.index(12))
    else:
        print("not exist")

def lo_output():
    # lo_test_01()
    # lo_test_02()
    lo_test_03()