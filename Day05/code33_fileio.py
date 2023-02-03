# 파일만들기
file = open('../sample07.txt', 'w', encoding='utf-8') # 파일을 쓰기로 만듦. encoding으로 utf-8 사용해줘야 모든 언어 사용 가능
# 글자 인코딩
# ASCII -> 한 단어를 표현하는 체계(영어)
# Unicode(UTF-8) -> 모든 나라 언어가 표현 가능

file.write('안녕하세요~\n')
file.write('두번째 파일이다!\n')
file.write('절대경로에 파일이 생성될겁니다.\n')

file.close()
print('samle07.txt가 생성되었습니다.')


# 파일/폴더 생성 경로

# Absolute folder (절대경로) : root forder부터 ~ 끝까지 모든 경로를 다 적어주는 것
# file = open('sample.txt', 'w', encoding='utf-8') 절대경로X
# file = open('C:\\DEV\\Temp\\Bank\\sample01.txt', 'w', encoding='utf-8') 절대경로O
# C:\\DEV\\Temp\\Bank\\ 로 텍스트 파일 만들 경로 지정한 것임 . root folder는 c드라이브

#상대경로
# file = open('./sample05.txt', 'w', encoding='utf-8') ./ 내 위치
# file = open('./Day05/../Day04/sample06.txt', 'w', encoding='utf-8') 현재 위치 근처에 만들때 많이 사용
# file = open('../sample07.txt', 'w', encoding='utf-8') ../ 부모폴더