# 콘솔 출력 보충
# escape character(탈출문자)

print('1.Hello.\r\nWorld')
print('2.Hello.\nWorld') # window 에서는 \r\n이랑 \n 차이없기때문에 \n 사용

print('3.Hello.\n\tWorld') # \t = tap
print('4.Hello.\n\t\bWorld') # \b = back space(한칸)

print('5.Hello.\n\'World\'') # \' 문자열내 홑따옴표
print('6.Hello."World"') # 전체를 '' 로 하고있기 때문에 \" 사용하지 않아도 오류X
print('7.Hello.\"World\"') 

print('8.Hello.\ World') # 이렇게 되는건 파이썬만 가능
print('9.Hello.\\ World') # \\ == 를 문자열에 표현하는 방법

print('10.Hello\0') #\0은 출력X 문자열의 끝을 알려줌

# 문자열 포맷팅 - 구닥다리~~
# %로 포맷코드를 시작
me = '저'
name = '박라온'
age = 13
print('%s는 %s입니다. %d살입니다.'%(me, name,age)) # 순서 바꾸면 안됨

print(f'{254.112233:.4f}') # 최신식
print('%4.4f' %(254.112233)) #구식



