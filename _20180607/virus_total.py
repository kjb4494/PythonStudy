import requests
import os
import hashlib
import pprint
import mysql.connector as myConn

apikey = '15b841c3fa1ea901a71c36690fb1a8f8602c197035089fd3721eb70542e6ff18'


def searchFiles():
    BUF_SIZE = 65536
    SHA_1 = hashlib.sha1()
    os.chdir("C:\\Users\\kitri\\Desktop\\cp test")
    # print(os.getcwd())
    for f in os.listdir():
        # t = os.path.abspath(f)
        # fileScan(t)
        with open(file=f, mode='rb') as ff:
            while True:
                data = ff.read(BUF_SIZE)
                if not data:
                    break
                else:
                    SHA_1.update(data)
            fileReport(SHA_1.hexdigest().upper())


def fileScan(abspath):
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': apikey}
    files = {'file': (abspath, open(abspath, 'rb'))}
    response = requests.post(url, files=files, params=params)
    pprint.pprint(response.json())


def fileReport(hash):
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {'apikey': apikey, 'resource': hash}
    response = requests.get(url, params=params)
    pprint.pprint(response.json())


def db_connect():
    coonectObject = myConn.connect(
        host="127.0.0.1",
        user="root",
        password="P@ssw0rd"
    )


def virus_total():
    searchFiles()
