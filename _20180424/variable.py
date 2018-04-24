import sys

def variable_test_01():
    # http://www.pythontutor.com/ 참고!
    v1 = 5
    v2 = 5
    print(sys.getrefcount(5))
    v3 = 5
    print(sys.getrefcount(5))

    del v1
    print(sys.getrefcount(5))

    print("id(v1) => %#x" % (id(v1)))

def variable_output():
    variable_test_01()