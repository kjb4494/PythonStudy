def output_structure():
    print("{0:d} {1:.1f} {2:d}".format(10, 20, 30))
    # 출력결과: 10 20.0 30
    print("{1:d} {2:d} {0:d}".format(10, 20, 30))
    # 출력결과: 30 10 20
    print("{t} {t} {t}".format(f=10, s=20, t=30))
    # 출력결과: 30 30 30

def output_structure_ouput():
    output_structure()