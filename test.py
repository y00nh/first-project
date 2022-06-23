import requests
from bs4 import BeautifulSoup

# requests 라이브러리를 사용해서 HTML 페이지를 요청한다.
# res 객체에 HTML 데이터가 저장되고, res.content 로 데이터 추출
res = requests.get('https://www.naver.com')

# HTML 소스를 가져온다.
soup = BeautifulSoup(res.content, 'html.parser')

# HTML 소스에서 title 태그를 가져온다.
# find 메소드를 통해서 태그를 검색할수 있다.
title = soup.find('title')

# title 태그의 text 출력
print(title.get_text())