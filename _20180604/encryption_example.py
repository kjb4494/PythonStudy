import random
import socket
import string
import dpkt

# 내가 짠 시저암호화
def caesar_cipher():
    class Caesar_cipher:
        def __init__(self, key_value):
            self.key_value = key_value
            self.alphabet_lower = list(string.ascii_lowercase)
            self.alphabet_upper = list(string.ascii_uppercase)

        def encryption(self, s):
            s = list(s)
            self.s = s
            for i, char in enumerate(s):
                if char in self.alphabet_lower:
                    position = (self.alphabet_lower.index(char) + self.key_value) % 26
                    s[i] = self.alphabet_lower[position]
                elif char in self.alphabet_upper:
                    position = (self.alphabet_upper.index(char) + self.key_value) % 26
                    s[i] = self.alphabet_upper[position]
                else:
                    pass
            result = ''.join(s)
            print("암호화 완료: {}".format(result))
            return result

        def decryption(self):
            for i, char in enumerate(self.s):
                if char in self.alphabet_lower:
                    position = (self.alphabet_lower.index(char) - self.key_value) % 26
                    self.s[i] = self.alphabet_lower[position]
                elif char in self.alphabet_upper:
                    position = (self.alphabet_upper.index(char) - self.key_value) % 26
                    self.s[i] = self.alphabet_upper[position]
                else:
                    pass
            result = ''.join(self.s)
            print("복호화 완료: {}".format(result))
            return result

    echo = dpkt.icmp.ICMP.Echo()
    echo.id = random.randint(0, 0xffff)
    echo.seq = random.randint(0, 0xffff)
    random_key = random.randint(2, 20)
    print("key_value: {}".format(random_key))
    object_caesar = Caesar_cipher(random_key)
    echo.data = object_caesar.encryption(input("전송할 평문을 입력해주세요.\n")).encode()

    icmp = dpkt.icmp.ICMP()
    icmp.type = dpkt.icmp.ICMP_ECHO
    icmp.data = echo

    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, dpkt.ip.IP_PROTO_ICMP)
    s.connect(('192.168.0.6', 1))
    sent = s.send(bytes(icmp))

    print('send %d bytes' % sent)

# 수업용 시저암호화
def cea():
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

    cea_object = Cea()
    cea_object.SetFieldList()
    cea_object.KeyRet()
    cea_object.writePlainText()
    cea_object.EncryptPlainText()
    cea_object.DecryptCipherText()

def encrytion_example():
    # caesar_cipher()
    cea()