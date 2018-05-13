## 파이썬 수업

> 해당 레파지토리는 KITRI 모의해킹 17기 파이썬 수업 내용을 다룹니다.

> Python 3.6 버전을 사용합니다.

> 수업일: 2018-04-23 ~ 2018-04-27

#### Study.py
> 메인함수입니다. 패키지를 수업 날짜 단위로 불러올 수 있습니다.

#### _날짜 패키지
> 'Ouput_날짜' 모듈에서 불러올 모듈을 관리할 수 있습니다. 각 모듈은 수업내용이 담겨있습니다.

> 각 모듈의 함수는 모듈 내의 _output 함수로 관리됩니다.

#### INTRO
> 패러다임의 분류
- 절자지향 언어: c언어
- 객체지향 언어: Java, Python(script, 접합언어), 클래스(class), JavaScript
- 함수지향 언어: Haskell

> 형 검사에 따른 분류
- int, char, short, long, float, double, string ... 

> 약한 타입언어(weak typing): Python
- 유지보수를 위한 표기법 예시: cData_int = 0x10
- 강한 타입언어(string typing): c, go, java

> 해석에 따른 분류
- Complier : 기계가 이해하는 언어로 convert (.obj)
- 인터프리터 : 한 줄 단위로 해석. 대화형 언어

> Python 3.x vs Python 2.x
- 10/3 : 3버전은 3.3333... 2버전은 3으로 출력된다.
- long형이 없어지고 int형으로 통일

> 수치형
>> 정수형 --- 십진수, 16진수, 8진수, 2진수
- 십진수 : 0~9
- 16진수: 0~9, A~F
- 8진수: 0~7
- 2진수: 0, 1
>> 실수형
- float

> 진수변환
- aDecimal = 14
- hex(aDecimal) = '0xe'
- oct(aDecimal) = '0o16'
- bin(aDecimal) = '0b1110'

> 표기법
- Snake: even_number
- 낙타: evenNumber

> 주석
- \# 또는 ''' : 한줄 주석
- """ : 여러줄 주석
- 컨트롤+/
