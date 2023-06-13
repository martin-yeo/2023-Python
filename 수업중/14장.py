# import urllib.request
# url = "http://storage.googleapis.com/patents/grant_full_text/2014/ipg140107.zip"

# print("Start Download")
# fname, header = urllib.request.urlretrieve(url, 'ipg140107.zip')

# print("End Download")

# import re
# import urllib.request

# url = "http://goo.gl/U7mSQl"
# html = urllib.request.urlopen(url)
# html_contents = str(html.read())

# id_results = re.findall(r"(c[A-Za-z0-9]+\*\*\*)", html_contents)

# for result in id_results:
#     print(result)

# import re
# import urllib.request

# url = "https://www.naver.com"
# html = urllib.request.urlopen(url)
# html_contents = str(html.read())
# rex = r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

# id_results = re.findall(rex, html_contents)
    
# import requests
# from bs4 import BeautifulSoup

# header = {'User-Agent': 'Mozilla/5.0'}
# url = "https://www.mokwon.ac.kr/kr/"
# response = requests.get(url, headers=header)
# html = response.text
# soup = BeautifulSoup(html, 'html.parser')
# word = soup.select_one(".photo_list--item")
# print(word.text)

# import requests
# from bs4 import BeautifulSoup

# header = {'User-Agent': 'Mozilla/5.0'}
# url = "https://news.naver.com/"
# response = requests.get(url, headers=header)
# html = response.text
# soup = BeautifulSoup(html, 'html.parser')
# words = soup.select('.cjs_t')
# count = 1
# for w in words:
#     print(f'{count:2} :: {w.text}')
#     count += 1

# import requests
# from bs4 import BeautifulSoup

# keyword = input("검색어를 입력하세요: ")
# header = {'User-Agent': 'Mozilla/5.0'}
# url = "https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=" + keyword
# response = requests.get(url, headers=header)
# html = response.text
# soup = BeautifulSoup(html, 'html.parser')
# words = soup.select('.news_tit')

# f = open(f'news_{keyword}.txt', 'w')
# count = 1
# for w in words:
#     f.write(f'{count:2} :: {w.text}\n')
#     f.write(f'  >>  {w.attrs["href"]}\n')
#     count += 1

# import requests
# from bs4 import BeautifulSoup

# codes = ['005380', '035720', '005930', '066570']
# header = {'User-Agent': 'Mozilla/5.0'}
# f= open("오늘의시세.txt", "w")
# title = '오늘의 주요 종목 시세'
# f.write(f'|{title:^30}|\n')
# for code in codes:
#     url = "https://finance.naver.com/item/sise.naver?code=" + code
#     response = requests.get(url, headers=header)
#     html = response.text
#     soup = BeautifulSoup(html, 'html.parser')
#     company = soup.select_one('.wrap_company > h2')
#     price = soup.select_one('#_nowVal')
#     f.write(f'종목: {company.text:10} > {price.text}원\n')
    

import requests
from bs4 import BeautifulSoup

header = {'User-Agent': 'Mozilla/5.0'}
keyword = input("검색어를 입력 : ")
url = f"https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query={keyword}&oquery=ghks&tqi=i4QTbsp0J1ZsseZO45Cssssst9h-462701"
response = requests.get(url, headers=header)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
words = soup.select('.news_tit')
for w in words:
    print(">", w.text)


















# import requests
# from bs4 import BeautifulSoup
# import pyautogui

# keyword = pyautogui.prompt("검색어를 입력하세요: ")
# header = {'User-Agent': 'Mozilla/5.0'}
# response = requests.get(f"https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query={keyword}", headers=header)
# soup = BeautifulSoup(response.text, 'html.parser')
# news = soup.select(".news_tit")

# f = open(f'news_{keyword}.txt', 'w')

# count = 1
# for title in news:
#     print(f'{count:2} :: {title.text}\n  >> {title.attrs["href"]}')
#     f.write(f'{count:2} :: {title.text}\n  >> {title.attrs["href"]}\n')
#     count += 1

# f.close()

# import requests
# from bs4 import BeautifulSoup

# codes = [
#     '005930',
#     '000660'
# ]

# header = {'User-Agent': 'Mozilla/5.0'}
# for code in codes:
#     url = f'https://finance.naver.com/item/sise.naver?code={code}'
#     response = requests.get(url, headers=header)
#     html = response.text
#     soup = BeautifulSoup(html, 'html.parser')
#     codeInfo = soup.select_one('#_nowVal')
#     print(codeInfo.text)
