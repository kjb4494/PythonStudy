def dim_test_01():
    # scalar
    v = 10

    # vector (1차원)
    vList = [10, 20, 30]

    # metrix
    # 2차원 배열
    metrix_A = [[1, 0], [0, 1]]
    for row in range(2):
        for col in range(2):
            print(metrix_A[row][col], end=" ")
        print()

    print()

    # 3차원 배열
    metrix_B = [[[1, 1, 1], [1, 1, 1], [1, 1, 1]],
                [[1, 1, 1], [1, 2, 1], [1, 1, 1]],
                [[1, 1, 1], [1, 1, 1], [1, 1, 1]]]
    print(metrix_B[1][1][1])

    # ########## 시험문제! ##########
def dim_test_02():
    # a를 찾아라.
    vList = [1, 2, 3, 4, 5, [5, 6, 7, 8, ['a'], 4, 5]]
    print(vList[5][4][0])

def dim_test_03():
    # 지능형 리스트를 사용하여 2차원배열 생성하기
    metix_A = [[0 for j in range(5)] for i in range(4)]
    print(metix_A)

def dim_output():
    # dim_test_01()
    # dim_test_02()
    dim_test_03()