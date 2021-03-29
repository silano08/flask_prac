import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=171539'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url,headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 여기에 코딩을 해서 meta tag를 먼저 가져와보겠습니다.

# head > meta:nth-child(9) 그냥 이렇게 가져올시 None으로 찍히는 경우도 있음
# 그럴때는 meta태그 안에서 특정 조건을 붙여주는 것으로 값을 찾아야함
title = soup.select_one('meta[property="og:title"]')['content']
image = soup.select_one('meta[property="og:image"]')['content']
desc = soup.select_one('meta[property="og:description"]')['content']

# 코멘트랑 URL은 받아오는거니까 이렇게만 하면 됨
print(title,image,desc)