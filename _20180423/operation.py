aValue = 100
bValue = 11

# 파이썬에서의 사칙연산

def operation_add():
    print("{} + {} = {}".format(aValue, bValue, aValue+bValue))
    print("%d + %d = %d" %(aValue, bValue, aValue+bValue))

def operation_sub():
    print("{} - {} = {}".format(aValue, bValue, aValue-bValue))
    print("%d - %d = %d" %(aValue, bValue, aValue-bValue))

def operation_mul():
    print("{} * {} = {}".format(aValue, bValue, aValue*bValue))
    print("%d * %d = %d" %(aValue, bValue, aValue*bValue))

def operation_dev():
    print("{} / {} = {}".format(aValue, bValue, aValue/bValue))
    print("%d / %d = %d" %(aValue, bValue, aValue/bValue))

def operation_res():
    print("{} % {} = {}".format(aValue, bValue, aValue % bValue))

def operation_output():
    operation_add()
    operation_sub()
    operation_mul()
    operation_dev()
    operation_res()