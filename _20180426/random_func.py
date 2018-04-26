import random


def random_test_01():
    print(random.random())

    # 그룹에서 7개 랜덤으로 뽑음. 중복 ㄴㄴ
    p = [i for i in range(1, 46)]
    s = set(random.sample(p, 7))
    print(s)


def random_test_02():
    # 번호는 1 ~ 45
    # 오늘의 당첨 로또 : 랜덤, 보너스 (총 7개)
    # 본인의 랜덤 로또 : 입력
    # 5등    : 3개
    # 4등    : 4개
    # 3등    : 5개
    # 2등    : 5개 + 1개
    # 1등    : 6개
    my_number = []
    while True:
        try:
            my_number = set([x for x in map(int, input("로또 번호 6개 찍어 ㅎㅎ: ").split(' ')) if 1 <= x <= 45])
            if len(my_number) != 6:
                print("1~45사이 숫자로 6개 뽑으라고 ㅡㅡ...")
                continue
            else:
                break
        except:
            print("입력 제대로해라. 죽빵맞는다.")
            continue

    print(end="\n\n")

    lotto_number = random.sample([i for i in range(1, 46)], 7)
    bonus_number = lotto_number[6]      # 보너스 번호
    del lotto_number[6]
    lotto_number = set(lotto_number)    # 보너스 번호를 뺀 순수 로또 당첨 번호
    
    print("로또 번호: {}".format(", ".join(str(i) for i in lotto_number)), end=" / ")
    print("보너스 번호: %d" % bonus_number)
    print("뽑은 번호: {}".format(", ".join(str(i) for i in my_number)))
    print("맞춘 번호: {}개".format(len(lotto_number & my_number)), end=" / ")
    print("보너스: {}".format("맞춤" if bonus_number in my_number else "못 맞춤"))

    print("결과: ", end="")

    if len(lotto_number & my_number) == 6:
        print("와 1등!")
    elif (bonus_number in my_number) and len(lotto_number & my_number) == 5:
        print("와 2등!")
    elif len(lotto_number & my_number) == 5:
        print("와 3등!")
    elif len(lotto_number & my_number) == 4:
        print("4등")
    elif len(lotto_number & my_number) == 3:
        print("5등")
    else:
        print("꽝 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")

def random_output():
    # random_test_01()
    random_test_02()