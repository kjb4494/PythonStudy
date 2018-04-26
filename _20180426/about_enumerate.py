# pretty print
import pprint


def enu_test_01():
    # 데이터 가공 --> 빅데이터 --> 인공지능
    vList = [10, 20, 30, 40, 50]
    vDict = dict()
    for v in enumerate(vList):
        vDict[v[0]] = v[1]
        print(type(v), v[0], v[1])
    print(vDict)

    # zip = tuple
    vallist = [x for x in range(ord('A'), ord('Z') + 1)]
    keylist = [chr(y) for y in range(ord('A'), ord('Z') + 1)]
    dV = dict()
    for v in zip(keylist, vallist):
        # v[0] keylist의 원소
        # v[1] vallist의 원소
        dV[v[0]] = v[1]
    pprint.pprint(dV)


def enu_test_02():
    # 문제
    # 딕셔너리 구성
    # {key:value}
    # => {key:{key:{key:{key:{key:value}}}}}
    # {'A':{65:'a'}, 'B':{66:'b'}, ..., 'Z':{90:'z'}} 를 구성해보시오.
    vallist01 = [x for x in range(ord('A'), ord('Z') + 1)]
    vallist02 = [chr(x) for x in range(ord('a'), ord('z') + 1)]
    keylist = [chr(y) for y in range(ord('A'), ord('Z') + 1)]
    dV = dict()
    for v in zip(keylist, vallist01, vallist02):
        dV[v[0]] = {v[1]:v[2]}
    pprint.pprint(dV)
    # V의 v를 출력
    print("v출력: {}".format(dV['V'][86]))


def enumerate_output():
    # enu_test_01()
    enu_test_02()
