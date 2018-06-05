import os
import hashlib


# http://implbits.com/products/hashtab/

def os_dir_ex():
    os.chdir("C:\\Users\\kitri\\Desktop\\cp test")
    # print(os.getcwd())
    for f in os.listdir():
        t = os.path.abspath(f)
        print(os.path.split(t))

    """
    os.remove(filename or path) : 파일 삭제/디렉토리 삭제
    os.mkdir(path): path 디렉토리가 생성
    os.path.abspath(filename) : 절대경로
    os.path.basename(filename) : 파일명만 추출
    os.pardir(): 부모디렉토리 얻기
    """


def hashlib_ex_01():
    object_sha1 = hashlib.sha1()
    object_sha1.update(b"Kim Hwi Su")
    print(object_sha1.digest())  # type: String
    print(object_sha1.hexdigest())
    print(len(object_sha1.hexdigest()) * 4)  # byte: 4


def hashlib_ex_02():
    BUF_SIZE = 65536
    SHA_1 = hashlib.sha1()

    os.chdir("C:\\Users\\kitri\\Desktop\\cp test")
    for f in os.listdir():
        with open(file=f, mode='rb') as ff:
            while True:
                data = ff.read(BUF_SIZE)
                if not data:
                    break
                else:
                    SHA_1.update(data)
            print("파일명: {}\nSHA_1 해쉬값: {}\n".format(f, (SHA_1.hexdigest()).upper()))


def virus_check_output():
    # os_dir_ex()
    # hashlib_ex_01()
    hashlib_ex_02()
