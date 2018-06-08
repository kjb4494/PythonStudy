
import urllib.request
from bs4 import BeautifulSoup

def crawling_ex01():
    url = "http://imgnews.naver.net/image/001/2018/06/08/C0A8CA3C00000163DCA3E6690004DC36_P2_20180608145407905.jpeg?type=w647"
    saveFileName = "aa.jpg"

    try:
        urllib.request.urlretrieve(url, saveFileName)
    except Exception as e:
        print("뭔가에러..", e)
    else:
        print("성공 ^^")

def crawling_ex02():
    # https://beomi.github.io/2017/01/20/HowToMakeWebCrawler/
    pass

def crawling_output():
    # crawling_ex01()
    crawling_ex02()