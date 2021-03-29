######## 라이브러리

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

### DB import
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

#######################################
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
#
# tree = soup.select('#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis')
# print(tree)

######################################
#
# # 순위 / 곡 제목 / 가수

tree = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for i in tree:
    title = i.select_one('td.info > a.title.ellipsis').text.strip()
    artist = i.select_one('td.info > a.artist.ellipsis').text.strip()
    rank = i.select('td.number')[0].text[0:2].strip()
    print(rank, title, artist)

################ rank만 따로 구하기
# tree = soup.select('#body-content > div.newest-list > div > table > tbody > tr:nth-child(33) > td.number')[0]
# print(tree.text.strip()[0:2])