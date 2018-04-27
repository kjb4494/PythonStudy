
import pprint

# 파일 .text
#
#  쓰기
# 	f = open("파일이름", "w")   <--- "열고"
# 	f.write("hello world")
# 	f.close()                 <--- "닫기" 생략 가능
# 	writelist(x) : x는 리스트의 형태
# 	w/w+ (읽고, 쓰기 모두 가능)
#  	a : append 추가
# 	wb : write byte
#
#  읽기
# 	f = open("대상이되는 파일", "r") read <---- "열고"
# 	f.read(x) x는 바이트(byte) 단위
# 	x 생략시 전체 값 읽어 들어 옮
# 	f.readline() # 한줄 한줄
# 	f.readlines()  # 전체
#
#  	r/r+ (읽고, 쓰기 모두 가능)
# 	rb : read byte :

def file_test_01():
    # f = open("파일이름", "w")
    f = open(file='C:\\Users\\kitri\\Desktop\\createFile.txt',
             mode='w')

    f.write("hello wolrd\n")
    f.write("kitri\n")

    for i in range(1, 11):
        f.write(str(i) + "\n")

    f.close()

def file_test_02():
    f = open(file='C:\\Users\\kitri\\Desktop\\createFile.txt',
             mode='r')

    s = f.read(2)       # 2바이트만 읽음
    print(s)
    f.close()

def file_test_03():
    sList = ["banana", "apple", "kiwi"]
    f = open("과일.txt", "w")
    f.write('\n'.join(sList))
    f.close()

def file_test_04():
    f = open("과일.txt", "r")
    element = f.readline()      # 한 줄만
    element = f.readlines()     # 전체
    print(element)
    f.close()

def file_output():
    # file_test_01()
    # file_test_02()
    # file_test_03()
    file_test_04()