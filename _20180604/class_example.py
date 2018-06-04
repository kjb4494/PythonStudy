# 클래스의 기본
def class_01():
    class Car(object):
        # Member variable (멤버 변수)
        w_ = 4
        d_ = 2

        # Instance variable (인스턴스 변수)
        def __init__(self, v1, v2):
            self.v1 = v1
            self.v2 = v2

        # Member function (멤버 함수)
        def f(self):
            print("w_ => {}".format(self.w_))
            print("d_ => {}".format(self.d_))

        # 소멸자 - 파이썬의 GC 덕분에 굳이 호출하지 않아도 된다.
        def __del__(self):
            print("소멸자가 호출되었습니다.")

    # Instance object (인스턴스 객체)
    car_object = Car(2, 3)

    # 생성된 이름의 공간 (namespace)
    print(dir())  # dir: 파이썬 내장 함수

    # 메모리 주소
    print("address(Car) => {0:#x}".format(id(Car)))
    print("address(car_object) => {0:#x}".format(id(car_object)))
    print("address(car_object) => {0:#x}".format(id(car_object.w_)))
    print("address(car_object) => {0:#x}".format(id(car_object.d_)))

    # 멤버 함수 f()호출
    car_object.f()

    # 인스턴스 변수 호출
    print("car_object.v1 => {}".format(car_object.v1))
    print("car_object.v2 => {}".format(car_object.v2))

    if isinstance(car_object, Car):
        print("네 맞워요 ^- ^")
    else:
        print("아니에용")

    # 해당 인스턴스 객체 클래스가 누구인지?
    class_of_car_object = car_object.__class__
    print(class_of_car_object)


# 클래스의 상속
def class_02():
    # 부모
    class P:
        v = 10

    # 자식
    class C(P):
        # private Call (외부참조 불가능 - 캡슐화)
        def __f(self):
            self.v = 12
            print(self.v)

        def set_v(self):
            self.__f()

    object_c = C()
    print("v of object_c => {}".format(object_c.v))

    # 자식 클래스인지?
    print(issubclass(C, P))  # True
    print(issubclass(C, object))  # True: 모든 객체는 object class와 자식관계에 있다.
    print(issubclass(C, C))  # True: 자기자신과는 언제나 부모자식 관계다.

    # 부모클래스 확인하기
    print(C.__bases__)  # P
    print(P.__bases__)  # object

    object_c.set_v()


def class_q1():
    class P():
        def __init__(self, xy1, xy2):
            self.xy1 = xy1
            self.xy2 = xy2

        def add_xy(self):
            return self.xy1[0] + self.xy2[0], self.xy1[1] + self.xy2[1]

        def sub_xy(self):
            return self.xy1[0] - self.xy2[0], self.xy1[1] - self.xy2[1]

    object_p = P((12, 32), (33, 23))
    print("좌표합: {}".format(object_p.add_xy()))
    print("좌표차: {}".format(object_p.sub_xy()))


def class_q2():
    class Oper():
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def oper_add(self):
            return self.x + self.y

        def oper_sub(self):
            return self.x - self.y

        def oper_mlt(self):
            return self.x * self.y

        def oper_dev(self):
            return self.x / self.y

    object_oper = Oper(100, 12)
    print("합: {}".format(object_oper.oper_add()))
    print("차: {}".format(object_oper.oper_sub()))
    print("곱: {}".format(object_oper.oper_mlt()))
    print("나누기: {}".format(object_oper.oper_dev()))


def class_03():
    class A:
        def __init__(self):
            print("A call")

    class B(A):
        def __init__(self):
            print("B call")
            super().__init__()

    class C(A):
        def __init__(self):
            print("C call")
            super().__init__()

    class D(B, C):
        def __init__(self):
            print("D call")
            super().__init__()

    d = D()


def class_04():
    class P:
        v = 0x12

    class C(P):
        # 이곳에 v가 있니? --> 없으면 부모로 이동
        w = 0x13

    c_object = C()
    w_object = C()
    print(hex(id(c_object)), hex(id(w_object)), hex(id(C)))  # 0x17819b59f98 0x17819b59fd0 0x17819c25b28
    print()
    # 초기상태는 주소가 같음
    print(hex(id(c_object.w)), hex(id(w_object.w)), hex(id(C.w)))  # 0x67506320 0x67506320 0x67506320
    print()
    # 값이 바뀌면 주소가 달라짐
    c_object.w = 12
    print(hex(id(c_object.w)), hex(id(w_object.w)), hex(id(C.w)))
    print()
    # y라는 변수가 없으면 생성 후 값 대입 --> 단, w_object에는 해당 변수가 없음 (미선언)
    c_object.y = 10
    print(hex(id(c_object.y)))
    print(c_object.w)
    print()
    # 클래스 자체에 추가해주면 파생 객체들도 변수 사용가능
    C.tmpValue = 0x100
    print(c_object.tmpValue)
    print(w_object.tmpValue)


# 오버라이딩
def class_05():
    class P_():
        # 멤버 함수
        def f(self):
            print("hello wolrd")

    class C_(P_):
        def f(self):
            print("i want to go home...")

    c_object = C_()
    c_object.f()

# 연산자 중복정의 1
def class_06():
    class Stu:
        def __init__(self):
            self.v = 10

        # other: 연산대상
        def __add__(self, other):
            self.v += other.v

    stu_object = Stu()
    stu_object_copy = Stu()
    print(type(stu_object))
    stu_object + stu_object_copy
    print(stu_object.v)
    print(type(stu_object))

# 연산자 중복정의 2
# 그 외 수치연산자 참고: http://blog.naver.com/PostView.nhn?blogId=dudwo567890&logNo=130164637746&parentCategoryNo=&categoryNo=39&viewDate=&isShowPopularPosts=false&from=postView
def class_07():
    class Num:
        def __init__(self, num):
            self.num = num

        def __add__(self, other):
            self.num += other

        def __cmp__(self, other):
            if self.num == other:
                print("same :)")
            else:
                print("nop! :(")

    object_num = Num(12)
    object_num + 12
    print(object_num.num)
    object_num.__cmp__(24)


def class_example_output():
    # class_01()
    # class_02()
    # class_q1()
    # class_q2()
    # class_03()
    # class_04()
    # class_05()
    # class_06()
    class_07()