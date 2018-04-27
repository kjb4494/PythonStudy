def pyIn_test_01():
    # 1. .py 의 파이썬 파일을 ".exe" 파일로 만들기
    #
    # 2. 환경변수
    # 	C:\Users\kitri\AppData\Local\Programs\Python\Python35\Scripts
    #
    # 3. 패키지 : pyintaller => .py 파일을 -> .exe 파일로 변환
    #
    # 4. 시스템 -> 고급시스템 설정 -> path
    #
    #        ;C:\Users\kitri\AppData\Local\Programs\Python\Python35
    #        ;C:\Users\kitri\AppData\Local\Programs\Python\Python35\Scripts
    # 		- pip 를 사용하기 위한 작업 입니다.
    #
    # 5. cmd 창을 열고 : "pip install pyinstaller" 실행
    # [+] 패키지를 설치하기 전에 반드시 pip search pyinstaller 로 해당하는 패키지가 존재하는지
    #     반드시 확인하는 절차 진행할 것
    # [+] 참고 pyinstaller는 python3.x 버전에서만 가능
    #
    # 6. 명령어 : pyinstaller -F -n targetFilename stu_1.py
    #
    # 7. cd dist

    print("Hello World ^^")

def pyinstaller_output():
    pyIn_test_01()