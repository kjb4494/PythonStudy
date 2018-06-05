import random
import socket
import dpkt


def affine_code():
    class Affine:
        def __init__(self):
            self.PlainText = ""  # 평문
            self.CipherText = ""  # 암호문
            self.mulKey = 0  # 곱셈에 대한 암호키
            self.addKey = 0  # 덧셈에 대한 암호키
            self.revMulKey = 0  # 곰셈에 대한 복화화키
            self.DecryptText = ""  # 복호된 문장, 후에 평문과 비교
            self.FieldList = list()

        def SetFieldList(self):
            # A ~ Z
            self.FieldList.extend(
                [chr(n) for n in range(ord('A'), ord('Z') + 1)])

            # a ~ z
            self.FieldList.extend(
                [chr(n) for n in range(ord('a'), ord('z') + 1)])

            # 0 ~ 9
            self.FieldList.extend(
                [chr(n) for n in range(ord('0'), ord('9') + 1)])

            # { ~ '~'
            self.FieldList.extend(
                [chr(n) for n in range(ord('{'), ord('~') + 1)])

            # : ~ @
            self.FieldList.extend(
                [chr(n) for n in range(ord(':'), ord('@') + 1)])

            #   ~ '/'
            self.FieldList.extend(
                [chr(n) for n in range(ord(' '), ord('/') + 1)])

        def KetSetting(self):
            """
                    덧셈에 대한 암호화키는 random (0, len(self.FieldList))
                    곰셈에 대한 암호화키는
                    최대 공약수가 1
                    gcd (k , len(self.FiledList)) = 1

                    곱셈에 대한 복호화키는
                    k x k^-1 = 1 (mod len(self.FiledList))
                    """
            print(len(self.FieldList))
            self.addKey = random.randint(0, len(self.FieldList))
            print("self.addKey => {}".format(self.addKey))
            mulKeySpaceList = []
            for i in range(2, len(self.FieldList)):
                cnt = 0
                for j in range(1, i + 1):
                    # 소수관계를 구하기 위한 부분
                    if (len(self.FieldList) % j == 0) and (i % j == 0):
                        cnt += 1
                if cnt == 1:
                    mulKeySpaceList.append(i)
            # print (mulKeySpaceList)
            indx = random.randint(0, len(mulKeySpaceList))
            self.mulKey = mulKeySpaceList[indx]
            print("self.mulKey => {}".format(self.mulKey))

            # 복호화 키
            for i in mulKeySpaceList:
                if (self.mulKey * i) % len(self.FieldList) == 1:
                    self.revMulKey = i
                    break

            print("self.revMulKey => {}".format(self.revMulKey))

        def plainTextWrite(self):
            self.PlainText = input("평문입력:  ")

        def EncrypAffine(self):
            for p in self.PlainText:
                if p in self.FieldList:
                    indx = (self.FieldList.index(p) + self.addKey) % len(self.FieldList)
                    indx = (indx * self.mulKey) % len(self.FieldList)
                    self.CipherText += self.FieldList[indx]
                else:
                    self.CipherText += p
            print("암호화 된 문장 {}".format(self.CipherText))

        def DecryptAffine(self):
            for c in self.CipherText:
                if c in self.FieldList:
                    indx = (self.FieldList.index(c) * self.revMulKey) % len(self.FieldList)
                    indx = (indx - self.addKey) % len(self.FieldList)
                    self.DecryptText += self.FieldList[indx]
                else:
                    self.DecryptText += c
            print("복호화 된 문장 {}".format(self.DecryptText))

        def sendPacket(self):
            echo = dpkt.icmp.ICMP.Echo()
            echo.id = random.randint(0, 0xffff)
            echo.seq = random.randint(0, 0xffff)
            random_key = random.randint(2, 20)
            print("key_value: {}".format(random_key))
            echo.data = self.CipherText.encode()

            icmp = dpkt.icmp.ICMP()
            icmp.type = dpkt.icmp.ICMP_ECHO
            icmp.data = echo

            s = socket.socket(socket.AF_INET, socket.SOCK_RAW, dpkt.ip.IP_PROTO_ICMP)
            s.connect(('192.168.0.6', 1))
            sent = s.send(bytes(icmp))

            print('send %d bytes' % sent)

    aff_object = Affine()
    aff_object.SetFieldList()
    aff_object.KetSetting()
    aff_object.plainTextWrite()
    aff_object.EncrypAffine()
    aff_object.sendPacket()
    aff_object.DecryptAffine()


def affine_output():
    affine_code()
