# import urllib.request
# url = "http://storage.googleapis.com/patents/grant_full_text/2014/ipg140107.zip"

# print("Start Download")
# fname, header = urllib.request.urlretrieve(url, 'ipg140107.zip')

# print("End Download")

# import re
# import urllib.request

# url = 'http://goo.gl/U7mSQl'
# html = urllib.request.urlopen(url)
# html_contents = str(html.read().decode('utf8'))
# id_results = re.findall(r"([A-Za-z0-9]+\*\*\*)", html_contents)

# for result in id_results:
#     print(result)
    
    
    
# import requests
# from bs4 import BeautifulSoup

# header = {'User-Agent': 'Mozilla/5.0'}
# response = requests.get("https://www.mokwon.ac.kr/kr/", headers=header)
# html = response.text
# soup = BeautifulSoup(html, 'html.parser')
# word = soup.select_one(".photo_list--item")
# print(word.text)

# import requests
# from bs4 import BeautifulSoup

# header = {'User-Agent': 'Mozilla/5.0'}
# response = requests.get("https://news.naver.com", headers=header)
# html = response.text
# soup = BeautifulSoup(html, 'html.parser')
# headlines = soup.select(".cjs_t")

# number = 1
# for headline in headlines:
#     print(number, "> ", headline.text)
#     number += 1


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

import requests
from bs4 import BeautifulSoup

codes = [
    '005930',
    '000660'
]

header = {'User-Agent': 'Mozilla/5.0'}
for code in codes:
    url = f'https://finance.naver.com/item/sise.naver?code={code}'
    response = requests.get(url, headers=header)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    codeInfo = soup.select_one('#_nowVal')
    print(codeInfo.text)
