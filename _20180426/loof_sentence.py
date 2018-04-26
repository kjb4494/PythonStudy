
def loof_test_01():
    # For 문

    # for i in range(start, end, jump):
    #   출력되는 범위 :
    #       if jump == 1: start ~ end - 1
    #       if jump == 2: start, start + 2, ... (end - 1 or end - 2)
    #   jump 생략 == jump 1일 경우
    # 증가
    #       for i in range(10, 20, -1)
    #       for i in range(10, 20, 1)
    # 감소
    #       for j in range(20, 9, -1)
    #       20, 19, 18, ... ,10
    # 이중 for문 - 별찍기, 행렬곱셈, 구구단
    #   for i in range(2, 10):
    #       for j in range(1, 10):
    #           print(i * j)

    # for element in iterableDate:
    # 출력 범위:
    #   iterableData가 가지고 있는 원소들을 모두 순회
    #       1) string
    #       2) list
    #       3) tuple
    #       4) dictionary
    #           -> 키값    .keys()
    #           -> 벨류    .values()
    #           -> 전체    .items()
    #       5) 숫자는 되지 않습니다. -- error

    s = [x for x in range(10)]
    for element in reversed(s):
        print(element, end=" ")         # 9 8 7 6 5 4 3 2 1 0

    print()

    for element in s[::-1]:
        print(element, end=" ")         # 위와 같다

    print()

    for i in range(len(s) - 1, -1, -1): # 위와 같다
        print(s[i], end=" ")

    print()

def loof_test_02():
    # While 문

    # 구조
    # while True:
    #       if 조건 ~~:
    #           break
    # a = 1
    # while a! = 10:
    #       a += 1

    # continue  : 아래 코드를 동작시키지않고 loof
    # break     : loof문을 빠져나감
    # pass      : 그냥 흘러감. 아무 동작도 하지않을 때 씀

    # while 문을 이용하여 구구단
    i = 2
    j = 1
    while i <= 9:
        while j <= 9:
            print("{} X {} = {}".format(i, j, i * j))
            j += 1
        i += 1
        j = 1
        print()

def loof_output():
    # loof_test_01()
    loof_test_02()