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


def class_q():
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

def class_example_output():
    # class_01()
    # class_02()
    class_q()
