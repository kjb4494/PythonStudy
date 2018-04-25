import time

def fibonacci_test():
    # 파이썬 최적화 코드
    # --- 0.14062952995300293 seconds ---
    num = int(input("몇번째 수를 볼래?: "))
    print("==측정시작!==")
    start_time = time.time()
    a, b = 1, 0
    for i in range(num):
        a, b = b, a + b
    print(b)
    print("--- %s seconds ---" % (time.time() - start_time))

    # 행렬을 이용한 방법
    # https://ko.wikipedia.org/wiki/%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98_%EC%88%98
    # --- 2.54697847366333 seconds ---
    pivonachiMatrix = [[1, 1], [1, 0]]
    tmpMatrix = [[1, 1], [1, 0]]
    resultMatrix = [[1, 1], [1, 0]]
    numIndx = int(input("몇번째 수를 볼래?:  "))
    print("==측정시작!==")
    start_time = time.time()
    for cnt in range(numIndx - 1):
        for i in range(0, 2):
            for r in range(0, 2):
                numBer = 0
                for c in range(0, 2):
                    numBer += (pivonachiMatrix[i][c] * tmpMatrix[c][r])
                    """
                    ic     cr
                    00     00
                    01     10 
                    """
                resultMatrix[i][r] = numBer

        for k in range(0, 2):
            for s in range(0, 2):
                pivonachiMatrix[k][s] = resultMatrix[k][s]
        # ppr.pprint(resultMatrix)
    print(resultMatrix[0][1])
    print("--- %s seconds ---" % (time.time() - start_time))

def q_fibonacci_output():
    fibonacci_test()