
def q_01():
    # 10개의 정수를 입력받아 배열에 저장한 후 짝수 번째 입력된
    # 값의 합과 홀수 번째 입력된 값의 평균을 출력하는 프로그램을 작성하시오.
    # 평균은 반올림하여 소수첫째자리까지 출력한다.
    while True:
        try:
            sList = [i for i in map(int, input("정수 10개 입력: ").split(' '))][:10]
            print("짝수의 합: %d" % sum([sList[i] for i in range(1, len(sList), 2)]))
            print("홀수의 평균: %.1f" % round(sum([sList[i] for i in range(0, len(sList), 2)])/5, 2))
            return
        except Exception as e:
            print("입력 값이 잘못되었습니다.", e)