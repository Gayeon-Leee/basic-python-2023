# urllib 패키지 불러오기
from urllib.request import Request, urlopen

req = Request('https://www.naver.com') # => network 통한 request에 대한 response 가 internet 인 것 알 수 있음
res = urlopen(req)
print(res.status)