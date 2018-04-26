def fanc_test_01():
    # 여러 개의 리턴값은 튜플 형태로 보내진다.
    def f():
        return 10, 20, 30, 40  # tuple

    print(f())


def fanc_test_02():
    print((lambda x: x ** 2)(10))

    sData = list(map(lambda x: x ** 2, range(10)))
    sData = [x ** 2 for x in range(10)]
    print(sData)


def fanc_test_03():
    def f1():
        return 10

    def f2():
        x = 11
        return x + f1()

    def f3(x=f2()):
        return x

    print(f3())


def fanction_output():
    # fanc_test_01()
    # fanc_test_02()
    fanc_test_03()
