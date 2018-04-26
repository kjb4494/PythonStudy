
def q_02():
    # 문제: http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=980&sca=20
    # 달팽이 사각형
    # 배열을 쓰지않았을 때 참고: http://tibyte.kr/247
    
    # 다차원 배열 만들기
    # Metr = [[0]*x for _ in range(0, x)]
    # Metr = [[0 for i in range(x) in range(x)]]
    
    while True:
        # 조건에 따라 입력값 처리
        try:
            leng = int(input("크기 입력: "))
            if not 1 <= leng <= 100:
                print("1에서 100사이의 숫자로 입력해주세요.")
                continue
        except Exception as e:
            print("제대로 입력해라 진짜 손모가지 뿌러지기 싫으면 ㅡㅡ...", e)
            continue

        # 달팽이 배열 알고리즘
        # snail_array(leng)
        other_snail_algorithm(leng)
        # no_ary_snail_algorithm(leng)
        return

def snail_array(size):
    # 지능형 리스트를 이용해 2차원배열 생성
    ary = [[0 for j in range(size)] for i in range(size)]

    offset = 0       # 사이클 횟수
    num = 1          # 넣을 숫자
    nRows = size     # 배열의 가로 길이
    nCols = size     # 배열의 세로 길이
    while nRows > 0 and nCols > 0:
        for i in range(offset, offset + nCols):
            ary[offset][i] = num
            num += 1
        for i in range(offset + 1, offset + nRows):
            ary[i][offset + nCols - 1] = num
            num += 1
        for i in range(offset + nCols - 2, offset - 1, -1):
            ary[offset + nRows - 1][i] = num
            num += 1
        for i in range(offset + nRows - 2, offset, -1):
            ary[i][offset] = num
            num += 1
        offset += 1
        nRows -= 2
        nCols -= 2

    # 배열 출력
    for i in range(size):
        for j in range(size):
            if ary[i][j] >= 1000:
                print("%d" % ary[i][j], end="\t")
            else:
                print("%d" % ary[i][j], end="\t\t")
        print()

# 벽을 이용해 만든 달팽이 배열 알고리즘
def other_snail_algorithm(size):
    # 지능형 리스트를 이용해 2차원배열 생성
    size += 2
    ary = [[0 for j in range(size)] for i in range(size)]

    # 벽을 만든다.
    for i in range(size):
        for j in range(size):
            if i == 0 or j == 0 or i == size - 1 or j == size - 1:
                ary[i][j] = 1

    # 알고리즘
    num = 1
    x = 1
    y = 0
    while num <= (size - 2) * (size - 2):
        while ary[x][y+1] == 0:     # 오른쪽이 0인동안 오른쪽으로 이동
            y += 1
            ary[x][y] = num
            num += 1
        while ary[x+1][y] == 0:     # 아래쪽
            x += 1
            ary[x][y] = num
            num += 1
        while ary[x][y-1] == 0:     # 왼쪽
            y -= 1
            ary[x][y] = num
            num += 1
        while ary[x-1][y] == 0:     # 위쪽
            x -= 1
            ary[x][y] = num
            num += 1
    
    # 배열 출력
    for i in range(size):
        for j in range(size):
            if not (i == 0 or j == 0 or i == size - 1 or j == size - 1):
                if ary[i][j] >= 1000:
                    print("%d" % ary[i][j], end="\t")
                else:
                    print("%d" % ary[i][j], end="\t\t")
        print()

# 배열을 사용하지 않은 달팽이 알고리즘
def no_ary_snail_algorithm(n):
    for y in range(0, n):
        for x in range(0, n):
            p = min(x, y, n - x - 1, n - y - 1)
            if x >= y:
                q = x + y - 2 * p
            else:
                q = (n - 1 - 2 * p) * 4 - (x + y - 2 * p)
            q += 4 * (p * n - (p * p))
            if q > 1000:
                print("%d" % (q + 1), end="\t")
            else:
                print("%d" % (q + 1), end="\t\t")
        print()