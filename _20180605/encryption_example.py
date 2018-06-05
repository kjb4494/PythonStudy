import random
import socket
import dpkt

# 수업용 시저암호화
class Cea(object):
    def __init__(self):
        self.PlainText = ""  # 평문
        self.CipherText = ""  # 암호문
        self.EncryptKey = 0  # 암호화 키
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

    def writePlainText(self):
        self.PlainText = input("평문을 입력해주세요)  ")

    def KeyRet(self):
        self.EncryptKey = random.randint(0, len(self.FieldList))

    def EncryptPlainText(self):
        for p in self.PlainText:
            if p in self.FieldList:
                # 암호화 되는 과정
                # c = (p + key)mod(len(self.FieldList))
                indx = (self.FieldList.index(p) + self.EncryptKey) % (len(self.FieldList))
                self.CipherText += self.FieldList[indx]
            else:
                self.CipherText += p

        print("암호화된 문장은 {}".format(self.CipherText))

    def DecryptCipherText(self):
        for c in self.CipherText:
            if c in self.FieldList:
                # 암호화 되는 과정
                # c = (p + key)mod(len(self.FieldList))
                indx = (self.FieldList.index(c) - self.EncryptKey) % (len(self.FieldList))
                self.DecryptText += self.FieldList[indx]
            else:
                self.DecryptText += c

        print("복호화된 문장은 {}".format(self.DecryptText))

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

def cea():
    cea_object = Cea()
    cea_object.SetFieldList()
    cea_object.KeyRet()
    cea_object.writePlainText()
    cea_object.EncryptPlainText()
    cea_object.sendPacket()
    # cea_object.DecryptCipherText()

def brute_force():
    bf_object = Cea()
    bf_object.SetFieldList()
    bf_object.CipherText = input("스니핑한 암호문 입력: ")
    for i in range(1, len(bf_object.FieldList)):
        bf_object.DecryptText = ''
        bf_object.EncryptKey = i
        print("key number: {}".format(bf_object.EncryptKey))
        bf_object.DecryptCipherText()
        print()

def encrytion_example():
    # cea()
    brute_force()