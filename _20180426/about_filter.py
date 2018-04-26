def filter_test_01():
    def EvenFilter(param):
        if param % 2 == 0:
            return param

    sList = [x for x in range(10, 20)]
    newList = list(filter(EvenFilter, sList))
    print(newList)

def filter_output():
    filter_test_01()