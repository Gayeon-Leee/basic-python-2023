# urllib 패키지 불러오기

from urllib.request import Request, urlopen
# urllib.request에 포함돼 있는 urlopen() 함수에 URL을 지정하여 웹 페이지를 추출
# => urllib.reques == 웹페이지 읽기용 모듈

req = Request('https://www.naver.com') 
res = urlopen(req)
print(res.status) # => 웹 페이지의 상태 코드 출력

# => network 통한 request에 대한 response 가 internet 인 것 알 수 있음