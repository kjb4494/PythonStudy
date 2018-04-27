import sys
import os
import re

def system_test_01():
    # 1step: ipconfig 결과를 파일저장
    # 2step: ip만 가져옴
    # 내 아이피는 xxx.xxx.xxx.xxx 입니다.
    os.system("ipconfig > C:\\Users\\kitri\\Desktop\\MyIpInformation.txt")
    # f = open(file='C:\\Users\\kitri\\Desktop\\MyIpInformation.txt',
    #          mode='r')
    # f_str = re.compile("^(\d{3}).(\d{3}).(\d{1}).(\d{2})$")
    #
    # sList = f.readlines()
    # for s in sList:
    #     s = s.replace('\n', '')
    #     ssList = [ss for ss in s.split(' ')]
    #     for ss in ssList:
    #         if not f_str.search(ss) is None:
    #             print("내 아이피는 {} 입니다.".format(ss))

    f = open("C:\\Users\\kitri\\Desktop\\MyIpInformation.txt", "r")
    s = re.compile("(\d{3})\.(\d{3})\.(\d{1,3})\.(\d{2})")
    result = f.read()
    # read -> string / readlines -> list
    ip = s.search(result)
    print(ip)
    f.close()

def system_output():
    system_test_01()