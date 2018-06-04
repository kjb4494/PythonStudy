# import re
#
# re.compile("~~~~~")
#
#  (1) '*' : 바로 앞에 있는 문자가 0번 이상 나타남
# 	ex) re.compile("a*")
# 		apple (t)
# 		aapple (t)
# 		bbb (t)
#
#  (2) '+' : 바로 앞에 있는 문자가 1번 이상 나타남
# 	ex) re.compile("a+")
# 		apple (t)
# 		aapple (t)
# 		bbb (f)
#
#  (3) [] : [A-Z] : A-Z사이의 한개의 문자 중 하나가 나타날 경우 참
# 	ex) re.compile("[A-Z]")
#
#
#  (4) [^] : [^A-Z] : (3)의 여집합 ~(A-Z)
#
#
#  (5) ( ) : 우선순위
# 	ex) (a*b)*
# 		abab
# 		bbbn
#
#  (6) '|' : or
# 	ex (a|b)+
# 		apple
# 		bpple
#
#
#  (7) {X,Y} : X이상 Y이하
# 	ex) re.complie("a{2,5}b{3,4}")
# 		aabbb
# 		aaab (x)
# 		aaabbbb (0)
#
#  (8) ^ : ^app : app로 시작하는 문자열이 참
#
#  (9) $ : pple$ : pple로 끝나는 문자열이 참
#
#  (10) . : 문자하나가 대체
#
# 	re.comple(".pple")
# 	  apple, bpple, cpple, %pple , &pple
#
#  (11) \d == [0-9]
#   010-1234-1234
#   010-123-1234
#   re.compile("(\d{3})-(\d{3,4})-(\d{4})")
#
#   (\d{3})-(\d{3,5})-(\d{4})
#
#
#  '(' : 우선순위 0순위
#  '\d' : d == decimal == [0-9]
#  '{3}' : 갯수 (3)
#  032-1234-1234
#  032-123-1234
#
#  (12) \w : [a-zA-Z0-9 ]
# 	ex) re.compile('\w+pple')
# 		apple , Apple, 0pple,  pple
#  (13) \W : [^a-zA-Z0-9 ]
#
#  (14) \D : \d
#
#  (15) \s : [ \t\n\r\f\v]
#
#  (16) \S : \s의 여집합
#
#  flag -----------------------
#
#  f = re.compile(pattern, flag)
#  flag = r.I or r.IGNORECASE : 대소문자를 구별하지 않겠습니다.
#
#  예)
#  f = re.compile(pattern = '^apple', flag = r.I or r.IGNORECASE)
#  str1 = "apple"
#  str2 = "APPLE"
#
#  f.search(str1) => true / false : None
#  f.search(str2) => true / false : None
#
#  f.match()   vs     f.search()
#  시작위치             문자열 전체에서 대상을 찾음 (물론 ^, $)
#
#  s = "hello world"
#  f = re.compile("world")
#  print(f.search(s))   =>  span
#  print(f.match(s))    =>  None


import re


def reg_exp_test_01():
    f = re.compile("a*")
    strValue = "apple banana"
    result = f.search(strValue)
    print(result)
    print(result.span())  # span=(0, 1) data type tuple
    v = result.span()  # packing
    print(strValue[v[0]:v[1]])  # unpacking


def reg_exp_test_02():
    f = re.compile("[A-Z0-9]+pple")
    strValue = "!pple $pple Apple apple 0pple"

    # 조건을 만족하는 문자열 모두를 찾을 때
    sList = [s for s in strValue.split(' ')]
    for s in sList:
        if not f.search(s) is None:
            print(s)


def reg_exp_test_03():
    f = re.compile("^da")
    strValue = "da dododfm dcde apple daidrag app"
    result = f.search(strValue)
    print(result)


def reg_exp_test_04():
    f = re.compile("(\d{1,3}).(\d{1,3}).(\d{1,3}).(\d{1,3})")
    MyIp = "내 아이피는 192.168.0.12 입니다."
    result = f.search(MyIp)
    v = result.span()
    print(MyIp[v[0]:v[1]])


def reg_exp_output():
    # reg_exp_test_01()
    # reg_exp_test_02()
    # reg_exp_test_03()
    reg_exp_test_04()