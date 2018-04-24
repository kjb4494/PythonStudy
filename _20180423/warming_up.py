# 구구단 출력하기
def gugudan():
    print("\n".join(["%d X %d = %d" % (i, j, i * j) \
                     for i in range(2, 10) for j in range(1, 10)]))

# 숫자를 입력받아 역삼각형 구하기
def reverse_star(num):
    print(''.join(["*" * (num - i + 1) + "\n" for i in range(1, num + 1)])[:-1])

def warming_up_output():
    num = int(input("숫자를 입력하시오: "))
    reverse_star(num)
    print("----------------------")
    gugudan()