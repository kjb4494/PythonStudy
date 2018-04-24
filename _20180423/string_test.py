def string_test_01():
    sValue_01 = 'Python"s favorite food is perl'
    sValue_02 = "Python's favorite food is perl"
    sValue_03 = "Python\"s favorite food is perl"

    # error: "Python favorite food is perl'

    print(sValue_01)
    print(sValue_02)
    print(sValue_03)

def string_test_02():

    # 파이썬의 문자열은 +연산자와 *연산자를 쓸 수 있다.
    a = "Hello"
    b = "Wolrd"
    c = a + b
    print(c * 100)

def string_test_03():

    # 문자열의 음수 인덱스
    #   0   1   2   3   4   5   6   7   8   9   10
    #   H   e   l   l   o       W   o   l   r   d
    #   -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1

    a = "Hello Wolrd"
    print(a[:-1])
    print(a[3:-2])
    print(a[-10:])
    print(a[:])
    # 3번째 숫자는 점프다.
    print(a[3:8:2])
    # 역순으로 출력
    print(a[::-1])

def string_test_04():
    print("%03d" % 34)
    # 문자열 총합 10 왼쪽에 출력
    print("%-10s" % "hello")
    # 문자열 총합 10 오른쪽에 출력
    print("%10s" % "hello")

    print("-------------------")

    # 각각 왼쪽, 오른쪽, 가운데 정렬.
    # 공백은 #으로 대체
    print("{0:#<10}".format("hello"))
    print("{0:#>10}".format("hello"))
    print("{0:#^10}".format("hello"))



def string_test_05():
    # s가 가지고 있는 문자열에서 i개수
    count = 0
    s = "isadsadisaidaifsafiafi"
    for i in s:
        if i == 'i':
            count += 1
    print(count)
    
    # count 함수를 사용
    print(s.count('i'))

def string_test_06():
    # s가 가지고 있는 문자열에서
    # i의 모든 인덱스 (find 함수사용)
    s = "Kitri World"
    count = 1
    while True:
        tmp = s.find('i', count)
        if tmp != -1:
            print(tmp)
            count = tmp + 1
        else:
            break

def string_test_07():
    # index 함수
    s = "Kitri World"
    print(s.index('i'))
    # 없으면,
    # ValueError: substring not found
    # 에러가 난다.

def string_test_08():
    # 대문자로 바꾸기
    s = "Kitri Wolrd"
    for i in s:
        if 'a' <= i <= 'z':
            print(chr(ord(i) - 32), end="")
        else:
            print(i, end="")
    print()

    # UPPER 함수 사용하기
    print(s.upper())

    # 소문자로 바꾸기
    for i in s:
        if 'A' <= i <= 'Z':
            print(chr(ord(i) + 32), end="")
        else:
            print(i, end="")
    print()

    # LOWER 함수 사용하기
    print(s.lower())

def string_test_09():
    # STRIP 함수 사용하기
    sValue = "     hello wolrd        "
    print("%s : %d" % (sValue.strip(), len(sValue.strip())))
    print("%s : %d" % (sValue.lstrip(), len(sValue.lstrip())))
    print("%s : %d" % (sValue.rstrip(), len(sValue.rstrip())))

def string_test_10():
    # REPLACE 함수 사용하기
    sValue = "      hello wo   l rd    "
    print("%s : %d" % (sValue.replace(' ', ''), len(sValue.replace(' ', ''))))

def string_test_11():
    # split and join
    sValue = "hello world a b c d"

    # split을 사용하여 문자열을 화이트 스페이스 기준으로 나누기
    sList = sValue.split(sep=' ')
    print(sList)
    
    # join을 이용하여 여러 개의 문자열을 합치기
    jList = " ".join(sList)
    print(jList)

def string_test_12():
    # 문제: kList를 합쳐서 거꾸로 출력해라.
    kList = ['KITR', 'WORLD', 'HELLO', 'WOLRD']
    print(kList)
    print("--> %s" % (" ".join(kList))[::-1])

def string_test_output():
    # string_test_01()
    # string_test_02()
    # string_test_03()
    # string_test_04()
    # string_test_05()
    # string_test_06()
    # string_test_07()
    # string_test_08()
    # string_test_09()
    # string_test_10()
    # string_test_11()
    string_test_12()