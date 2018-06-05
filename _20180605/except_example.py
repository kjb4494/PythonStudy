from ctypes import *  # c언어 함수 호출 라이브러리
from win32api import *


def libc_ex():
    libc = cdll.msvcrt
    libc.printf(b"hello wolrd")  # hello wolrd
    """
    함수호출 규약
    cdll -->    cdecl
                stdcall
                vectorcall
                fastcall
    """


def win32api_ex():
    try:
        CopyFile("C:\\Users\\kitri\\Desktop\\cp test\\cp.txt",
                 "C:\\Users\\kitri\\Desktop\\cp test\\cp_file.txt")
        print("success copy")
    except Exception as e:
        print("error", e)


def except_ex01():
    L = [10, 11, 12]
    # print(L[3])    # IndexError: list index out of range
    s = 'apple'
    # print(10 / s)  # TypeError: unsupported operand type(s) for /: 'int' and 'str'
    a = 10
    b = "hello"
    try:
        c = a/b
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print("무언가의 에러: ", e)
    # 성공했을 때
    else:
        print("c => {}".format(c))
    finally:
        print("끝")

def except_ex02():
    try:
        f = open("kitri.txt", "r")
    except IOError:
        print("해당하는 파일이 존재하지 않습니다.")
    else:
        print("파일을 성공적으로 처리하였습니다.")
        f.close()

def except_ex03():
    # 억지로 에러 발생 (raise)
    try:
        raise Exception("오류발생")
    except Exception as e:
        print(e)

def except_output():
    # libc_ex()
    # win32api_ex()
    # except_ex01()
    # except_ex02()
    except_ex03()
