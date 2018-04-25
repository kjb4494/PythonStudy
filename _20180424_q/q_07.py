
def q_07():
    #  두 수를 입력받아 최대공약수,최소 공배수를 구하는 프로그램을 작성하시오.

    # 입력
    # 두 양의 정수 a , b 가 입력으로 주어진다. (1 <= a , b <= 100 000)

    # 출력
    # 최대공약수,최소공배수를 한 줄에 출력한다.
    # 두 수의 최대공약수 와 최소 공배수는 정수 범위(2^31 - 1)를 넘지 않는다.
    while True:
        try:
            num01, num02 = map(int, input("두 정수 입력: ").split(' '))
            if not (1 <= num01 <= 100000 and 1 <= num02 <= 100000):
                print("입력 범위가 잘못되었습니다.")
                continue
            print("%d %d" % (euclid_method_gcd(num01, num02), euclid_method_lcm(num01, num02)))
            return

        except Exception as e:
            print("입력 값이 잘못되었습니다.", e)

def euclid_method_gcd(a, b):
    mod = a % b
    while mod > 0:
        a = b
        b = mod
        mod = a % b
    return b

def euclid_method_lcm(a, b):
    return a * b // euclid_method_gcd(a, b)