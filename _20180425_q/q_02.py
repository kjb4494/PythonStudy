
def q_02():
    # 문제: http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=980&sca=20
    # 달팽이 사각형
    # 배열을 쓰지않았을 때 참고: http://tibyte.kr/247
    while True:
        try:
            leng = int(input("크기 입력: "))
            if not 1 <= leng <= 100:
                print("1에서 100사이의 숫자로 입력해주세요.")
                continue
        except Exception as e:
            print("제대로 입력해라 진짜 손모가지 뿌러지기 싫으면 ㅡㅡ...", e)
            continue
        reg_arr = [[0 for j in range(leng)] for i in range(leng)]

        snail_array(reg_arr)

        for i in range(leng):
            for j in range(leng):
                if reg_arr[i][j] >= 1000:
                    print("%d" % reg_arr[i][j], end="\t")
                else:
                    print("%d" % reg_arr[i][j], end="\t\t")
            print()
        return

def snail_array(ary):
    offset = 0
    num = 1
    nRows = len(ary[0])
    nCols = len(ary[0])
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