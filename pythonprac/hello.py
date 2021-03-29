import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

### DB import
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

##################

# 텍스트만 출력
# title = soup.select_one('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')
# print("title.text : "+title.text , title['href'] )

#old_content > table > tbody > tr:nth-child(2)
#old_content > table > tbody > tr
#old_content > table > tbody > tr:nth-child(2) > td.title > div > a
#old_content > table > tbody > tr:nth-child(2) > td.point

#old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img
#old_content > table > tbody > tr:nth-child(3) > td:nth-child(1) > img

#old_content > table > tbody > tr:nth-child(2) > td.title > div > a
#old_content > table > tbody > tr:nth-child(2) > td.point

trs = soup.select('#old_content > table > tbody > tr')


for tr in trs:
    a_tag = tr.select_one('td.title > div > a')
    start = tr.select_one('td.point')
    if a_tag is not None:
        title = a_tag.text
        star = start.text
        rank = tr.select_one('td:nth-child(1) > img')['alt']
        doc = {
            'rank':rank,
            'title':title,
            'star':star
        }
        db.movie.insert_one(doc)

################