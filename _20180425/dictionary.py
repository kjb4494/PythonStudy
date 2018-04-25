def dic_test_01():
    # dictionary 선언
    # case 1 초기화 된 형태
    dic_01 = {'one': 1, 'two': 2, 'three': 3}

    # 데이터 타입 확인
    print(type(dic_01))  # class dict

    # 데이터 접근
    print(dic_01['one'])  # 1

    # 반복문 접근
    # dictionary key 접근 .keys
    for key in dic_01.keys():
        print(key, end=" ")  # "one", "two", "three"

    print()

    # dictionary value 접근 .values
    for value in dic_01.values():
        print(value, end=" ")  # 1, 2, 3

    print()

    # dictionary key, value 동시 접근 .items
    for item in dic_01.items():
        print(item, end=" ")  # ('one', 1) ('two', 2) ('three', 3)


def dic_test_02():
    dic_01 = {'one': 1, 'two': 2, 'three': 3}

    # item 추가하기
    dic_01['four'] = 4
    print(dic_01)

    # 추가할 때 기존에 있는 키 값이라면?       in 활용
    if 'three' in dic_01.keys():
        print("이미 있는 키 값입니다.")
    else:
        pass


def dic_test_03():
    # 문제 : 아스키코드표를 활용하여 다음과 같은 구조의 딕셔너리 생성해보세요.
    # A: 65 ... Z: 90, a: 97 ... z: 122
    ascii_dict = dict()
    for i in range(65, 91):
        ascii_dict[str(i)] = chr(i)
    for i in range(97, 123):
        ascii_dict[str(i)] = chr(i)
    print(ascii_dict)


def dic_test_04():
    # for문을 이용하여 dictionary 생성
    dicW = {x: x ** 2 for x in range(1, 10)}
    print(dicW)

def dic_test_05():
    # 임의의 문자열 입력
    # ex) "hello a b c a b c hello"
    # 결과물
    # key   : value
    # hello : 2
    # a     : 2
    # b     : 2
    # c     : 2
    nList = [s for s in map(str, input("문자열 입력: ").split(' '))]
    nDic = dict()
    for s in nList:
        if s in nDic.keys():
            for key in nDic.keys():
                if key == s:
                    nDic[s] += 1
        else:
            nDic[s] = 1
    print(nDic)

def dictionary_output():
    # dic_test_01()
    # dic_test_02()
    # dic_test_03()
    # dic_test_04()
    dic_test_05()