
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"

req = requests.get(url)

print(req)		 # get은 단순히 응답코드만 가져옵니다.

html = req.text

#print(html)

soup = BeautifulSoup(html, 'html.parser')
result = soup.select('.thumb')

print(result)